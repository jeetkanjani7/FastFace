import cv2
from PIL import Image

# callback to display image in window instance
def repeat(capture) :
    frame = capture.read()
    #cv2.imshow('Face Capture', frame)

# retrieves n-many webcam images
#
# @param n <int> - number of images to capture
# @return pil_images <array of PIL.Image> - n-many webcam captured images
def handleWebcamCapture(n) :
    print("handleWebcam")
    cv2.namedWindow('Face Capture',cv2.WINDOW_NORMAL)
    camera_index = 0
    capture = cv2.VideoCapture(camera_index)
    pil_images = []
    while True:
        repeat(capture)
        if (cv2.waitKey(10) == 27) :
            print 'ESC pressed. Exiting ...'
            cv2.DestroyAllWindows()
            break
        if (cv2.waitKey(10) == 13) :
            image = capture.read()
            pil_images.append(Image.fromstring("RGB",cv2.GetSize(image),image.tostring(),'raw','BGR',image.width*3,0))
            print 'Image captured.'
            if len(pil_images) > n - 1 :
                cv2.DestroyAllWindows()
                return pil_images
            else : 
                print('else')
                continue
             