import streamlit as st
import os
import tempfile
from dotenv import load_dotenv
from utils.extractor import extract_text
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from langchain_anthropic import ChatAnthropic
from langchain.chat_models import ChatOpenAI
import warnings
warnings.filterwarnings("ignore")


# Load .env for OpenRouter API key
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "mistralai/mistral-7b-instruct"

# Streamlit UI setup
st.set_page_config(page_title="AI Lab Report Explainer", layout="centered")
st.title("🧠 AI Lab Report Explainer")

uploaded_file = st.file_uploader("Upload Lab Report (PDF, JPG, PNG)", type=["pdf", "jpg", "jpeg", "png"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[-1]) as tmp:
        tmp.write(uploaded_file.read())
        file_path = tmp.name

    with st.spinner("🔍 Extracting text from report..."):
        extracted_text = extract_text(file_path)

    st.subheader("📄 Extracted Text")
    st.code(extracted_text)

    if st.button("🧠 Explain this Report"):
        prompt_template = PromptTemplate(
            input_variables=["report_text"],
            template="""
You are an expert medical doctor.

Below is a list of lab test results extracted from a diagnostic report:

[START OF REPORT]
{report_text}
[END OF REPORT]

Please generate the following:
1. Layman Explanation (English):  Medically accurate interpretation with normal reference ranges. Simplified, easy-to-understand (minimum lines possible).
2. Provide summery in simple word.
3. Hindi: Translate the summery into Hindi (हिंदी).
4. Urdu: Translate the summery into Urdu (اردو).
Use a clean format, be very concise but informative. If any value is abnormal, mention it briefly.
"""
        )
        formatted_prompt = prompt_template.format(report_text=extracted_text)

        with st.spinner("🧠 Preparing explanation..."):
            try:
                chat = ChatOpenAI(
                    model=MODEL,
                    api_key=OPENROUTER_API_KEY,
                    base_url="https://openrouter.ai/api/v1"
                )
                response = chat.invoke([HumanMessage(content=formatted_prompt)])
                st.subheader("📋 Explanation")
                st.markdown(response.content)
            except Exception as e:
                st.error(f"❌ Failed to get explanation: {str(e)}")