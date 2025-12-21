Proje Konusu:
-Ruh Haline göre Playlist yapan RAG Destekli Yapay Zekâ Ajanı

Ajanın Görevi:
-Kullanıcının girdiği tek veya birden fazla mood’u analiz etmek
-RAG veri kaynağından ilgili şarkıları bulmak ve playlist oluşturmak

Yapay Zekâ Ajanı:
-Girdi analizi (mood parsing)
-Karar verme (kaç şarkı, hangi mood)
-Eylem (playlist oluşturma)
-Çıktı üretme

RAG (Retrieval-Augmented Generation):
-Ana kaynak - https://www.kaggle.com/datasets/abdullahorzan/moodify-dataset?resource=download

Web Arayüzü:
-Input gir
-Playlist oluşsun


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

Files:
.env -API key location
agent.py - Uses the LLM to interpret user intent then Uses RAG to fetch songs
app.py -Interface
llm.py -Communication with OpenAI (Sends prompts-Receives model responses)
rag.py -Dataset
requirements.txt -Import list
service.py -AI understanding + data retrieval ?


Run the code:
-Put API key to .env - https://platform.openai.com/api-keys
-New terminal
pip install -r requirements.txt
streamlit run app.py