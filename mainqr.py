import streamlit as st
import cv2
from pyzbar.pyzbar import decode
from PIL import Image
import json
import numpy as np 

# Función para decodificar el QR
def decode_qr(frame):
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    qr_code = decode(gray_img)
    if qr_code:
        return qr_code[0].data.decode('utf-8')
    return ""

def main():
    st.title("QR Code Scanner")

    # Cámara para capturar video
    video = st.camera_input("Scan your QR code")

    # Botón de configuración para mostrar la información en JSON
    if video is not None:
        # Convertir la imagen de la cámara a un formato que OpenCV pueda procesar
        img = Image.open(video)
        frame = np.array(img)

        # Decodificar QR
        qr_info = decode_qr(frame)
        st.text_area("QR Code Information", value=qr_info, height=150)

        if st.button("Show JSON"):
            if qr_info:
                st.json(json.dumps({"qr_data": qr_info}))
            else:
                st.write("No QR code detected.")

if __name__ == "__main__":
    main()
