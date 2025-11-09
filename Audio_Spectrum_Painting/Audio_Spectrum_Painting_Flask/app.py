from flask import Flask, render_template, request, send_file, redirect, url_for
import wave
import numpy as np
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def encode_image_in_audio(audio_path, image_path, output_path):
    audio = wave.open(audio_path, mode='rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    params = audio.getparams()
    audio.close()

    with open(image_path, 'rb') as img:
        image_data = img.read()

    image_data += b'###'
    bits = list(map(int, ''.join([bin(byte)[2:].rjust(8, '0') for byte in image_data])))

    for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit

    encoded_audio = wave.open(output_path, 'wb')
    encoded_audio.setparams(params)
    encoded_audio.writeframes(frame_bytes)
    encoded_audio.close()

def decode_image_from_audio(audio_path, output_image_path):
    audio = wave.open(audio_path, mode='rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    audio.close()

    extracted_bits = [str(frame_bytes[i] & 1) for i in range(len(frame_bytes))]
    extracted_bytes = [extracted_bits[i:i+8] for i in range(0, len(extracted_bits), 8)]
    extracted_data = bytearray([int(''.join(byte), 2) for byte in extracted_bytes])

    delimiter = extracted_data.find(b'###')
    if delimiter != -1:
        image_data = extracted_data[:delimiter]
        with open(output_image_path, 'wb') as img_file:
            img_file.write(image_data)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode():
    audio_file = request.files['audio']
    image_file = request.files['image']
    if audio_file and image_file:
        audio_path = os.path.join(UPLOAD_FOLDER, 'input_audio.wav')
        image_path = os.path.join(UPLOAD_FOLDER, 'input_image.png')
        output_audio_path = os.path.join(UPLOAD_FOLDER, 'encoded_audio.wav')

        audio_file.save(audio_path)
        image_file.save(image_path)
        encode_image_in_audio(audio_path, image_path, output_audio_path)
        return send_file(output_audio_path, as_attachment=True)
    return redirect(url_for('index'))

@app.route('/decode', methods=['POST'])
def decode():
    audio_file = request.files['audio']
    if audio_file:
        audio_path = os.path.join(UPLOAD_FOLDER, 'encoded_audio.wav')
        output_image_path = os.path.join(UPLOAD_FOLDER, 'decoded_image.png')
        audio_file.save(audio_path)
        decode_image_from_audio(audio_path, output_image_path)
        return send_file(output_image_path, as_attachment=True)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
