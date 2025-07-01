import streamlit as st
from datetime import datetime

# Configure page
st.set_page_config(
    page_title="Sai Kumar Srinivas | Data Analytics Portfolio",
    page_icon="📊",
    layout="wide"
)

# CSS styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# Header
col1, col2 = st.columns([1, 3])
with col1:
    st.image("profile.jpg", width=150)  # Replace with your profile image

with col2:
    st.title("Sai Kumar Srinivas")
    st.subheader("Data Analytics Professional")
    st.write("""
    Worcester, MA | +1 (508) 365 9639 | 
    [saikumar.srinivas123@gmail.com](mailto:saikumar.srinivas123@gmail.com) | 
    [LinkedIn](https://www.linkedin.com/in/saikumar-srinivas/)
    """)
    st.write("""
    Data Analyst with expertise in Snowflake, Power BI, Python, and Machine Learning. 
    Passionate about transforming data into actionable insights and building efficient data systems.
    """)

# Navigation
st.markdown("---")
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", 
                          ["About", "Education", "Experience", "Projects", "Skills", "Contact"])

# About Section
if section == "About":
    st.header("About Me")
    st.write("""
    I am a Data Analytics professional currently pursuing my Master's degree at Clark University with a 3.9 GPA. 
    I have hands-on experience in data engineering, visualization, and machine learning across various industries.
    
    My technical expertise spans:
    - Data Warehousing (Snowflake, SQL)
    - Data Visualization (Power BI, Tableau)
    - Programming (Python, R, SQL)
    - Machine Learning & NLP
    - Cloud Technologies (AWS, Docker, Kubernetes)
    
    I'm passionate about solving complex problems with data-driven approaches and building systems that deliver value.
    """)

# Education Section
elif section == "Education":
    st.header("Education")
    
    with st.expander("Clark University, Worcester, MA", expanded=True):
        st.subheader("Master of Science in Data Analytics")
        st.write("Aug 2023 - May 2025 | CGPA: 3.9/4.0")
        st.write("""
        **Courses:** Mathematical Statistics, Machine Learning, Agile Methodologies, 
        Data Visualization, Business Intelligence
        """)
    
    with st.expander("AMC Engineering College, Bengaluru, Karnataka, India"):
        st.subheader("Bachelor of Science in Computers")
        st.write("July 2018 - Aug 2022 | CGPA: 3.7/4.0")

# Experience Section
elif section == "Experience":
    st.header("Professional Experience")
    
    with st.expander("Code Ninjas, Northborough, MA - Program Coordinator / Data Analyst", expanded=True):
        st.subheader("Program Coordinator / Data Analyst")
        st.write("Feb 2025 - Present")
        st.write("""
        - Spearheaded migration from legacy billing system to Snowflake, optimizing data storage and compute costs by 15%
        - Designed efficient data models in Snowflake using clustering keys and automatic scaling
        - Automated legacy billing reconciliation by SQL stored procedures in Snowflake, reduced validation time by 25%
        - Conducted data lineage analysis to transit from legacy systems, documenting in Snowflake's data dictionary
        - Replaced legacy ETL jobs with Snowflake Snowpipe for near-real-time data ingestion, cutting pipeline latency by 40%
        - Automated reporting and scheduling workflows using Google Sheets + App Script, reducing administrative time by 30%
        - Contributed to a 90% increase in student retention by analyzing feedback and optimizing lesson delivery
        """)
    
    with st.expander("Clark University, Worcester, MA - Teaching Assistant in Data Visualization"):
        st.subheader("Teaching Assistant in Data Visualization")
        st.write("Dec 2024 - May 2025")
        st.write("""
        - Guided students in data visualization using Tableau and Power BI
        - Applied advanced features like Calculated Fields, LOD Expressions, DAX, and Dynamic Parameters
        - Gained hands-on experience in data modelling, blending, relationships for visualization optimization
        """)
    
    with st.expander("Digit Insurance, Karnataka, India - Graduate Trainee Engineer / Software Development"):
        st.subheader("Graduate Trainee Engineer / Software Development")
        st.write("Aug 2022 - Aug 2023")
        st.write("""
        - Developed and optimized an email ticketing system, enhancing service efficiency by 15%
        - Automated web-based processes using Selenium, increasing bot efficiency by 20%
        - Deployed and managed applications in Docker & Kubernetes, reducing deployment time by 30%
        - Utilized Python (Pandas, NumPy) for data analysis, improving processing speed by 25%
        - Designed RESTful APIs using Flask for seamless data exchange between services
        - Reduced system downtime by 35% through troubleshooting and debugging automation scripts
        - Worked in agile environment implementing user-driven enhancements
        """)

# Projects Section
elif section == "Projects":
    st.header("Projects")
    
    with st.expander("Language Data Analytics & Computational Linguistics", expanded=True):
        st.subheader("Language Data Analytics & Computational Linguistics")
        st.write("Clark University, Worcester, MA")
        st.write("""
        **Project Overview:** Built strong language data systems to work with speech and text in multiple languages.
        
        - Built language datasets from scratch, adapting quickly to changing project needs
        - Worked with multilingual speech and text data, building Finite-State Transducers
        - Developed statistical language models to improve NLP tool accuracy
        - Analyzed linguistic data patterns using SQL, R, and MATLAB
        """)
    
    # Add more projects as needed
    with st.expander("Automated Reporting System"):
        st.subheader("Automated Reporting System")
        st.write("""
        - Developed a system to automate business reporting using Python and Power BI
        - Reduced manual reporting time by 60%
        - Implemented data validation checks to ensure report accuracy
        """)

# Skills Section
elif section == "Skills":
    st.header("Technical Skills")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Programming")
        st.write("""
        - R
        - Python
        - C#
        - JavaScript
        - SQL
        - HTML
        """)
        
        st.subheader("Database")
        st.write("""
        - MySQL
        - PostgreSQL
        - Microsoft SQL
        - MongoDB
        - Oracle EE
        """)
    
    with col2:
        st.subheader("Tools/CI-CD")
        st.write("""
        - Jira Software
        - Kubernetes
        - AWS Practitioner
        - FMEA, SWOT Analysis
        - Mind Manager, Lucid Chart
        - ERP, CRM, SAP
        - Snowflake, Oracle Cloud
        - RACI Matrix, WBS
        - Resource Allocation, Risk Analysis
        - Novologix system, Rally, Visio
        """)
        
        st.subheader("Data & Visualization")
        st.write("""
        - Pandas, NumPy
        - Matplotlib, Seaborn, Plotly
        - Tweepy, EDA, Trend Analysis
        - Tableau, Power BI
        - Flask, Streamlit
        """)
    
    with col3:
        st.subheader("ML & Deep Learning")
        st.write("""
        - Scikit-learn
        - TensorFlow, PyTorch, Keras
        - Transformers, YOLOv8
        - CNNs, RNNs
        - DSA
        """)
        
        st.subheader("NLP")
        st.write("""
        - RoBERTa, GPT-2, Pegasus
        - Hugging Face, LangChain
        - NLTK, SpaCy
        - Sentiment Analysis
        - QA Systems, Summarization
        """)

# Contact Section
elif section == "Contact":
    st.header("Contact Me")
    
    contact_form = """
    <form action="https://formsubmit.co/saikumar.srinivas123@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """
    
    st.markdown(contact_form, unsafe_allow_html=True)
    
    # Add social media links
    st.write("""
    ### Connect with me:
    - [LinkedIn](https://www.linkedin.com/in/saikumar-srinivas/)
    - Email: [saikumar.srinivas123@gmail.com](mailto:saikumar.srinivas123@gmail.com)
    - Phone: +1 (508) 365 9639
    """)

# Footer
st.markdown("---")
st.markdown(f"© {datetime.now().year} Sai Kumar Srinivas. All rights reserved.")