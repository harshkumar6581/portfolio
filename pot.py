import streamlit as st

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Harsh Kumar | Data Scientist & ML Engineer Portfolio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================================
# AESTHETIC DARK THEME CUSTOM CSS
# ==========================================
st.markdown(
    """
    <style>
    /* Google Fonts Import */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

    /* Global Color Variables & Theme Override */
    :root {
        --bg-color: #0d1117;
        --card-bg: #161b22;
        --card-border: #30363d;
        --accent-color: #6366f1;
        --accent-hover: #4f46e5;
        --accent-gradient: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        --text-primary: #f0f6fc;
        --text-secondary: #8b949e;
        --badge-bg: #21262d;
    }

    .stApp {
        background-color: var(--bg-color);
        color: var(--text-primary);
        font-family: 'Inter', sans-serif;
    }

    /* Modern Glassmorphic Cards */
    .glass-card {
        background: var(--card-bg);
        border: 1px solid var(--card-border);
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        transition: transform 0.3s ease, border-color 0.3s ease;
    }
    .glass-card:hover {
        border-color: var(--accent-color);
        transform: translateY(-2px);
    }

    /* Typography & Headers */
    .hero-greeting {
        color: var(--accent-color);
        font-family: 'JetBrains Mono', monospace;
        font-size: 1.1rem;
        font-weight: 600;
        letter-spacing: 1.5px;
        margin-bottom: 8px;
    }
    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 12px;
        background: var(--accent-gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero-subtitle {
        font-size: 1.5rem;
        color: var(--text-secondary);
        font-weight: 500;
        margin-bottom: 20px;
    }
    .section-header {
        font-size: 2rem;
        font-weight: 700;
        color: var(--text-primary);
        margin-top: 40px;
        margin-bottom: 24px;
        border-left: 4px solid var(--accent-color);
        padding-left: 12px;
    }

    /* Buttons & Social Links */
    .button-container {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .portfolio-btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        background: var(--accent-gradient);
        color: #ffffff !important;
        padding: 10px 24px;
        border-radius: 8px;
        font-weight: 600;
        text-decoration: none;
        transition: opacity 0.3s ease, transform 0.2s ease;
        border: none;
    }
    .portfolio-btn:hover {
        opacity: 0.9;
        transform: translateY(-1px);
    }
    .portfolio-btn-outline {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        background-color: var(--card-bg);
        color: var(--text-primary) !important;
        border: 1px solid var(--card-border);
        padding: 10px 24px;
        border-radius: 8px;
        font-weight: 600;
        text-decoration: none;
        transition: all 0.3s ease;
    }
    .portfolio-btn-outline:hover {
        border-color: var(--accent-color);
        color: var(--accent-color) !important;
    }

    /* Skill Badges & Timeline */
    .skill-badge {
        display: inline-block;
        background-color: var(--badge-bg);
        color: var(--text-primary);
        border: 1px solid var(--card-border);
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.88rem;
        font-weight: 500;
        margin: 4px;
        transition: all 0.2s ease;
    }
    .skill-badge:hover {
        border-color: var(--accent-color);
        color: var(--accent-color);
    }
    .timeline-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: var(--text-primary);
    }
    .timeline-subtitle {
        font-size: 1rem;
        color: var(--accent-color);
        font-weight: 600;
        margin-bottom: 4px;
    }
    .timeline-date {
        font-size: 0.85rem;
        color: var(--text-secondary);
        font-family: 'JetBrains Mono', monospace;
        margin-bottom: 12px;
    }

    /* Footer Styling */
    .footer {
        text-align: center;
        padding: 40px 0 20px 0;
        margin-top: 60px;
        border-top: 1px solid var(--card-border);
        color: var(--text-secondary);
        font-size: 0.9rem;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ==========================================
# SIDEBAR
# ==========================================
with st.sidebar:
    st.image(
        "https://api.dicebear.com/7.x/bottts/svg?seed=HarshKumar", width=120
    )
    st.markdown("## **Harsh Kumar**")
    st.caption("Data Scientist | ML Engineer")
    st.write("📍 Ramgarh, Jharkhand, India")

    st.markdown("---")
    st.markdown("### 📬 Quick Contact")
    st.markdown("📧 **Email:** [harshkumars2116@gmail.com](mailto:harshkumars2116@gmail.com)")
    st.markdown("📱 **Phone:** +91 9142678054")
    st.markdown("🔗 **LinkedIn:** [harsh-kumar](https://linkedin.com/in/harsh-kumar-5711703a1)")
    st.markdown("💻 **GitHub:** [harshkumar6581](https://github.com/harshkumar6581)")

    st.markdown("---")
    st.caption("Built with Streamlit & Python")

# ==========================================
# HERO SECTION
# ==========================================
st.markdown(
    """
    <div class="glass-card">
        <div class="hero-greeting">HELLO WORLD, I'M</div>
        <div class="hero-title">HARSH KUMAR</div>
        <div class="hero-subtitle">Aspiring Data Scientist & Machine Learning Engineer</div>
        <p style="color: #8b949e; line-height: 1.6; font-size: 1.05rem;">
            Leveraging strong foundational knowledge of Python, SQL, core computer science concepts, and practical project experience in data preprocessing and predictive modeling. Passionate about deploying deep learning architectures and analytical machine learning algorithms to drive scalable, data-backed solutions.
        </p>
        <div class="button-container">
            <a class="portfolio-btn" href="mailto:harshkumars2116@gmail.com">📩 Get In Touch</a>
            <a class="portfolio-btn-outline" href="https://github.com/harshkumar6581" target="_blank">🐙 GitHub Profile</a>
            <a class="portfolio-btn-outline" href="https://linkedin.com/in/harsh-kumar-5711703a1" target="_blank">💼 LinkedIn Profile</a>
        </div>
    </div>
""",
    unsafe_allow_html=True,
)

# ==========================================
# KEY METRICS DASHBOARD
# ==========================================
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric(label="🎓 Current Pursuit", value="B.Tech (AI & ML)")
with m2:
    st.metric(label="🚀 Key ML Projects", value="3 Complete")
with m3:
    st.metric(label="🎯 Max Model Accuracy", value="~92%")
with m4:
    st.metric(label="📜 Certifications", value="2 Professional")

# ==========================================
# TECHNICAL SKILLS MATRIX
# ==========================================
st.markdown('<div class="section-header">🛠️ Technical Skills & Competencies</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div class="glass-card">
            <h3>💻 Core CS & Languages</h3>
            <div style="margin-top: 12px;">
                <span class="skill-badge">Python</span>
                <span class="skill-badge">SQL</span>
                <span class="skill-badge">Data Structures</span>
                <span class="skill-badge">OOPs</span>
                <span class="skill-badge">DBMS</span>
                <span class="skill-badge">MySQL</span>
            </div>
            <h3 style="margin-top: 24px;">📊 Data Science & ML Libraries</h3>
            <div style="margin-top: 12px;">
                <span class="skill-badge">Pandas</span>
                <span class="skill-badge">NumPy</span>
                <span class="skill-badge">Scikit-learn</span>
                <span class="skill-badge">Matplotlib</span>
                <span class="skill-badge">Seaborn</span>
                <span class="skill-badge">Imbalanced-learn</span>
            </div>
        </div>
    """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="glass-card">
            <h3>🧠 ML Algorithms & Advanced Domain</h3>
            <div style="margin-top: 12px;">
                <span class="skill-badge">Linear & Logistic Regression</span>
                <span class="skill-badge">Classification & Clustering</span>
                <span class="skill-badge">Random Forest</span>
                <span class="skill-badge">SVM</span>
                <span class="skill-badge">KNN</span>
                <span class="skill-badge">Deep Learning</span>
                <span class="skill-badge">Natural Language Processing (NLP)</span>
            </div>
            <h3 style="margin-top: 24px;">⚙️ Developer Tools & Environments</h3>
            <div style="margin-top: 12px;">
                <span class="skill-badge">Jupyter Notebook</span>
                <span class="skill-badge">VS Code</span>
                <span class="skill-badge">Git</span>
                <span class="skill-badge">GitHub</span>
                <span class="skill-badge">Streamlit</span>
            </div>
        </div>
    """,
        unsafe_allow_html=True,
    )

# ==========================================
# FEATURED PROJECTS
# ==========================================
st.markdown('<div class="section-header">🚀 Featured Machine Learning Projects</div>', unsafe_allow_html=True)

# Project 1
st.markdown(
    """
    <div class="glass-card">
        <div class="timeline-title">📚 Book Recommendation System</div>
        <div class="timeline-subtitle">Python | Pandas | NumPy | Scikit-learn</div>
        <div class="timeline-date">Project Year: 2024</div>
        <ul style="color: #8b949e; line-height: 1.6;">
            <li>Designed and developed an end-to-end recommendation engine delivering personalized suggestions from user preference metrics and rating histories.</li>
            <li>Executed exploratory data analysis (EDA), automated data cleaning, and systematic feature transformation pipelines to maintain optimal dataset cleanliness.</li>
            <li>Implemented cosine similarity mechanisms to quantify user-item similarity metrics accurately.</li>
            <li>Constructed a streamlined inference workflow generating actionable user recommendations with low execution latency.</li>
        </ul>
        <span class="skill-badge">Cosine Similarity</span>
        <span class="skill-badge">Data Cleaning</span>
        <span class="skill-badge">EDA</span>
        <span class="skill-badge">Recommendation Engine</span>
    </div>
""",
    unsafe_allow_html=True,
)

# Project 2
st.markdown(
    """
    <div class="glass-card">
        <div class="timeline-title">📊 Customer Churn Prediction</div>
        <div class="timeline-subtitle">Python | Scikit-learn | Pandas | Matplotlib | Seaborn</div>
        <div class="timeline-date">Project Year: 2024</div>
        <ul style="color: #8b949e; line-height: 1.6;">
            <li>Engineered a machine learning classification framework designed to assess customer retention behavior dynamics.</li>
            <li>Conducted EDA, missing value handling, and categorical encoding feature engineering to maximize model predictive capability.</li>
            <li>Executed benchmarking across Random Forest and Logistic Regression techniques, achieving a high classification performance of <b>~85–90% accuracy</b>.</li>
        </ul>
        <span class="skill-badge">Classification</span>
        <span class="skill-badge">Random Forest</span>
        <span class="skill-badge">Feature Engineering</span>
        <span class="skill-badge">Predictive Analytics</span>
    </div>
""",
    unsafe_allow_html=True,
)

# Project 3
st.markdown(
    """
    <div class="glass-card">
        <div class="timeline-title">💳 Credit Card Fraud Detection System</div>
        <div class="timeline-subtitle">Python | Scikit-learn | Imbalanced-learn</div>
        <div class="timeline-date">Project Year: 2024</div>
        <ul style="color: #8b949e; line-height: 1.6;">
            <li>Built an end-to-end transaction fraud identification architecture tailored to resolve severe class imbalance issues.</li>
            <li>Applied Synthetic Minority Over-sampling Technique (SMOTE) paired with strategic undersampling to handle skewed class distribution.</li>
            <li>Fine-tuned hyperparameter profiles, optimizing the precision-recall balance to reach <b>~92% prediction accuracy</b> on validation sets.</li>
        </ul>
        <span class="skill-badge">SMOTE</span>
        <span class="skill-badge">Imbalanced Data</span>
        <span class="skill-badge">Hyperparameter Tuning</span>
        <span class="skill-badge">Fraud Detection</span>
    </div>
""",
    unsafe_allow_html=True,
)

# ==========================================
# EDUCATION & CERTIFICATIONS
# ==========================================
col_edu, col_cert = st.columns(2)

with col_edu:
    st.markdown('<div class="section-header">🎓 Education Timeline</div>', unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class="glass-card">
            <div class="timeline-title">Bachelor of Technology - Computer Science (AI & ML)</div>
            <div class="timeline-subtitle">OIST Bhopal, MP</div>
            <div class="timeline-date">2024 – 2027</div>
            <p style="color: #8b949e;">Focused specialization on Artificial Intelligence, Machine Learning Algorithms, Advanced Data Structures, and Database Systems.</p>
        </div>
        <div class="glass-card">
            <div class="timeline-title">Diploma in Electrical Engineering</div>
            <div class="timeline-subtitle">Gumla Polytechnic, Gumla, JH</div>
            <div class="timeline-date">2021 – 2024</div>
            <p style="color: #8b949e;">Strong foundation in technical problem-solving, engineering fundamentals, and quantitative logic.</p>
        </div>
        <div class="glass-card">
            <div class="timeline-title">Class X Secondary Education</div>
            <div class="timeline-subtitle">Kendriya Vidyalaya, Ramgarh, JH</div>
            <div class="timeline-date">Completed 2021</div>
        </div>
    """,
        unsafe_allow_html=True,
    )

with col_cert:
    st.markdown('<div class="section-header">📜 Certifications & Strengths</div>', unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class="glass-card">
            <div class="timeline-title">Python Programming Certification</div>
            <div class="timeline-subtitle">GeeksforGeeks</div>
            <p style="color: #8b949e; margin-top: 8px;">Comprehensive validation covering core structures, object-oriented concepts, algorithm optimization, and practical scripting fluency.</p>
        </div>
        <div class="glass-card">
            <div class="timeline-title">Data Science & Machine Learning Bootcamp</div>
            <div class="timeline-subtitle">Udemy (Instructor: Krish Naik)</div>
            <p style="color: #8b949e; margin-top: 8px;">Practical training covering complete data science pipelines, exploratory analysis, supervised/unsupervised ML models, and deep learning architectures.</p>
        </div>
        <div class="glass-card">
            <div class="timeline-title">⚡ Core Strengths</div>
            <div style="margin-top: 12px;">
                <span class="skill-badge">Analytical Problem-Solving</span>
                <span class="skill-badge">Rapid Technology Adaptability</span>
                <span class="skill-badge">Cross-functional Team Collaboration</span>
                <span class="skill-badge">Data-Driven Communication</span>
            </div>
        </div>
    """,
        unsafe_allow_html=True,
    )

# ==========================================
# FOOTER SECTION
# ==========================================
st.markdown(
    """
    <div class="footer">
        <p>© 2026 Harsh Kumar. All Rights Reserved.</p>
        <p>Built with Streamlit • Designed with Aesthetic Dark Theme UI</p>
    </div>
""",
    unsafe_allow_html=True,
)