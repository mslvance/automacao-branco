import requests

TOKEN = '7275443105:AAFLlQtY52_qxtvZCIA6B13lh3SLZXy8JSs'
CHAT_ID = '-2207574453'
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

def enviar_para_telegram(horarios):
    print("Dentro da função de envio dos sinais")

    # Adicionar "Entradas:" antes dos horários
    mensagem = "Entradas:\n" + "\n".join(horarios)

    payload = {
        'chat_id': CHAT_ID,
        'text': mensagem
    }

    response = requests.post(URL, data=payload)
    if response.status_code != 200:
        print(f"Falha ao enviar mensagem: {response.status_code}")
    else:
        print("Mensagem enviada com sucesso.")

