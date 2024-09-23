import requests
from datetime import datetime, timedelta
from func_ad import calcular_linhas_AD
from func_dateTime import calcular_horarios
from func_envio import enviar_para_telegram
from concurrent.futures import ThreadPoolExecutor, TimeoutError
import time

URL_API = "https://blaze.com"


class BlazeAPI(object):
    def __init__(self):
        self.session = requests.Session()

    def get_last_doubles(self):
        # Obtendo a hora atual menos dois minutos
        hora = datetime.now() - timedelta(minutes=2)
        current_time = datetime.now() - timedelta(minutes=2)
        hora -= timedelta(hours=3)  # Para ajustar a hora que vai ser alocada na função, quando em ambiente de produção
        hora = hora.strftime("%H:%M")  # hora antes do ajuste

        # Ajuste por conta do fuso horário onde esta hospedada a API
        #current_time += timedelta(hours=3) #para executar em ambiente de desenvolvimento

        formatted_time = current_time.strftime("%H:%M")  # Hora depois do ajuste

        print("print hora: ", hora)
        print("print hora com fuso horário: ", formatted_time)
        
        # Nova API = https://blaze.com/api/singleplayer-originals/originals/roulette_games/recent/1

        response = self.session.get(f"{URL_API}/api/singleplayer-originals/originals/roulette_games/recent/1")
        if response.status_code == 200:
            doubles = response.json()
            last_doubles = []
            for item in doubles:
                color = "branco" if item["color"] == 0 else "vermelho" if item["color"] == 1 else "preto"
                created_date = datetime.strptime(item["created_at"], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%H:%M")
                if created_date == formatted_time and color in ["vermelho", "preto"]:
                    last_doubles.append({"color": color, "value": item["roll"], "created_date": created_date})
            return last_doubles, hora
        else:
            print("Falha ao obter os últimos resultados da roleta:", response.status_code)
            return None, hora


def lida_resultados(resultados, hora):
    print("Hora dentro da função lida_resultados: ", hora)

    if resultados:
        # Aloca os valores obtidos na rodada referente ao horario de execução
        ah = resultados[0]["value"] if len(resultados) > 0 else 0
        al = resultados[1]["value"] if len(resultados) > 1 else 0

        valores_ah_al = [ah, al]
        horario_ah7 = hora

        array_ad = calcular_linhas_AD(valores_ah_al, horario_ah7)

        AH7 = horario_ah7
        valores_AD = array_ad

        # Chama a função para calcular os horarios
        if valores_AD is None:
            print(valores_AD)
            print(f"Não é possível obter os horários para essa hora de execução: {hora} ")
            return
        else:
            horarios = calcular_horarios(AH7, valores_AD)

        # Printa os resultados na tela e os coloca em um array, ja formatados
        resultados_formatados = []
        for hora in horarios:
            print(hora + " ⚪")
            resultados_formatados.append(hora + " ⚪")

        return resultados_formatados
    else:
        print("Nenhum resultado encontrado para adicionar à planilha.")
        return []


def executar_com_timeout(func, args=(), timeout=10):
    with ThreadPoolExecutor() as executor:
        future = executor.submit(func, *args)
        try:
            return future.result(timeout=timeout)
        except TimeoutError:
            print("Timeout: reiniciando a função")
            return None


def main():
    # Defina os horários específicos em que deseja executar a tarefa
    horarios_especificos = [
        "00:02", "01:03", "02:04", "03:05", "04:06", "05:07", "06:08", "07:09", "08:10",
        "09:11", "10:12", "11:13", "12:14", "13:15", "14:16", "15:17", "16:18", "17:19",
        "18:20", "19:21", "20:22", "21:23", "22:24", "23:25"
    ]

    hora_atual = datetime.now()
    hora_atual -= timedelta(hours=3)
    hora_atual = hora_atual.strftime("%H:%M")
    print("Hora atual: ", hora_atual)

    if hora_atual in horarios_especificos:
        ba = BlazeAPI()
        resultados, hora = ba.get_last_doubles()
        print("Resultados obtidos da roleta: ", resultados)
        horarios_formatados = executar_com_timeout(lida_resultados, (resultados, hora), timeout=10)

        while horarios_formatados is None:
            horarios_formatados = executar_com_timeout(lida_resultados, (resultados, hora), timeout=10)

        enviar_para_telegram(horarios_formatados)
    else:
        print("Não estamos no horário programado")


if __name__ == "__main__":
    main()
