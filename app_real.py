import streamlit as st
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="AutoShortlist.AI Demo", page_icon="🤖")

st.title("🤖 AutoShortlist.AI - Resume Shortlisting Demo")

st.write("Upload your resume and paste a job description to see your match score!")

uploaded_file = st.file_uploader("📄 Upload Resume (PDF only)", type=["pdf"])
job_desc = st.text_area("🧾 Paste Job Description", height=200)

if uploaded_file and job_desc:
    pdf_reader = PdfReader(uploaded_file)
    resume_text = ""
    for page in pdf_reader.pages:
        resume_text += page.extract_text()

    documents = [resume_text, job_desc]
    tfidf = TfidfVectorizer().fit_transform(documents)
    similarity = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]

    score = round(similarity * 100, 2)

    st.subheader("✅ Job Match Score:")
    st.progress(score / 100)
    st.write(f"**{score}% Match**")

    skills = ["Python", "AWS", "AI", "Machine Learning", "Data Analysis", "Communication"]
    found = [s for s in skills if s.lower() in resume_text.lower()]
    st.subheader("💡 Detected Skills:")
    st.write(", ".join(found) if found else "No common skills found.")

    st.success("🎯 This shows how AutoShortlist.AI automatically matches resumes to jobs using AI!")
else:
    st.info("Please upload your resume and paste a job description to continue.")
