from networktables import NetworkTables
import time

# O IP do rádio do roboRIO 2 é = "10.91.63.2"

def ConnectionTest(ip_roborio):
    print(f"Conectando ao roboRIO ({ip_roborio})...")

    NetworkTables.initialize(server=ip_roborio)

    # Debug p/ ver se conectou ao roboRIO (costuma demorar até 7 segundos)
    for i in range(50):
        if NetworkTables.isConnected():
            print("✅ Conectado com sucesso ao NetworkTables!")
            break
        else:
            print("⏳ Tentando conectar...")
            time.sleep(1)
    else:
        print("❌ Não foi possível conectar ao NetworkTables.")

ConnectionTest("10.91.63.2")