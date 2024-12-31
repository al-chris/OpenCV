import numpy as np
import cv2

# img = cv2.imread('assets/test.png', 0)
# img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
# img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# cv2.imwrite('assets/test_resized.png', img)

# cv2.imshow("Test", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# print(img.shape)

cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     width = int(cap.get(3))
#     height = int(cap.get(4))

#     image = np.zeros(frame.shape, np.uint8)
#     smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
#     image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
#     image[height//2:, :width//2] = smaller_frame
#     image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
#     image[height//2:, width//2:] = smaller_frame

#     cv2.imshow("Video", image)

#     if cv2.waitKey(1) == ord('q'):
#         break


while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)

    cv2.imshow("Video", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()