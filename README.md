Proje Konusu: Ruh Haline göre Playlist yapan RAG Destekli Yapay Zekâ Ajanı

Ajanın Görevi: Kullanıcının girdiği tek veya birden fazla mood’u analiz etmek _ RAG veri kaynağından ilgili şarkıları bulmak ve playlist oluşturmak

Akış:
Kullanıcı
   ↓
Web Arayüzü (Streamlit)
   ↓
AI Ajanı
   ↓
LLM (Mood Analizi)
   ↓
RAG (Şarkı Verisi)
   ↓
Playlist

Run the code: 

- Put API key to .env from (https://platform.openai.com/api-keys) 

-Put the csv file in data folder (https://www.kaggle.com/datasets/abdullahorzan/moodify-dataset?resource=download)

- pip install -r requirements.txt 

- New terminal (streamlit run app.py)
