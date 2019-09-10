# import numpy as np
import cv2

# img = cv2.imread('media/abba.png')
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# cv2.namedWindow('some other name', cv2.WINDOW_NORMAL)
# cv2.waitKey(0)
# cv2.imwrite('one_at_once.png', img)


img = cv2.imread('media/abba.jpg', 0)
cv2.imshow('wfw', img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):  # wait for 's' key to save and exit
    cv2.imwrite('new.png', img)
    cv2.destroyAllWindows()
