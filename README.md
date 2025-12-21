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

- Create folder name "data" and put .csv file as "music_dataset.csv" (https://www.kaggle.com/datasets/abdullahorzan/moodify-dataset?resource=download)

- python -m pip install -r mood_playlist_agent-main\requirements.txt

- New terminal (streamlit run app.py)



