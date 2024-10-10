import subprocess
import time

while True:
    try:
        subprocess.run(["python3", "/caminho/completo/para/seu/api.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar api.py: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    
    time.sleep(60)  # Espera 60 segundos (1 minuto) antes da próxima execução