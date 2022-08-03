import cv2

#########################################F#########################################################

objectName= "pakai masker"
objectName2= "tanpa masker"
objectName3= "lengkap"
objectName4= "tidak lengkap"

color= (0,255,0)
color2= (0,0,255)
###################################################################################################

# LOAD THE CLASSIFIER
cascade = cv2.CascadeClassifier('C:/Users/Dwipa Yogi/Documents/PROJECT 21/Haarcascade/Masker cascade/classifier3/cascade.xml')
cascade2 = cv2.CascadeClassifier('C:/Users/Dwipa Yogi/Documents/PROJECT 21/Haarcascade/Tanpa Masker/classifier/cascade.xml')
cascade3 = cv2.CascadeClassifier('C:/Users/Dwipa Yogi/Documents/PROJECT 21/Haarcascade/Lengkap cascade/classifier2/cascade.xml')
cascade4 = cv2.CascadeClassifier('C:/Users/Dwipa Yogi/Documents/PROJECT 21/Haarcascade/Tidak Lengkap/classifier/cascade.xml')


path = 'C:/Users/Dwipa Yogi/Documents/PROJECT 21/images/1 (5).jpg'
img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


objects = cascade.detectMultiScale(
    gray,
    scaleFactor = 1.10,
    minNeighbors = 6
)
for x, y, w, h in objects:
    img = cv2.rectangle(
        img,            # image object
        (x,y),          # posisi kotak
        (x+w, y+h),     # posisi kotak
        (0, 255, 0),    # warna kotak RGB
        2               # lebar garis kotak
    )
    cv2.putText(img,objectName,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,1)
    roi_color = img[y:y+h, x:x+w]

objects2 = cascade2.detectMultiScale(
    gray,
    scaleFactor = 1.10,
    minNeighbors = 6
)
for x, y, w, h in objects2:
    img = cv2.rectangle(
        img,            # image object
        (x,y),          # posisi kotak
        (x+w, y+h),     # posisi kotak
        (0, 0, 255),    # warna kotak RGB
        2               # lebar garis kotak
    )
    cv2.putText(img,objectName2,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color2,1)
    roi_color = img[y:y+h, x:x+w]

objects3 = cascade3.detectMultiScale(
    gray,
    scaleFactor = 1.10,
    minNeighbors = 6
)
for x, y, w, h in objects3:
    img = cv2.rectangle(
        img,            # image object
        (x,y),          # posisi kotak
        (x+w, y+h),     # posisi kotak
        (0, 255, 0),    # warna kotak RGB
        3               # lebar garis kotak
    )
    cv2.putText(img,objectName3,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,1)
    roi_color = img[y:y+h, x:x+w]

objects4 = cascade4.detectMultiScale(
    gray,
    scaleFactor = 1.10,
    minNeighbors = 6
)
for x, y, w, h in objects4:
    img = cv2.rectangle(
        img,            # image object
        (x,y),          # posisi kotak
        (x+w, y+h),     # posisi kotak
        (0, 0, 255),    # warna kotak RGB
        3               # lebar garis kotak
    )
    cv2.putText(img,objectName4,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color2,1)
    roi_color = img[y:y+h, x:x+w]

resized = cv2.resize(img, (800,600))
cv2.imshow('Output', resized)
cv2.imwrite('C:/Users/Dwipa Yogi/Documents/PROJECT 21/Output/test1.jpg', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()