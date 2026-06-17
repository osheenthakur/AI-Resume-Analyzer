import streamlit as st
import pdfplumber

st.title("📄 AI Resume Analyzer")
st.caption("Analyze resumes, detect skills, and receive improvement suggestions.")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text()

    st.subheader("Resume Content")
    st.write(text)
    st.success("Resume uploaded successfully!")

    skills = [
        "Python",
        "C++",
        "Java",
        "SQL",
        "Git",
        "GitHub",
        "HTML",
        "CSS",
        "JavaScript",
        "Machine Learning",
        "AI"
    ]

    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    st.subheader("Detected Skills")

    if found_skills:
        for skill in found_skills:
            st.success(skill)
    else:
        st.warning("No skills detected")

    score = len(found_skills) * 10

    if score > 100:
        score = 100

    st.metric("Skills Detected", len(found_skills))
    st.metric("Resume Strength", f"{score}%")
    st.subheader("Resume Score")
    st.progress(score / 100)
    st.write(f"Score: {score}/100")
    st.subheader("💪 Strengths")

if found_skills:
    for skill in found_skills:
        st.success(f"Strong in {skill}")

        st.subheader("📈 Recommended Skills")

recommended_skills = [
    "Python",
    "SQL",
    "Git",
    "GitHub",
    "Machine Learning"
]

for skill in recommended_skills:
    if skill not in found_skills:
        st.warning(f"Consider learning {skill}")

        st.subheader("📝 Resume Suggestions")

if score < 40:
    st.error("Your resume needs significant improvement.")

elif score < 70:
    st.warning("Your resume is decent but can be improved.")

else:
    st.success("Your resume looks strong!")
    st.subheader("🏆 Resume Category")

if score < 40:
    st.write("Beginner Level Resume")

elif score < 70:
    st.write("Intermediate Level Resume")

else:
    st.write("Strong Internship Ready Resume")

