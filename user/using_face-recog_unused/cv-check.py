from cv2 import cv2

img = cv2.VideoCapture(0)

while(True):
    _,cam = img.read()
    cv2.imshow('frame', cam)
    
    if cv2.waitKey(1) & 0xFF == ord(' '):
        cv2.imwrite('uploads/unknown_faces/cv2_image_person3.jpg', cam)
        break

img.release()
cv2.destroyAllWindows()

 


