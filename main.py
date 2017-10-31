
import sys
import numpy as np

from webcam import handleWebcamCapture
from utils import load_images
from control import verify_face, add_to_db

print "\n----------------------------------------------------------------------------"
print "\nFacial Recognition Using the PCA (Principal Component Analysis) Algorithm."
print "\nCreated by Jeet Kanjani https://jeetkanjani.wordpress.com/\n"
print "----------------------------------------------------------------------------"
print "\nProceed with login? Press Y/N to continue..."
print "\nIf instead you wish to enroll your face in the database, press 'N'\n"
while True :
  	sys.stdin.flush()
	inpt = raw_input("Y/N?")#sys.stdin.read(1)
	if(inpt == "y" or inpt == "Y") :
		print "\nPress 'Enter' to capture frame"
		print "Press 'ESC' at any time to exit\n"
		image = handleWebcamCapture(1)
		verify_face(image)
		break
	elif(inpt == "n" or inpt == "N") :
		print "\nThe first step is to train the software to recognize you by inputing images of your face into the database."
		print "We will take a total of 10 pictures to construct information about you.\n"
		print "\nPress 'Enter' to capture frame"
		print "Press 'ESC' at any time to exit\n"
		images = handleWebcamCapture(10)
		images = load_images(10)
		add_to_db(images)
		break
	else :
		print "Incorrect input. Please press Y/N to continue"
