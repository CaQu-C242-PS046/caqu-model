# Menggunakan image Python sebagai dasar
FROM python:3.11

# Menentukan direktori kerja di dalam container
WORKDIR /app

# Menyalin file requirements.txt ke dalam container
COPY requirements.txt .

# Menginstal dependensi
RUN pip install --no-cache-dir -r requirements.txt

# Menyalin semua file kode ke dalam container
COPY . .

# Menentukan port yang akan diekspos
EXPOSE 8000

# Perintah untuk menjalankan aplikasi FastAPI menggunakan Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
