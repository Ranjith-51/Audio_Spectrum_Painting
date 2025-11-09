from flask import Flask, render_template, request, send_file
import numpy as np
from scipy.io import wavfile
import io

app = Flask(__name__)

def encode_image_in_audio(audio_data, image_data):
    img_bits = np.unpackbits(np.frombuffer(image_data, dtype=np.uint8))
    audio_flat = audio_data.flatten()
    audio_flat[:len(img_bits)] &= ~1
    audio_flat[:len(img_bits)] |= img_bits
    return audio_flat.reshape(audio_data.shape)

def decode_image_from_audio(audio_data, img_size):
    bits = audio_data.flatten() & 1
    img_bytes = np.packbits(bits[:img_size*8]).tobytes()
    return img_bytes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode():
    audio = request.files['audio']
    image = request.files['image']
    samplerate, data = wavfile.read(audio)
    image_bytes = image.read()
    stego_data = encode_image_in_audio(data, image_bytes)
    output = io.BytesIO()
    wavfile.write(output, samplerate, stego_data.astype(np.int16))
    output.seek(0)
    return send_file(output, as_attachment=True, download_name='stego_audio.wav', mimetype='audio/wav')

@app.route('/decode', methods=['POST'])
def decode():
    stego_audio = request.files['stego']
    samplerate, data = wavfile.read(stego_audio)
    decoded_bytes = decode_image_from_audio(data, 50000)
    return send_file(io.BytesIO(decoded_bytes), as_attachment=True, download_name='decoded_image.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
