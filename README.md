# OpenMusic Django API

OpenMusic-Django adalah REST API berbasis Django untuk mengelola data musik.

## 🚀 Fitur

- Autentikasi menggunakan Django Rest Framework (DRF)
- CRUD API untuk mengelola lagu dan playlist
- Token-based authentication

## 🛠️ Setup Proyek

### 1️⃣ **Clone Repository**

```bash
git clone https://github.com/Rizald95/OpenMusic-Django.git
cd OpenMusic-Django


```

2️⃣ **Buat Virtual Environment & Install Dependencies**

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt

```

3️⃣ **Buat File .env (Jika Diperlukan)**

```bash
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3


```

4️⃣ **Migrate Database**

```bash
python manage.py makemigrations
python manage.py migrate


```

5️⃣ **Jalankan Server**

```bash
python manage.py runserver

```
