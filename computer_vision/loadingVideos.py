import cv2

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    # print(frame)
    cv2.imshow("reading webcam", frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
