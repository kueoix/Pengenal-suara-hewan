import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')


def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 10)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return frame

video_capture = cv2.VideoCapture("koceng.mp4")
while True:
    kocng,frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
video_capture.release()