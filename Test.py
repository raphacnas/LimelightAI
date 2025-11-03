import cv2

LIMELIGHT_IP = "10.91.63.30:5801"  # IP da sua Limelight
STREAM_URL = f"http://{LIMELIGHT_IP}"  # ou 5801, dependendo do modo

cap = cv2.VideoCapture(STREAM_URL)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Sem vídeo da Limelight")
        break

    cv2.imshow("Limelight Stream", frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()