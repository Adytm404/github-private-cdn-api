# Private CDN dengan Flask dan GitHub

Sebuah aplikasi web Flask sederhana yang berfungsi sebagai *Content Delivery Network* (CDN) pribadi dengan mengunggah file ke repositori GitHub melalui API.

---

## Fitur

-   **Unggah File**: Menyediakan endpoint API (`/api/upload`) untuk mengunggah file.
-   **Penggantian Nama Otomatis**: File yang diunggah akan diganti namanya secara otomatis dengan format `timestamp-ukuranfile.ekstensi` untuk memastikan nama yang unik.
-   **Integrasi GitHub**: Mengunggah file langsung ke repositori GitHub yang ditentukan menggunakan GitHub API.
-   **Respons URL**: Memberikan URL mentah (`raw_url`) dari file yang berhasil diunggah di GitHub.

---

## Persyaratan

Proyek ini memerlukan Python dan pustaka berikut:
-   Flask
-   requests
-   python-dotenv

---

## Pengaturan dan Instalasi

1.  **Clone Repositori**
    ```bash
    git clone [<URL_REPOSITORI_ANDA>](https://github.com/Adytm404/upload-private-cdn)
    cd upload-private-cdn
    ```

2.  **Buat dan Aktifkan Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Untuk Windows gunakan `venv\Scripts\activate`
    ```

3.  **Instal Dependensi**
    Pastikan semua dependensi yang ada di `requirements.txt` terinstal.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Konfigurasi Environment**
    Aplikasi ini menggunakan variabel environment untuk konfigurasi. Buat file `.env` di direktori root proyek. File `.env` dan direktori `venv` diabaikan oleh Git.
    ```
    GITHUB_TOKEN="your_github_personal_access_token"
    REPO_OWNER="your_github_username"
    REPO_NAME="your_github_repository_name"
    ```
    -   `GITHUB_TOKEN`: Token akses personal GitHub Anda dengan izin `repo`.
    -   `REPO_OWNER`: Nama pengguna atau organisasi pemilik repositori.
    -   `REPO_NAME`: Nama repositori di GitHub tempat file akan disimpan.

---

## Cara Menjalankan

1.  **Jalankan Aplikasi Flask**
    ```bash
    python app.py
    ```
    Aplikasi akan berjalan di `http://0.0.0.0:5000`.

2.  **Gunakan API untuk Mengunggah File**
    Gunakan `curl` atau alat API lainnya untuk mengirim permintaan `POST` ke endpoint `/api/upload`.

    Contoh menggunakan `curl`:
    ```bash
    curl -X POST -F "file=@/path/to/your/file.jpg" http://localhost:5000/api/upload
    ```

---

## Endpoint API

### Unggah File

-   **Endpoint**: `/api/upload`
-   **Metode**: `POST`
-   **Request**: `multipart/form-data`
    -   **Key**: `file`
    -   **Value**: File yang akan diunggah.

-   **Respons Sukses (`200 OK` atau `201 Created`)**
    ```json
    {
      "success": true,
      "url": "[https://raw.githubusercontent.com/REPO_OWNER/REPO_NAME/main/images/20231027103000-12345.jpg](https://raw.githubusercontent.com/REPO_OWNER/REPO_NAME/main/images/20231027103000-12345.jpg)"
    }
    ```

-   **Respons Gagal (`400 Bad Request`)**
    Jika tidak ada file yang disertakan dalam permintaan.
    ```json
    {
      "error": "No file provided"
    }
    ```
-   **Respons Gagal (dari GitHub)**
    Jika terjadi kesalahan saat mengunggah ke GitHub, respons dari API GitHub akan diteruskan.
    ```json
    {
        "success": false,
        "error": { ... }
    }
    ```
