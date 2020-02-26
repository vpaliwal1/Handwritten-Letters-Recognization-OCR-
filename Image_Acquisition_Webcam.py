import cv2

cv2.namedWindow("WebcamAcquisitionPreview")
vc = cv2.VideoCapture(0)

i = 0

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("WebcamAcquisitionPreview", frame)
    rval, frame = vc.read()
    #key = cv2.waitKey(20)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("c"):
        cv2.imwrite('img' + str(i)+ '.jpg', frame)
        img = cv2.imread('img' + str(i)+ '.jpg',0)
        print(img.shape)
        i += 1
    elif key == ord("q"):   # exit on q press
        break
    else:
        y = 0#Do nothing
cv2.destroyWindow("WebcamAcquisitionPreview")
