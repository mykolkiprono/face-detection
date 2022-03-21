import cv2 as cv 
import mediapipe as mp 
import time

cap = cv.VideoCapture(0)
ptime = 0

mpFaceDetection = mp.solutions.face_detection
mpdraw = mp.solutions.drawing_utils
face_detection = mpFaceDetection.FaceDetection()

while True:
	is_true, frame  = cap.read()

	image_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
	results = face_detection.process(image_rgb)
	# print(results)

	if results.detections:
		for id, detection in enumerate(results.detections):
			print(id, detection)
			mpdraw.draw_detection(frame, detection)

	ctime = time.time()
	fps = 1/(ctime-ptime)
	ptime = ctime

	cv.putText(frame, f"FPS: {int(fps)}", (10, 70), cv.FONT_HERSHEY_PLAIN,3,(0, 255, 0), 3)

	cv.imshow('frame', frame)

	if cv.waitKey(1) & 0xFF == ord('q'):
		break 