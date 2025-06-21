# 🧠 AI Lab Report Explainer

Upload a **lab report (PDF or image)** and get a short, **human-friendly explanation** of the results in **English and Hindi** using a **powerful LLM (mistral-7b-instruct)** via **OpenRouter**.  
Ideal for patients, healthcare assistants, or anyone looking to **understand medical reports easily**.

![AI Report Explainer Demo](https://github.com/user-attachments/assets/695fb06e-f722-4f63-9118-31406e3095bb)
 <!-- Replace with actual image/GIF path -->

---

## 🚀 Live Demo

🔗 [Try the App on Streamlit](https://report-explainer-jv5sms6btbnf6nrmyxwmne.streamlit.app/)

---

## ✨ Features

- 📄 Accepts PDF, JPG, PNG reports (PDF for better text extraction)
- 🔍 Extracts text using **OCR** (EasyOCR + pdfplumber)
- 🧠 Explains the report in:
  - ✅ **English (layman explanation)**
  - **Hindi (translated explanation)**
  - **Urdu (translated explantion)**
- 📊 Mentions abnormal values (if any)
- 🔐 Secure API Key handling with `.env` and Streamlit Secrets

---

## 🧰 Tech Stack

| Component       | Tool                      |
|----------------|---------------------------|
| Frontend       | Streamlit                 |
| Backend Model  | Mistral-7b-instruct(via OpenRouter) |
| OCR Engine     | EasyOCR, pdfplumber       |
| LLM Interface  | LangChain                 |
| Deployment     | Streamlit Cloud           |

---

## 🧠 How It Works

- Upload: Choose a lab report (PDF, JPG, PNG)

- Extract: Text is extracted using EasyOCR or pdfplumber

- Prompt: Clean prompt template is prepared with LangChain

- Explain: Mistral AI responds with plain-English + Hindi and Urdu explanation

- Output: Shown nicely on Streamlit UI with abnormal values highlighted

---

## 📌 Sample Use Cases

- 🧑‍⚕️ Patients who can’t understand technical reports

- 🌐 Multilingual clinics for easy communication

- 🏥 Layman explanation and summary in different languages

---

## 📂 Folder Structure

- report-explainer/
 ├── main.py # Streamlit app
 ├── .env # API key (not committed)
 ├── requirements.txt # Python dependencies
 ├── utils/
 │ ├── init.py
 │ └── extractor.py # OCR and PDF text extractor
 ├── .gitignore
 └── README.md

---

## 🧪 How to Run Locally

- 1. Clone the repo
  - git clone https://github.com/hassanibnasad/report-explainer.git
  - cd report-explainer

- 2. Install dependencies
  - pip install -r requirements.txt

- 3. Add your OpenRouter API key
  - echo "OPENROUTER_API_KEY=your-key" > .env

- 4. Run the Streamlit app
  - streamlit run main.py
 
---

## 🙏 Credits

- Streamlit
- LangChain
- OpenRouter
- Mistral AI
- EasyOCR
- pdfplumber

