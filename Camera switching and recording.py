import cv2

#Capture
cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width, height)

#Video Recording
writer = cv2.VideoWriter("Video_recording", cv2.VideoWriter_fourcc(*"DIVX"),20,(width, height))

while True:
    ret, frame = cap.read()
    cv2.imshow("video", frame)

    #save
    writer.write(frame)

    if cv2.waitKey(1) & 0xFF == ord("s"):
        break


cv2.waitKey()
cap.release()
writer.release()
cv2.destroyAllWindow()

























