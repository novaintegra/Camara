import cv2
import numpy as np
import deepface.DeepFace

# Reemplaza 'http://tu_camara_ip/video' con la URL de tu cámara
cap = cv2.VideoCapture(0)

while(True):
    # Capturamos un frame
    ret, frame = cap.read()

    # Convertimos el frame a escala de grises (opcional)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    #try:
    # Detectar rostros
    
    faces = deepface.DeepFace.extract_faces(gray)

    # Para cada rostro, obtener atributos
    for face in faces:
   
        # Análisis de edad, género y emoción
        
          
            coordenadas = face['facial_area']
            print(coordenadas)
        

            cv2.rectangle(gray, (coordenadas['x'], coordenadas['y']), (coordenadas['x'] + coordenadas['w'], coordenadas['y'] + coordenadas['h']), (0, 255, 0), 2)

            analysis = deepface.DeepFace.analyze(gray, actions=['age', 'gender', 'emotion'], enforce_detection=False)

       

            font_size = 0.5
            cv2.putText(gray, 'Género: '+analysis[0].get("dominant_gender"),
                        (coordenadas['x'], coordenadas['y'] + coordenadas['h']-30),cv2.FONT_HERSHEY_SIMPLEX,
                        font_size,
                        (255,255,0),
                        2,3)    
            cv2.putText(gray, 'Animo: ' + analysis[0].get("dominant_emotion"),
                        (coordenadas['x'], coordenadas['y'] + coordenadas['h']-15),cv2.FONT_HERSHEY_SIMPLEX,
                        font_size,
                        (255,255,0),
                        2,3)  
        
            cv2.putText(gray, 'Raza: ' + str(analysis[0].get("dominant_race")),
                        (coordenadas['x'] + 80, coordenadas['y'] + coordenadas['h']),cv2.FONT_HERSHEY_SIMPLEX,
                        font_size,
                        (255,255,0),
                        2,3)  
        
            cv2.putText(gray, 'Edad: ' + str(analysis[0].get("age")),
                        (coordenadas['x'], coordenadas['y'] + coordenadas['h']),cv2.FONT_HERSHEY_SIMPLEX,
                        font_size,
                        (255,255,0),
                        2,3)   

   #except Exception as e:
   #    print("Error al analizar la imagen:", e, )


    # Mostramos el frame
    cv2.imshow('Camara ip',frame)

    # Si se presiona la tecla 'q', salimos
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cuando todo haya terminado, liberamos la captura
cap.release()
cv2.destroyAllWindows()