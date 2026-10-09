# DIA 2 - Como quebrei meu próprio SSH e me peguei no log

## RESUMÃO PRA BURRO (com analogia)

Pensa no SSH como a porta do seu quarto trancada.
O usuário `lab` com senha `toor123` é você deixando a chave embaixo do tapete.
Meu script `ssh-tester.py` foi o ladrão testando 5 chaves que todo mundo usa (123456, admin, toor123).

O `journalctl` é a câmera da portaria. Toda vez que alguém tenta a porta, ela grava:
- `Failed password` = tentou a chave e errou
- `Accepted password` = acertou e entrou

No meu print tem 14 falhas e 4 acertos. Foi eu mesmo me atacando em 127.0.0.1 (meu próprio PC).

Depois eu fui o segurança: apaguei o usuário fraco `lab` e criei o `devops` com senha forte. Na vida real a empresa faz isso + desativa login por senha e usa chave SSH.

## FERRAMENTAS DO KALI QUE USEI

- `sudo service ssh start` - liga o servidor SSH (a porta)
- `sudo adduser lab` / `sudo deluser lab` - cria e apaga usuário alvo
- `python3-paramiko` - biblioteca Python que fala SSH
- `sudo journalctl -u ssh --no-pager | grep "Failed password"` - vê quem tentou e errou
- `sudo journalctl -u ssh --no-pager | grep "Accepted"` - vê quem conseguiu entrar
- `sudo journalctl -u ssh --no-pager | grep -E "Failed|Accepted"` - vê os dois juntos

## COMO USAR ESSE CÓDIGO DE NOVO

Se você esquecer, é só abrir o `ssh-tester.py`, o passo a passo tá dentro do arquivo.

1. Ligar servidor: `sudo service ssh start`
2. Criar alvo fraco: `sudo adduser lab` (senha toor123)
3. Instalar lib: `sudo apt install python3-paramiko -y`
4. Rodar ataque: `python3 ssh-tester.py`
5. Se detectar: `sudo journalctl -u ssh --no-pager | grep -E "Failed|Accepted" | tail -n 20`
6. Defender: `sudo deluser lab --remove-home && sudo adduser devops`

## PRINT DA PROVA

O log mostrou:
- 14x Failed password for lab from 127.0.0.1
- 4x Accepted password for lab from 127.0.0.1

Ataque e defesa feitos em localhost, 100% educacional.
