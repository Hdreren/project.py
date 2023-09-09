import cv2
import time

#Specify the path to the video frame
Video_Name = "File path"

#Open the video
cap = cv2.VideoCapture(Video_Name)

#Get video features
print("height:", int(cap.get(3))) #Video height
print("compatibility:", int(cap.get(1))) #Video compatibility

#give an error message if the video does not open
if not cap.isOpened():
    print("Hata: Video did not open")

while True:
    ret, frame = cap.read()

    if ret:
        #Show all frames
        cv2.imshow("Video", frame)

        #Terminate when "q" is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

#End video playback
cap.release()
cv2.destroyAllWindows()










