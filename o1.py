import cv2
img=cv2.imread("lena15.jpg",0)
cv2.imshow("lena",img)
k=cv2.waitKey(0) 
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite("copy.png",img)
    cv2.destroyAllWindows()