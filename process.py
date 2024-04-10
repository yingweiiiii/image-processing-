import cv2

def dark(src):
    src = cv2.imread("photo.jpg")
    dstx = cv2.Sobel(src,cv2.CV_32F,1,0)
    dsty = cv2.Sobel(src,cv2.CV_32F,0,1)
    dstx = cv2.convertScaleAbs(dstx)
    dsty = cv2.convertScaleAbs(dsty)
    dst = cv2.addWeighted(dstx,0.5,dsty,0.5,0)
    cv2.imshow("Src",src)
    #cv2.imshow("Dstx",dstx)
    #cv2.imshow("Dsty",dsty)
    cv2.imshow("Dst",dst)
    cv2.imwrite("result.jpg",dst)


cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

if not cap.isOpened():
    print("Cannot open camara")
    exit()
    
while True:
    ret,frame = cap.read()
    
    if not ret:
        print("Can't receive frame(stream end?).EXiting...")
        break
    cv2.imshow("frame",frame)
    cv2.imwrite("photo.jpg",frame)
    dark("webcam.jpg")
    
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
