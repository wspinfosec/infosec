import socket


host = "192.168.56.10"
doors = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 3306, 5432, 8080]

for i in doors:
  
    s=socket.socket()
    s.settimeout(1)

    try:
        s.connect ((host, i))
        print(f"Door {i} is open")
        s.close()
    except:
        print(f"Door {i} is closed")
