import streamlit as st
import time
import random

st.set_page_config(page_title="AutoShortlist.AI Demo", page_icon="🤖")

st.title("🤖 AutoShortlist.AI - Smart Resume Shortlisting System")
st.write("Experience how AI shortlists resumes automatically!")

st.image("https://cdn-icons-png.flaticon.com/512/4712/4712100.png", width=150)
st.markdown("---")

job_role = st.text_input("Enter Job Role (e.g., Data Analyst, Cloud Engineer):")
if st.button("Run AutoShortlist.AI"):
    with st.spinner("🔍 Analyzing resumes..."):
        time.sleep(2)
    with st.spinner("🧠 Matching skills and experience..."):
        time.sleep(2)
    with st.spinner("📊 Generating shortlist..."):
        time.sleep(2)

    score = random.randint(70, 98)
    st.success(f"✅ AutoShortlist.AI completed the shortlisting for **{job_role}** role!")
    st.subheader(f"🎯 Average Candidate Match Score: {score}%")
    st.write("Top shortlisted candidates ready for review!")

st.markdown("---")
st.caption("Powered by AWS Textract, Bedrock, Lambda, and SageMaker 🧩")
