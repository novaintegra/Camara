import cv2

# Capturar video desde la cámara web (0 indica la primera cámara)
cap = cv2.VideoCapture(0)

# Definir el codec y crear un VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('salida.mp4', fourcc, 20.0, (640, 480))

while(True):
    # Capturar un frame
    ret, frame = cap.read()

    # Escribir el frame en el video de salida
  #  out.write(frame)

    # Mostrar el frame en una ventana
    cv2.imshow('Camara Frontal',frame)

    # Si se presiona la tecla 'q', se detiene la captura
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos
cap.release()
out.release()
cv2.destroyAllWindows()