import cv2
import time

#Iniciando comunicação com a camera
url = "rtsp://CameraRua:122328aA@192.168.15.114:554/live/ch0"
cap = cv2.VideoCapture(url)

# Definições de Gravação (6 FPS para economizar HD)
fps_gravacao = 6

# Resolução das lentes
res_lente = (3072, 1024)
fourcc = cv2.VideoWriter_fourcc(*'XVID') # Codec leve para o PC

# criando o arquivo para cada uma das lentes
out_fixa  = cv2.VideoWriter('lente_fixa.avi',  fourcc, fps_gravacao, res_lente)
out_movel = cv2.VideoWriter('lente_movel.avi', fourcc, fps_gravacao, res_lente)

contador_frames = 0

# Definindo tamanho da janela que vai ser aberta no PC
display_width  = 800
display_height = 400

validade, frame_gigante = cap.read()

while validade:
    validade, frame_gigante = cap.read()

    # Gira horizontal e verticalmente
    frame_gigante = cv2.flip(frame_gigante, -1)
    lente_superior_full = frame_gigante[0:1024, :]  # corte da camera fixa (corte na vertical)
    lente_inferior_full = frame_gigante[1300:,  :]  # corte da camera 360 (corte na vertical)

    # --- Redimensionar APENAS para Exibir no Monitor ---
    lente_Superior_small = cv2.resize(lente_superior_full, (display_width, display_height))
    lente_Inferior_small = cv2.resize(lente_inferior_full, (display_width, display_height))

    # --- Exibir as janelas ---
    cv2.imshow("Lente Movel", lente_Superior_small)
    cv2.imshow("Lente Fixa ", lente_Inferior_small)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC para sair
        break

cap.release()
cv2.destroyAllWindows()




#OBSERVAÇÕES
# Dimensões Totais da Câmera: 3072x2048 (ONVIF Device Manager)
# Ponto de corte é no meio: 1024 de altura.