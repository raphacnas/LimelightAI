from networktables import NetworkTables
import time

NetworkTables.initialize(server='10.91.63.2')
vision = NetworkTables.getTable("vision")

while not NetworkTables.isConnected():
    print("Tentando conectar...")
    time.sleep(0.5)
print("✅ Conectado")

vision.putNumber("distancia", 1.23)
vision.putBoolean("alvo_detectado", True)

print("📡 Valor enviado.")
print("🔍 Valor lido de volta:", vision.getNumber("distancia", 0), "|", vision.getBoolean("alvo_detectado", False))
