from ultralytics import YOLO

# Código para rodar a IA
model = YOLO("best.pt")
limelight_url = "http://10.91.63.30:5800"
model.predict(source=limelight_url, show=True)


