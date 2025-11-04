import cv2

LIMELIGHT_IP = "10.91.63.30:5800"
STREAM_URL = f"http://{LIMELIGHT_IP}"

cap = cv2.VideoCapture(STREAM_URL)

# ---------- configuração da janela ----------
cv2.namedWindow("Limelight Stream", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Limelight Stream", 640, 480)
cv2.setWindowProperty("Limelight Stream", cv2.WND_PROP_TOPMOST, 1)
# --------------------------------------------

while True:
    ret, frame = cap.read()
    if not ret:
        print("Sem vídeo da Limelight")
        break

    cv2.imshow("Limelight Stream", frame)
    if cv2.waitKey(50) == 27:          # 50 ms → ~20 fps
        break

cap.release()
cv2.destroyAllWindows()