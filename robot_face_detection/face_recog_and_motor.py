import io
import picamera
import cv2
import numpy
import pyfirmata
from time import sleep
import math



board = pyfirmata.Arduino('/dev/ttyACM0')
servo = board.get_pin('d:8:s')

DELAY = 1
MIN = 5
MAX = 175
MID = 90

def move_servo(v):
    servo.write(v)
    board.pass_time(DELAY)

    
#Create a memory stream so photos doesn't need to be saved in a file
stream = io.BytesIO()

#Get the picture (low resolution, so it should be quite fast)
#Here you can also specify other parameters (e.g.:rotate the image)
with picamera.PiCamera() as camera:
    camera.resolution = (1920, 1080)
    camera.capture(stream, format='jpeg')

#Convert the picture into a numpy array
buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)

#Now creates an OpenCV image
image = cv2.imdecode(buff, 1)

#Load a cascade file for detecting faces
face_cascade = cv2.CascadeClassifier('/home/pi/Desktop/robot_face_detection/faces.xml')

#Convert to grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#Look for faces in the image using the loaded cascade file
faces = face_cascade.detectMultiScale(gray, 1.1, 5)

print("Found "+str(len(faces))+" face(s)")

#Move servo accordingly if there is a face or not and print the angular position
if len(faces) != 0:
    move_servo(MID)
else:
    move_servo(MIN)

print("Servo position (deg): {}".format(servo.read()))
    
#Draw a rectangle around every found face
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)

#Save the result image
cv2.imwrite('result.jpg',image)

board.exit()

