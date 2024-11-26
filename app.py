from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import tensorflow as tf
import numpy as np
import uvicorn

# Inisialisasi aplikasi FastAPI
app = FastAPI()

# Memuat model ML
MODEL_PATH = "MLfix.h5"
try:
    model = tf.keras.models.load_model(MODEL_PATH)
    print("Model loaded successfully")
except Exception as e:
    raise Exception(f"Error loading ML model: {e}")

# Daftar nama karir yang sesuai dengan output model
CAREERS = [
    "Animator", "Dokter Gigi", "Apoteker", "Perawat", "Teknisi Otomasi",
    "Pengembang Perangkat Lunak", "Insinyur Sipil", "Matematikawan", "Ahli Kimia",
    "Fisikawan", "Ilmu Geologi", "Manajer Pariwisata", "Pakar Teknologi Informasi",
    "Spesialis Komputer", "Arsitek", "Sejarawan", "Seniman", "Pengusaha",
    "Desainer Mode", "Jurnalis", "Pengacara", "Manajer Acara", "Administrator Bisnis",
    "Insinyur Elektronika dan Komunikasi", "Insinyur Mekanikal", "Profesional Perdagangan",
    "Ekonom", "Akuntan Publik Bersertifikat", "Sekretaris Perusahaan",
    "Aktor/Sutradara", "Dokter Medis", "Pegawai Negeri Sipil (PNS)", 
    "Spesialis Bahasa Inggris", "Spesialis Bahasa Indonesia", "Pendidik/Guru"
]

# Schema untuk input prediksi
class PredictionInput(BaseModel):
    Menggambar: float
    Menari: float
    Bernyanyi: float
    Olahraga: float
    Permainan_Video: float
    Berakting: float
    Bepergian: float
    Berkebun: float
    Hewan: float
    Fotografi: float
    Mengajar: float
    Olahraga_Fisik: float
    Pemrograman: float
    Komponen_Listrik: float
    Komponen_Mekanik: float
    Komponen_Komputer: float
    Meneliti: float
    Arsitektur: float
    Koleksi_Sejarah: float
    Botani: float
    Zoologi: float
    Fisika: float
    Akuntansi: float
    Ekonomi: float
    Sosiologi: float
    Geografi: float
    Psikologi: float
    Sejarah: float
    Ilmu_Pengetahuan: float
    Pendidikan_Bisnis: float
    Kimia: float
    Matematika: float
    Biologi: float
    Make_Up: float
    Mendesign: float
    Penulisan_Konten: float
    Kerajinan: float
    Sastra: float
    Membaca: float
    Membuat_Kartun: float
    Berdebat: float
    Astrologi: float
    Bahasa_Indonesia: float
    Bahasa_Inggris: float
    Bahasa_Lain: float
    Memecahkan_Teka_teki: float
    Senam: float
    Yoga: float
    Teknik: float
    Dokter: float
    Apoteker: float
    Bersepeda: float
    Merajut: float
    Sutradara: float
    Jurnalisme: float
    Bisnis: float
    Mendengarkan_Musik: float

# Endpoint untuk prediksi menggunakan model ML
@app.post("/predict/")
def predict(input_data: PredictionInput):
    try:
        # Membentuk array input berdasarkan urutan fitur
        input_array = np.array([[getattr(input_data, field) for field in input_data.__fields__]])
        print("Input array shape:", input_array.shape)  # Debugging input array shape
        
        # Melakukan prediksi
        prediction = model.predict(input_array)
        print("Prediction result:", prediction)  # Debugging hasil prediksi

        # Mengambil indeks hasil prediksi tertinggi
        predicted_index = np.argmax(prediction[0])
        predicted_career = CAREERS[predicted_index]
        return {"predicted_career": predicted_career}
    except Exception as e:
        print("Error during prediction:", str(e))  # Debugging error
        raise HTTPException(status_code=500, detail=f"Error during prediction: {e}")
