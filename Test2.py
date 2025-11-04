from networktables import NetworkTables

# Código para enviar as variáveis para o RoboRio
NetworkTables.initialize(server="10.91.63.2")
table = NetworkTables.getTable("vision")