from datetime import datetime, timedelta
from config import RISCO

# Função para converter hora no formato "hh:mm" para minutos
def hora_para_minutos(hora):
    partes = hora.split(":")
    return int(partes[0]) * 60 + int(partes[1])


# Função para calcular os horários
def calcular_horarios(AH7, valores_AD):
    print("Variavel de risco: ", RISCO)

    # Filtra valores_AD removendo valores None após o terceiro elemento e ordena a lista
    valores_AD = [valor for valor in valores_AD if valor is not None or valores_AD.index(valor) > 3]
    valores_AD.sort()

    # Converte o valor de AH7 para minutos
    minutos_AH7 = hora_para_minutos(AH7)

    # Conjunto para armazenar os resultados únicos
    resultados_unicos = set()

    # Loop para calcular e imprimir os horários até obter 12 resultados únicos
    while len(resultados_unicos) < 10:
        for valor_AD in valores_AD:
            novo_horario = minutos_AH7 + valor_AD  # Novo horário em minutos

            # Calcular o restante de minutos em horas completas
            dias_completos = novo_horario // (24 * 60)
            minutos_restantes = novo_horario % (24 * 60)

            # Calcular horas e minutos
            horas = minutos_restantes // 60
            minutos = minutos_restantes % 60

            # Formata o horário em "HH:MM"
            minutos = minutos - RISCO

            horas_str = str(horas).zfill(2)
            minutos_str = str(minutos).zfill(2)

            novo_horario_str = f"{horas_str}:{minutos_str}"

            # Adicionar o resultado ao conjunto de resultados únicos
            resultados_unicos.add(novo_horario_str)

            # Se alcançarmos 12 resultados únicos, sair do loop
            if len(resultados_unicos) == 10:
                break

    # Hora alvo fornecida
    target_hour = int(AH7.split(":")[0])

    # Filtra os resultados para incluir apenas os horários que começam com a hora alvo
    filtered_results = [result for result in sorted(resultados_unicos) if int(result.split(":")[0]) == target_hour]

    print("Fim da função calcular_horarios, ", filtered_results)

    return sorted(filtered_results)

