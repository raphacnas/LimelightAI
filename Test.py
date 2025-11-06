from networktables import NetworkTables
import time

NetworkTables.initialize(server="10.91.63.2")
vision = NetworkTables.getTable("limelight-front")

while not NetworkTables.isConnected():
    print("Tentando conectar...")
    time.sleep(0.5)

print("✅ Conectado")

# Lê continuamente o que há na NetworkTable
while True:
    keys = vision.getKeys()
    print("🔍 Chaves na tabela:", keys)
    for k in keys:
        print(f"  {k}: {vision.getValue(k, 0)}")
    time.sleep(1)

