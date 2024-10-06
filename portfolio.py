import streamlit as st

import google.generativeai as genai


key=st.secrets["GOOGLE-API-KEY"]
genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-1.5-flash")

col1,space,col2=  st.columns([1,0.5,1])
with col1:
    st.title("About Me")
    st.write("I am Muhammad Dawood, a passionate data scientist with a strong foundation in machine learning, data analysis, and computer vision. I am currently pursuing a Bachelor's in Computer Science at Abdul Wali Khan University and have experience working on real-world data science projects through internships. Skilled in Python, SQL, and various data visualization tools, I aim to solve complex problems using data-driven approaches.")
with space:
    st.empty()
with col2:
    st.title("")
    st.image("pic.jpg",caption="Dawood",width=200)


st.title("Chat Bot")

persona="""
Yor are Dawood AI bot. You Help peoples to answer about yourself(e.g Dawood).Answer as if you are responding. Dont answer in second or third person. If you don't know the answer just say "To Knowing more about me Contact: hpofficial406@gmail.com here".
Here is more info about Dawood
Muhammad Dawood - Data Scientist & Data Analyst
Location: Mardan, Khyber Pakhtunkhwa, Pakistan
Education: Bachelor of Science in Computer Science, Abdul Wali Khan University

About Me:
I am Muhammad Dawood, a dedicated data scientist and data analyst with a strong foundation in machine learning, deep learning, computer vision, and data analysis. With a passion for uncovering insights from data, I use my skills in Python, SQL, and various analytical tools to solve complex problems and drive data-informed decisions.

Currently pursuing my Bachelor of Science in Computer Science at Abdul Wali Khan University, I have developed a deep understanding of data science concepts through both academic coursework and hands-on experience. I’m enthusiastic about leveraging my expertise to contribute to impactful projects and am continuously exploring new opportunities to grow in the field of data science.

Skills:

Data Science & Analysis
Machine Learning & Deep Learning
Computer Vision
Python & SQL
Data Visualization & Statistical Analysis
Professional Experience: I have completed internships focused on applying data science principles, contributing to real-world projects, and gaining experience in data-driven solutions.

Objective:
To leverage my analytical and technical expertise in a data-driven organization, where I can contribute to solving complex challenges, derive meaningful insights, and continue growing in the rapidly evolving field of data science.
 


"""
question=st.text_input("Ask Anything About me")
if st.button("Ask",use_container_width=400):
    prompt=persona+question
    response = model.generate_content(prompt)
    st.write(response.text)
st.subheader("Education")
edu="""
<ul>
  <li>Bachelor in Computer Science - Abdul Wali Khan University (2021 – 2025)</li>
  <li>Inter in Computer Science - BISE Mardan (2019-2021)</li>
  <li>Diploma in Information Technology - BTE Peshawar (2020-2021)</li>
  <li>Matric in Science - BISE Mardan (2017-2019)</li>
</ul>

"""
st.markdown(edu,unsafe_allow_html=True)
c1,c2=st.columns(2)

with c1:
    st.subheader("Certifications")
    html_code="""
    <ol>
    <li>IBM Data Science</li>
    <li>IBM AI-Engineering</li>
    <li>Data Analysis with Python</li>
    <li>Machine Learning, Ai and Data Science</li>
    <li>Data Science</li>
    <li>CIT(Web and Graphics Designing)</li>
    </ol>
    """
    st.markdown(html_code,unsafe_allow_html=True)

with c2:
    st.subheader("Languages")
    html=f"""
    <ul>
    <li>English</li>
    <li>Urdu</li>
    <li>Pashto</li>
    </ul>
    """
    st.markdown(html,unsafe_allow_html=True)

st.title("")

st.subheader("Skills")

st.slider("Programming(Python,SQL)",0,100,70)
st.slider("Data Science(Pandas, NumPy, Scikit-learn, TensorFlow, Keras)",0,100,80)
st.slider("Data Analysis",0,100,75)

st.subheader("Projects")
list=f"""
    <ul>
    <li>Sentiment Analysis</li>
    <li>Customer Segmentation</li>
    <li>TSLA Stock Price Analysis</li>
    <li>British Airways Customer Review Analysis</li>
    <li>House Price Prediction</li>
    <li>Heart Failure Classification</li>
    <li>Image Classification</li>
    <li>Recommender System</li>
    <li>Predictive System</li>
    <li>Breast Cancer Prediction</li>
    </ul>
    """
st.markdown(list,unsafe_allow_html=True)

st.subheader("Internships & Work Experience")
work="""
    <ul>
  <li>The Spark Foundation (june-july)2024</li>
  <li>Programmer's Tech (Jan-June)2024</li>
  <li>British Airways (Aug-Sept)2023</li>
  <li>internee.pk(Nov-Dec)2023</li>
</ul>

"""
st.markdown(work,unsafe_allow_html=True)

st.subheader("Contact")
con="""
Github: <a href='https://github.com/datascientist406' style='text-decoration:none;'>Click here</a><br>
Linkedin: <a href='https://linkedin.com/in/dawood406' style='text-decoration:none;'>Click here</a>
"""

st.markdown(con,unsafe_allow_html=True)
