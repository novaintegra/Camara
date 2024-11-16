import cv2
import deepface
import deepface.DeepFace    

capture = cv2.VideoCapture(0)

face_model = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while(True):
    _, frame = capture.read()
    face = face_model.detectMultiScale(cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY), scaleFactor=1.1, minNeighbors= 50,  flags=cv2.CASCADE_SCALE_IMAGE)
     
    for x, y, width, height in face:
        emotion = deepface.DeepFace.analyze(frame, actions=['emotion','gender','age'])
       
        font_size = 0.5
        cv2.putText(frame, 'Genero: ' +emotion[0].get("dominant_gender"),
                        (x, y + height-40),cv2.FONT_HERSHEY_SIMPLEX,
                        font_size,
                        (255,255,0),
                        2,3)    
        cv2.putText(frame, 'Edad: ' + str(emotion[0].get("age")),
                        (x, y + height-20),cv2.FONT_HERSHEY_SIMPLEX,
                        font_size,
                        (255,255,0),
                        2,3)  
        cv2.putText(frame, 'Animo: ' + emotion[0].get("dominant_emotion"),
                        (x, y + height-5),cv2.FONT_HERSHEY_SIMPLEX,
                        font_size,
                        (255,255,0),
                        2,3)  
               
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)

    cv2.imshow('Video de emociones',frame)

   # Si se presiona la tecla 'q', salimos
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cuando todo haya terminado, liberamos la captura
capture.release()
cv2.destroyAllWindows()
