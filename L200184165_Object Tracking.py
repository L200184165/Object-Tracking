import cv2

#To Use video, just change inside the () below with the name of the file and the format. Example : ("vid.mp4")
#To use webcam, fill inside the () with 0, Example : (0)
cap = cv2.VideoCapture(0)


tracker = cv2.TrackerKCF_create()
success, img = cap.read()               
bbox = cv2.selectROI("Tracking",img,False)
tracker.init(img,bbox)

def drawBox(img, bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)
    cv2.putText(img, "Tracking", (5, 50), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0))


while True:
    timer = cv2.getTickCount()
    success, img = cap.read()

    success, bbox = tracker.update(img)

    if success:
        drawBox(img,bbox)
    else:
        cv2.putText(img,"Lost",(5,50),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,255))


    fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    cv2.putText(img,str(int(fps)),(5,25),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0))
    cv2.imshow("Tracking",img)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
