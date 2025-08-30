import streamlit as st
import PyPDF2
import io
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Resume Critiquer", page_icon="📃", layout="centered")

st.title("AI Resume Critiquer")
st.markdown("Upload your resume and get AI-powered feedback tailored to your needs!")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role you're targeting (optional)")

analyze = st.button("Analyze Resume")

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")

if analyze and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)
        
        if not file_content.strip():
            st.error("File does not have any content...")
            st.stop()
        
        prompt = f"""Please analyze this resume and provide constructive feedback. 
        Focus on the following aspects:
        1. Content clarity and impact
        2. Skills presentation
        3. Experience descriptions
        4. Specific improvements for {job_role if job_role else 'general job applications'}
        
        Resume content:
        {file_content}
        
        Please provide your analysis in a clear, structured format with specific recommendations."""
        
        client = Groq(api_key=GROQ_API_KEY)
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",   # or "llama-3.1-70b-versatile"
            messages=[
                {"role": "system", "content": "You are an expert resume reviewer with years of experience in HR and recruitment."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        
        st.markdown("### Analysis Results")
        st.markdown(response.choices[0].message.content)
    
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
