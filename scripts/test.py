import cv2

img = cv2.imread("/home/erik/Pictures/normal_reflection.png", cv2.IMREAD_COLOR)



cv2.imshow("reflection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()