# 💬 Chatbot Finansial - Bro Edition 🚀

Sebuah chatbot keuangan sederhana yang dibangun dengan Python dan Gradio. Bot ini bisa bantu lo catat pemasukan, pengeluaran, cicilan, dan kasih insight analisis keuangan pribadi lo pake prinsip budgeting 50/30/20.

---

## 🧠 Fitur

- 📝 Input pemasukan, pengeluaran, dan cicilan via natural language (bahasa sehari-hari)
- 🔍 Parsing nominal otomatis dari kalimat (misal: "gaji 5 juta, freelance 2 juta")
- 📊 Analisis keuangan berdasarkan rasio pengeluaran dan cicilan
- 💡 Rekomendasi budgeting 50/30/20 (kebutuhan, gaya hidup, tabungan)
- 🧾 State tracking: bot tau lo udah input apa aja
- ✅ UI simple pake Gradio — tinggal run & pakai!

---

## 🛠️ Tech Stack

- Python 3.10+
- Gradio
- Regex
- Modular code (state management, parser, chatbot logic)
- Optional: bisa di-deploy ke Hugging Face / Streamlit Cloud / Docker

---

## 🧪 Cara Jalankan

1. **Clone project**  
    ```bash
    git clone https://github.com/username/nama-repo.git
    cd nama-repo
    ```

2. **Bikin virtual environment (recommended)**  
    ```bash
    python -m venv venv
    source venv/bin/activate     # Linux/macOS
    .\venv\Scripts\activate      # Windows
    ```

3. **Install dependencies**  
    ```bash
    pip install -r requirements.txt
    ```

4. **Run chatbot**  
    ```bash
    python main.py
    ```

5. Akses di browser lo (default: http://127.0.0.1:7860)

---

## 🗂️ Struktur Project

AI-chatbot-finansial/
├── app/
│ ├── chatbot.py # logika chatbot
│ ├── parsing.py # parser input user
│ ├── state.py # manajemen state
│ └── init.py
├── main.py # UI Gradio
├── requirements.txt # dependencies
├── .gitignore
└── README.md


---

## 🧠 Insight

Tujuan utama project ini:
- Latihan state management & modular Python
- Implementasi parsing bahasa alami
- Showcase project AI kecil tapi kontekstual
- Bisa dikembangkan jadi financial planner otomatis

---

## 📌 Rencana Pengembangan (Next Step)

- Tambah penyimpanan ke SQLite / JSON
- Integrasi dengan Telegram / WhatsApp bot
- Support pengenalan entitas dengan NLP (spaCy)
- UI versi web pake Streamlit atau FastAPI

---

## ✨ Credit

Built with 🔥 oleh [@Assubki](https://github.com/Assubki)

---

git config --global user.name "Assubki"
git config --global user.email "subkisyafii@email.com"
