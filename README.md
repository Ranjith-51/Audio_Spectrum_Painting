# 🎨 Audio Spectrum Painting – LSB-Based Steganography System

## 📘 Overview
**Audio Spectrum Painting** is an innovative web-based system that hides image data within audio files using the **Least Significant Bit (LSB) steganography** technique.  
It aims to achieve **secure, imperceptible, and efficient multimedia data hiding**, allowing users to embed and extract images seamlessly through a simple, interactive **Flask web interface**.

---

## 🧠 Project Objectives
- To implement secure data embedding using the **LSB technique** in audio signals.  
- To ensure **no perceptible distortion** occurs in the stego-audio.  
- To provide both **encoding (embedding)** and **decoding (extraction)** functionalities.  
- To create a **user-friendly web application** using Flask and modern web technologies.  
- To explore the potential of **audio-based steganography** in real-world data security.

---

## ⚙️ System Modules
1. **User Interface Module** – Interactive web frontend built with HTML, CSS, and Flask templates.  
2. **Encoding Module** – Embeds image data into audio samples using the LSB method.  
3. **Decoding Module** – Extracts hidden image data from stego-audio.  
4. **Validation Module** – Ensures audio integrity and checks payload limits.  
5. **Security Module** – Preserves data confidentiality and prevents unauthorized access.

---

## 🧩 Technologies & Libraries Used
### **Languages**
- Python  
- HTML, CSS, JavaScript  

### **Framework**
- Flask  

### **Python Libraries**
- `wave` – For reading and writing `.wav` audio files  
- `numpy` – For bit-level manipulation and audio array handling  
- `Pillow (PIL)` – For image processing  
- `flask` – For web server and UI integration  
- `os`, `io`, `base64` – For file and data handling  

---

## 🧠 Theoretical Background
The **Least Significant Bit (LSB) technique** works by modifying the lowest bit in each audio sample to store hidden information.  
Since the human ear is not sensitive to these minor alterations, the hidden image remains imperceptible while maintaining audio quality.  
This approach makes it ideal for **covert communication** and **secure information transmission** in multimedia systems.

---

## 💡 Concept & Methodology
1. The system accepts a **.wav audio file** and an **image file (e.g., .png, .jpg)**.  
2. The image’s binary data is **split into bits** and embedded into the **least significant bits** of the audio samples.  
3. The modified (stego) audio is saved and made available for download.  
4. During decoding, the process is reversed to **reconstruct the original image** from the audio.  
5. Flask handles the backend logic and routes user interactions, while HTML templates provide a simple and clean interface.

---

## 🧱 System Architecture
- **Frontend:** User uploads files through a web page.  
- **Backend:** Flask receives files → Encodes/decodes using LSB algorithm → Returns results.  
- **Output:** Stego-audio or recovered image.

---

## 📊 Results and Discussion
The implementation demonstrates that large image data can be embedded into standard `.wav` audio without noticeable degradation in sound quality.  
Spectrogram analysis shows minimal waveform variation, validating the effectiveness of LSB-based embedding.  
Testing across multiple audio samples confirmed the system’s reliability, robustness, and fidelity.  
The decoding process successfully retrieves hidden images, proving the system’s efficiency for secure multimedia communication.

---

## 🌍 Real-Time Application
**Audio Spectrum Painting in IT Industries:**  
In IT and cybersecurity fields, this approach can be used for **covert communication**, **digital watermarking**, **confidential data exchange**, and **intellectual property protection**.  
It offers practical utility in sectors such as **defense communication**, **forensic data recovery**, and **multimedia authentication**.

---

## 🎯 Sustainable Development Goals (SDGs) Alignment
This project contributes to:
- **SDG 9:** Industry, Innovation, and Infrastructure  
- **SDG 16:** Peace, Justice, and Strong Institutions  
- **SDG 17:** Partnerships for the Goals  
By promoting **innovation in secure digital communication** and enhancing **data integrity** mechanisms.

---

## 🔮 Conclusion & Future Scope
The project establishes a secure, efficient, and imperceptible multimedia steganography system.  
Future enhancements could include:
- Supporting multiple audio formats (`.mp3`, `.flac`, etc.)  
- Adding **encryption layers** before embedding  
- Deploying the web app to **cloud platforms** (e.g., GitHub Pages or Render)  
- Incorporating **AI-driven adaptive encoding** for enhanced capacity and security.

---

## 🧾 References
1. Johnson, N. F., & Jajodia, S. (1998). Exploring steganography: Seeing the unseen. *IEEE Computer*.  
2. Katzenbeisser, S., & Petitcolas, F. A. (2000). *Information hiding techniques for steganography and digital watermarking*. Artech House.  
3. Provos, N., & Honeyman, P. (2003). Hide and seek: An introduction to steganography. *IEEE Security & Privacy*.  
4. Research articles on LSB audio steganography (IEEE, Springer, ScienceDirect).  

---

## 👩‍💻 Contributors
- **Project Developer :** R.Ranjith Kumar
- **Project Advisor :** Pradosh Gopalakrishnan
- **Project Co-Advisor :** Rogan Prabhu

---

© 2025 Audio Spectrum Painting | Developed for Academic and Research Purposes
