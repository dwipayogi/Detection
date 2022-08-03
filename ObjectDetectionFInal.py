import cv2

#########################################F#########################################################
path = 'C:/Users/Dwipa Yogi/Documents/PROJECT 21/Haarcascade/Masker/classifier/cascade.xml'
objectName= "pakai masker"
color= (0,255,0)

path2 = 'C:/Users/Dwipa Yogi/Documents/PROJECT 21/Haarcascade/Tanpa Masker/classifier/cascade.xml'
objectName2= "tanpa masker"
color2= (0,0,255)

path3 = 'C:/Users/Dwipa Yogi/Documents/PROJECT 21/Haarcascade/Lengkap cascade/classifier2/cascade.xml'
objectName3= "lengkap"
color3= (0,255,0)

path4 = 'C:/Users/Dwipa Yogi/Documents/PROJECT 21/Haarcascade/Tidak Lengkap/classifier/cascade.xml'
objectName4= "tidak lengkap"
color4= (0,0,255)

###################################################################################################
cameraNo = 0
frameWidth = 1200
frameHeight = 1000
###################################################################################################
cam = cv2.VideoCapture(cameraNo)
cam.set(3, frameWidth)
cam.set(4, frameHeight)

def empty(a):
    pass

#CREATE WINDOW
cv2.namedWindow("Detection")

#CREATE TRACKBAR
cv2.namedWindow("Settings for mask")
cv2.createTrackbar("Brightness","Settings for mask",100,255,empty)
cv2.createTrackbar ("Scale","Settings for mask",200,1000,empty)
cv2.createTrackbar("Neig","Settings for mask",8,20,empty)
cv2.createTrackbar("Min Area","Settings for mask",0,40000,empty)

#CREATE TRACKBAR
cv2.namedWindow("Settings for uniform")
cv2.createTrackbar ("Scale","Settings for uniform",200,1000,empty)
cv2.createTrackbar("Neig","Settings for uniform",8,20,empty)
cv2.createTrackbar("Min Area","Settings for uniform",0,100000,empty)


# LOAD THE CLASSIFIER
cascade = cv2.CascadeClassifier(path)
cascade2 = cv2.CascadeClassifier(path2)
cascade3 = cv2.CascadeClassifier(path3)
cascade4 = cv2.CascadeClassifier(path4)

while True:
    cameraBrightness = cv2.getTrackbarPos("Brightness","Settings for mask")
    cam.set(10, cameraBrightness)

    success, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    scaleVal =1 + (cv2.getTrackbarPos("Scale", "Settings for mask") /1000)
    neig= cv2.getTrackbarPos("Neig", "Settings for mask")
    objects = cascade.detectMultiScale(gray,scaleVal, neig) #Masker
    
    for (x,y,w,h) in objects:
        area = w*h
        minArea = cv2.getTrackbarPos("Min Area", "Settings for mask")
        if area >minArea:
            cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
            cv2.putText(img,objectName,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,1)
            roi_color = img[y:y+h, x:x+w]


    objects2 = cascade2.detectMultiScale(gray,scaleVal, neig) #Tanpa Masker
    for (x,y,w,h) in objects2:
        area = w*h
        minArea2 = cv2.getTrackbarPos("Min Area", "Settings for mask")
        if area >minArea2:
            cv2.rectangle(img,(x,y),(x+w,y+h),color2,2)
            cv2.putText(img,objectName2,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color2,1)
            roi_color = img[y:y+h, x:x+w]

    scaleVal2 = 1 + (cv2.getTrackbarPos("Scale", "Settings for uniform") / 1000)
    neig2 = cv2.getTrackbarPos("Neig", "Settings for uniform")
    objects3 = cascade3.detectMultiScale(gray,scaleVal2, neig2) #Lengkap
    for (x,y,w,h) in objects3:
        area = w*h
        minArea3 = cv2.getTrackbarPos("Min Area", "Settings for uniform")
        if area >minArea3:
            cv2.rectangle(img,(x,y),(x+w,y+h),color3,3)
            cv2.putText(img,objectName3,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color3,1)
            roi_color = img[y:y+h, x:x+w]

    scaleVal2 = 1 + (cv2.getTrackbarPos("Scale", "Settings for uniform") / 1000)
    neig2 = cv2.getTrackbarPos("Neig", "Settings for uniform")
    objects4 = cascade4.detectMultiScale(gray,scaleVal2, neig2) #Tidak Lengkap
    for (x,y,w,h) in objects4:
        area = w*h
        minArea3 = cv2.getTrackbarPos("Min Area", "Settings for uniform")
        if area >minArea3:
            cv2.rectangle(img,(x,y),(x+w,y+h),color4,3)
            cv2.putText(img,objectName4,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color4,1)
            roi_color = img[y:y+h, x:x+w]


    cv2.imshow("Detection",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break