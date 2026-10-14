# Dia 03 - Recon

**Data:** 14/10/2026
**Alvo:** 192.168.56.10
**Maquina:** Linux-Target-Server (Ubuntu)

## Conectividade
- ping 192.168.56.10 -> OK (0.5ms avg, 0% loss)

## Nmap
- Comando: nmap -sV -p 22 192.168.56.10
- Resultado: 
    - PORT 22/tcp open
    - SERVICE ssh OpenSSH 10.2p1 Ubuntu 2ubuntu3.6
    - OS: Linux

## Proximo passo
- Testar brute-force SSH com dicionario do Dia 02