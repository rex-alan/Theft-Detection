import cv2

cam = cv2.VideoCapture(0)
cv2.namedWindow("test")
img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        print('Image' + str(img_counter) + 'saved')
        file = "Your photo directory's location"
        cv2.imwrite(file, frame)
        img_counter += 1

cam.release()
cv2.destroyAllWindows()
