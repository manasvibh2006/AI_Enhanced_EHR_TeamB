import streamlit as st
import json
import os
from PIL import Image
from datetime import datetime

# ============== PAGE CONFIG ==============
st.set_page_config(
    page_title="AI-Enhanced EHR",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="auto"
)

# Initialize session state for page navigation
if "page" not in st.session_state:
    st.session_state.page = "landing"

def go_to_dashboard():
    st.session_state.page = "dashboard"

def go_to_landing():
    st.session_state.page = "landing"

# ============== LANDING PAGE ==============
def landing_page():
    st.markdown("""
    <style>
        /* Global Landing Page Styles */
        .main {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
            padding: 0;
        }
        
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 1400px;
        }
        
        /* Hero Section */
        .landing-hero {
            background: linear-gradient(135deg, #1e40af 0%, #3b82f6 50%, #60a5fa 100%);
            padding: 100px 60px;
            text-align: center;
            border-radius: 24px;
            margin-bottom: 4rem;
            box-shadow: 0 25px 50px rgba(30, 64, 175, 0.4);
            position: relative;
            overflow: hidden;
        }
        
        .landing-hero::before {
            content: '';
            position: absolute;
            top: -50%;
            right: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
            animation: pulse-glow 8s ease-in-out infinite;
        }
        
        @keyframes pulse-glow {
            0%, 100% { transform: scale(1); opacity: 0.3; }
            50% { transform: scale(1.1); opacity: 0.5; }
        }
        
        .landing-hero h1 {
            color: #ffffff;
            font-size: 4rem;
            font-weight: 900;
            margin: 0 0 1.5rem 0;
            text-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
            position: relative;
            z-index: 1;
            letter-spacing: -1px;
        }
        
        .landing-hero p {
            color: #e0f2fe;
            font-size: 1.5rem;
            margin: 0 0 1rem 0;
            font-weight: 400;
            position: relative;
            z-index: 1;
        }
        
        .landing-subtitle {
            color: #bfdbfe;
            font-size: 1.1rem;
            margin-top: 1.5rem;
            font-weight: 500;
            position: relative;
            z-index: 1;
        }
        
        /* Feature Grid */
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 2rem;
            margin: 3rem 0;
        }
        
        .feature-card {
            background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
            padding: 2.5rem;
            border-radius: 20px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            border: 1px solid rgba(30, 64, 175, 0.1);
            position: relative;
            overflow: hidden;
        }
        
        .feature-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 5px;
            background: linear-gradient(90deg, #1e40af 0%, #3b82f6 50%, #60a5fa 100%);
            transform: scaleX(0);
            transition: transform 0.4s ease;
        }
        
        .feature-card:hover::before {
            transform: scaleX(1);
        }
        
        .feature-card:hover {
            transform: translateY(-12px);
            box-shadow: 0 20px 60px rgba(30, 64, 175, 0.25);
        }
        
        .feature-icon {
            font-size: 3rem;
            margin-bottom: 1.5rem;
            display: inline-block;
            transition: transform 0.3s ease;
        }
        
        .feature-card:hover .feature-icon {
            transform: scale(1.1) rotate(5deg);
        }
        
        .feature-title {
            font-size: 1.4rem;
            font-weight: 700;
            color: #000080 !important;
            margin: 0 0 1rem 0;
            opacity: 1 !important;
        }
        
        .feature-text {
            color: #475569;
            font-size: 1rem;
            line-height: 1.7;
            margin: 0;
        }
        
        /* CTA Section */
        .cta-container {
            text-align: center;
            margin: 4rem 0;
        }
        
        .stButton > button {
            background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%) !important;
            color: white !important;
            padding: 18px 60px !important;
            border-radius: 50px !important;
            font-size: 1.2rem !important;
            font-weight: 700 !important;
            border: none !important;
            box-shadow: 0 15px 35px rgba(30, 64, 175, 0.4) !important;
            transition: all 0.3s ease !important;
            text-transform: uppercase !important;
            letter-spacing: 1px !important;
        }
        
        .stButton > button:hover {
            transform: translateY(-3px) !important;
            box-shadow: 0 20px 45px rgba(30, 64, 175, 0.5) !important;
        }
        
        /* Stats Section */
        .stats-row {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 2rem;
            margin: 4rem 0;
            background: linear-gradient(135deg, #ffffff 0%, #f1f5f9 100%);
            padding: 3rem 2rem;
            border-radius: 20px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
        }
        
        .stat-item {
            text-align: center;
            padding: 1rem;
        }
        
        .stat-number {
            font-size: 3rem;
            font-weight: 900;
            background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .stat-label {
            color: #64748b;
            font-size: 1rem;
            margin-top: 0.5rem;
            font-weight: 600;
        }
        
        /* Benefits Section */
        .benefits-list {
            background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
            padding: 3rem;
            border-radius: 20px;
            margin: 3rem 0;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
            border: 1px solid rgba(30, 64, 175, 0.1);
        }
        
        .benefits-list h3 {
            color: #1e40af;
            font-size: 2rem;
            margin-bottom: 2rem;
            font-weight: 800;
            text-align: center;
        }
        
        .benefit-item {
            display: flex;
            align-items: flex-start;
            margin-bottom: 1.5rem;
            padding: 1rem;
            background: #f8fafc;
            border-radius: 12px;
            transition: all 0.3s ease;
        }
        
        .benefit-item:hover {
            background: #eff6ff;
            transform: translateX(10px);
        }
        
        .benefit-item:last-child {
            margin-bottom: 0;
        }
        
        .benefit-icon {
            font-size: 1.8rem;
            margin-right: 1.5rem;
            color: #10b981;
            flex-shrink: 0;
        }
        
        .benefit-text {
            color: #334155;
            line-height: 1.7;
            font-size: 1rem;
        }
        
        .benefit-text strong {
            color: #1e40af;
            font-weight: 700;
        }
        
        /* Section Headers */
        .section-header-landing {
            text-align: center;
            color: #ffffff;
            font-size: 2.5rem;
            margin: 4rem 0 2rem 0;
            font-weight: 800;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
        }
        
        /* Footer */
        .footer-landing {
            text-align: center;
            padding: 3rem 2rem;
            color: #e2e8f0;
            margin-top: 5rem;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .footer-landing h3 {
            color: #ffffff;
            margin-bottom: 1rem;
            font-size: 2rem;
            font-weight: 700;
        }
        
        .footer-landing p {
            color: #cbd5e1;
            margin-bottom: 1.5rem;
            font-size: 1.1rem;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Hero Section
    st.markdown("""
    <div class="landing-hero">
        <h1>🏥 AI-Enhanced EHR System</h1>
        <p>Advanced Electronic Health Records Powered by Artificial Intelligence</p>
        <div class="landing-subtitle">Secure • Intelligent • Comprehensive</div>
    </div>
    """, unsafe_allow_html=True)
    
    # CTA Button
    st.markdown("<div class='cta-container'>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🚀 Access Patient Portal", key="cta_btn", use_container_width=True):
            go_to_dashboard()
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Key Features
    st.markdown('<h2 class="section-header-landing">Key Features</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-grid">
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <h3 class="feature-title">Comprehensive Records</h3>
            <p class="feature-text">Access complete patient histories, diagnoses, and treatment plans in one unified view.</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🤖</div>
            <h3 class="feature-title">AI-Powered Analytics</h3>
            <p class="feature-text">Leverage machine learning insights for enhanced diagnostic accuracy and clinical decision support.</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🖼️</div>
            <h3 class="feature-title">Medical Imaging</h3>
            <p class="feature-text">AI-enhanced medical images with improved visualization for better diagnostic interpretation.</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🔐</div>
            <h3 class="feature-title">Security & Privacy</h3>
            <p class="feature-text">HIPAA-compliant infrastructure ensuring patient data protection and confidentiality.</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">📈</div>
            <h3 class="feature-title">Clinical Insights</h3>
            <p class="feature-text">Real-time analytics and trend analysis for improved patient outcomes and care coordination.</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">⚡</div>
            <h3 class="feature-title">Instant Access</h3>
            <p class="feature-text">Lightning-fast retrieval of patient records with intuitive navigation and search capabilities.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats Section
    st.markdown("""
    <div class="stats-row">
        <div class="stat-item">
            <div class="stat-number">100+</div>
            <div class="stat-label">Active Patients</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">99.9%</div>
            <div class="stat-label">System Uptime</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">24/7</div>
            <div class="stat-label">Access Availability</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">50+</div>
            <div class="stat-label">Data Points/Patient</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Benefits Section
    st.markdown("""
    <div class="benefits-list">
        <h3>Why Choose Our EHR System?</h3>
        <div class="benefit-item">
            <span class="benefit-icon">✓</span>
            <div class="benefit-text"><strong>Unified Patient View:</strong> Consolidate all patient information in a single, easy-to-navigate dashboard</div>
        </div>
        <div class="benefit-item">
            <span class="benefit-icon">✓</span>
            <div class="benefit-text"><strong>AI-Enhanced Diagnostics:</strong> Automated image analysis and clinical recommendations powered by advanced algorithms</div>
        </div>
        <div class="benefit-item">
            <span class="benefit-icon">✓</span>
            <div class="benefit-text"><strong>Standardized Coding:</strong> Automatic ICD-10 mapping for proper billing and medical coding compliance</div>
        </div>
        <div class="benefit-item">
            <span class="benefit-icon">✓</span>
            <div class="benefit-text"><strong>Real-time Updates:</strong> Instant access to the latest patient information and clinical notes</div>
        </div>
        <div class="benefit-item">
            <span class="benefit-icon">✓</span>
            <div class="benefit-text"><strong>Enterprise Security:</strong> Bank-level encryption and compliance with healthcare data regulations</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div class="footer-landing">
        <h3>Ready to Transform Your EHR Experience?</h3>
        <p>Join hundreds of healthcare professionals already using our AI-Enhanced EHR System</p>
    </div>
    """, unsafe_allow_html=True)

# ============== DASHBOARD PAGE ==============
def dashboard_page():
    # Custom CSS for Dashboard
    st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    .main {
        font-family: 'Inter', sans-serif;
        background-color: #f0f4f8;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Header Styling */
    .main-header {
        background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%);
        padding: 1.5rem 2rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 15px rgba(30, 58, 95, 0.3);
    }
    
    .main-header h1 {
        color: white;
        font-size: 1.8rem;
        font-weight: 600;
        margin: 0;
    }
    
    .main-header p {
        color: #a8c5e2;
        margin: 0.3rem 0 0 0;
        font-size: 0.95rem;
    }
    
    /* Patient Info Card */
    .patient-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
        border-left: 5px solid #2d5a87;
        margin-bottom: 1.5rem;
    }
    
    .patient-name {
        font-size: 1.4rem;
        font-weight: 600;
        color: #1e3a5f;
        margin-bottom: 0.5rem;
    }
    
    .patient-id {
        background: #e8f4fd;
        color: #2d5a87;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 500;
        display: inline-block;
    }
    
    /* Metric Cards */
    .metric-container {
        display: flex;
        gap: 1rem;
        flex-wrap: wrap;
        margin: 1rem 0;
    }
    
    .metric-card {
        background: white;
        border-radius: 10px;
        padding: 1rem 1.5rem;
        flex: 1;
        min-width: 150px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
        border-top: 3px solid #4CAF50;
    }
    
    .metric-card.warning {
        border-top-color: #ff9800;
    }
    
    .metric-card.danger {
        border-top-color: #f44336;
    }
    
    .metric-card.info {
        border-top-color: #2196F3;
    }
    
    .metric-label {
        font-size: 0.75rem;
        color: #6b7280;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-weight: 500;
    }
    
    .metric-value {
        font-size: 1.3rem;
        font-weight: 600;
        color: #1e3a5f;
        margin-top: 0.3rem;
    }
    
    /* Section Cards */
    .section-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    }
    
    .section-header {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        margin-bottom: 1rem;
        padding-bottom: 0.75rem;
        border-bottom: 2px solid #e5e7eb;
    }
    
    .section-icon {
        font-size: 1.3rem;
    }
    
    .section-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #000080 !important;
        margin: 0;
        opacity: 1 !important;
    }
    
    .section-content {
        color: #374151;
        line-height: 1.6;
    }
    
    /* Diagnosis Badge */
    .diagnosis-badge {
        background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%);
        border: 1px solid #ffb74d;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    
    .diagnosis-text {
        color: #e65100;
        font-weight: 600;
        font-size: 1rem;
    }
    
    /* ICD Code */
    .icd-code {
        background: #1e3a5f;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 6px;
        font-family: 'Monaco', 'Consolas', monospace;
        font-size: 0.95rem;
        display: inline-block;
    }
    
    /* Plan Items */
    .plan-item {
        background: #f0fdf4;
        border-left: 3px solid #22c55e;
        padding: 0.75rem 1rem;
        margin: 0.5rem 0;
        border-radius: 0 8px 8px 0;
        color: #166534;
    }
    
    /* Status Indicator */
    .status-active {
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        background: #dcfce7;
        color: #166534;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 500;
    }
    
    .status-dot {
        width: 8px;
        height: 8px;
        background: #22c55e;
        border-radius: 50%;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    
    /* Image Container */
    .image-container {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
    }
    
    .image-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
    }
    
    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: white;
        padding: 0.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: 500;
        color: #000080 !important;
        opacity: 1 !important;
    }
    
    .stTabs [aria-selected="true"] {
        background: #1e3a5f !important;
        color: white !important;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 1.5rem;
        color: #6b7280;
        font-size: 0.85rem;
        margin-top: 2rem;
        border-top: 1px solid #e5e7eb;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .metric-container {
            flex-direction: column;
        }
    }
</style>
""", unsafe_allow_html=True)
    
    # Load Data
    @st.cache_data
    def load_ehr():
        import os
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(current_dir, "Data", "ehr_processed.json")
        if not os.path.exists(data_path):
            st.error(f"Data file not found at: {data_path}")
            return {}
        with open(data_path, "r", encoding="utf-8") as f:
            return json.load(f)
    
    ehr_data = load_ehr()
    if not ehr_data:
        st.error("No patient data available. Please check the data file.")
        st.stop()
    patient_ids = sorted(ehr_data.keys())
    
    # Sidebar
    with st.sidebar:
        st.markdown("""
    <div style="text-align: center; padding: 1rem 0;">
        <h2 style="color: white; margin: 0;">🏥 EHR SYSTEM</h2>
        <p style="color: #a8c5e2; font-size: 0.85rem;">AI-Enhanced Portal</p>
    </div>
    """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Back to Landing Button
        if st.button("← Back to Landing", key="back_btn", use_container_width=True):
            go_to_landing()
            st.rerun()
        
        st.markdown("---")
        
        st.markdown('<p style="color: #a8c5e2; font-size: 0.85rem; margin-bottom: 0.5rem;">📋 PATIENT SELECTION</p>', unsafe_allow_html=True)
        patient_id = st.selectbox(
            "Select Patient",
            patient_ids,
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        # Quick Stats
        st.markdown('<p style="color: #a8c5e2; font-size: 0.85rem;">📊 QUICK STATS</p>', unsafe_allow_html=True)
        st.markdown(f"""
    <div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 8px; margin-top: 0.5rem;">
        <p style="color: white; margin: 0.3rem 0; font-size: 0.9rem;">
            <strong>Total Patients:</strong> {len(patient_ids)}
        </p>
        <p style="color: white; margin: 0.3rem 0; font-size: 0.9rem;">
            <strong>Current ID:</strong> {patient_id}
        </p>
        <p style="color: white; margin: 0.3rem 0; font-size: 0.9rem;">
            <strong>Last Updated:</strong> {datetime.now().strftime("%b %d, %Y")}
        </p>
    </div>
    """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # System Status
        st.markdown('<p style="color: #a8c5e2; font-size: 0.85rem;">⚡ SYSTEM STATUS</p>', unsafe_allow_html=True)
        st.markdown("""
    <div style="margin-top: 0.5rem;">
        <span style="display: inline-flex; align-items: center; gap: 0.3rem; color: #4ade80; font-size: 0.85rem;">
            <span style="width: 8px; height: 8px; background: #4ade80; border-radius: 50%; display: inline-block;"></span>
            All Systems Operational
        </span>
    </div>
    """, unsafe_allow_html=True)
    
    patient = ehr_data[patient_id]
    
    # Header
    st.markdown("""
<div class="main-header">
    <h1>🩺 AI-Enhanced Electronic Health Record</h1>
    <p>Integrated clinical summary, diagnostics, and medical imaging powered by AI</p>
</div>
""", unsafe_allow_html=True)
    
    # Parse Clinical Note
    note = patient.get("clinical_note", "")
    sections = {}
    for block in note.split("\n\n"):
        if ":" in block:
            key, value = block.split(":", 1)
            sections[key.strip()] = value.strip()
    
    # Patient Info Card
    patient_name = patient.get("name", f"Patient {patient_id}")
    
    st.markdown(f"""
<div class="patient-card">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap;">
        <div>
            <div class="patient-name">{patient_name}</div>
            <span class="patient-id">ID: {patient_id}</span>
            <div class="status-active" style="margin-left: 0.5rem; display: inline-flex;">
                <span class="status-dot"></span>
                Active Record
            </div>
        </div>
        <div style="text-align: right; color: #6b7280; font-size: 0.9rem;">
            <div>📅 Accessed: {datetime.now().strftime("%B %d, %Y at %I:%M %p")}</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
    
    # Metric Cards
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
    <div class="metric-card info">
        <div class="metric-label">Patient ID</div>
        <div class="metric-value">{patient_id}</div>
    </div>
    """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">ICD-10 Code</div>
        <div class="metric-value">{patient.get("icd10", "N/A")[:10]}</div>
    </div>
    """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
    <div class="metric-card warning">
        <div class="metric-label">Record Status</div>
        <div class="metric-value">Active</div>
    </div>
    """, unsafe_allow_html=True)
    
    with col4:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_dir = os.path.join(current_dir, "Images", "ehr_processedimages")
        if os.path.exists(image_dir):
            image_files = [f for f in os.listdir(image_dir) if f.lower().startswith(patient_id.lower())]
            has_image = len(image_files) > 0
        else:
            has_image = False
        img_status = "Available" if has_image else "Pending"
        st.markdown(f"""
    <div class="metric-card {'info' if has_image else 'danger'}">
        <div class="metric-label">Medical Image</div>
        <div class="metric-value">{img_status}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Tabs
    st.markdown("<br>", unsafe_allow_html=True)
    tab1, tab2, tab3 = st.tabs(["📋 Clinical Summary", "🖼️ Medical Imaging", "📄 Raw EHR Data"])
    
    # Tab 1: Clinical Summary
    with tab1:
        col_left, col_right = st.columns([2, 1])
        
        with col_left:
            st.markdown(f"""
        <div class="section-card">
            <div class="section-header">
                <span class="section-icon">🎯</span>
                <h3 class="section-title">Chief Complaint / Reason for Visit</h3>
            </div>
            <div class="section-content">
                {sections.get("Chief Complaint", "No chief complaint recorded.")}
            </div>
        </div>
        """, unsafe_allow_html=True)
            
            st.markdown(f"""
        <div class="section-card">
            <div class="section-header">
                <span class="section-icon">📝</span>
                <h3 class="section-title">History of Present Illness</h3>
            </div>
            <div class="section-content">
                {sections.get("History of Present Illness", "No history recorded.")}
            </div>
        </div>
        """, unsafe_allow_html=True)
            
            st.markdown(f"""
        <div class="section-card">
            <div class="section-header">
                <span class="section-icon">🔬</span>
                <h3 class="section-title">Clinical Findings & Examination</h3>
            </div>
            <div class="section-content">
                {sections.get("Examination Findings", "No examination findings recorded.")}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        with col_right:
            diagnosis = sections.get("Diagnosis", "Pending diagnosis")
            st.markdown(f"""
        <div class="section-card">
            <div class="section-header">
                <span class="section-icon">⚕️</span>
                <h3 class="section-title">Primary Diagnosis</h3>
            </div>
            <div class="diagnosis-badge">
                <div class="diagnosis-text">{diagnosis}</div>
            </div>
            <div style="margin-top: 1rem;">
                <span style="font-size: 0.85rem; color: #6b7280;">ICD-10 Classification:</span>
                <div class="icd-code" style="margin-top: 0.5rem;">{patient.get("icd10", "Not available")}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
            
            plan = sections.get("Plan", "")
            plan_html = ""
            if plan:
                for step in plan.split(","):
                    if step.strip():
                        plan_html += f'<div class="plan-item">✓ {step.strip()}</div>'
            else:
                plan_html = '<div style="color: #6b7280;">No treatment plan recorded.</div>'
            
            st.markdown(f"""
        <div class="section-card">
            <div class="section-header">
                <span class="section-icon">📋</span>
                <h3 class="section-title">Treatment Plan</h3>
            </div>
            {plan_html}
        </div>
        """, unsafe_allow_html=True)
    
    # Tab 2: Medical Imaging
    with tab2:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_dir = os.path.join(current_dir, "Images", "ehr_processedimages")
        if os.path.exists(image_dir):
            image_files = [f for f in os.listdir(image_dir) if f.lower().startswith(patient_id.lower())]
            image_path = os.path.join(image_dir, image_files[0]) if image_files else None
        else:
            image_path = None
        
        st.markdown("""
    <div class="image-container">
        <div class="image-header">
            <div>
                <h3 style="margin: 0; color: #1e3a5f;">🖼️ AI-Enhanced Medical Image</h3>
                <p style="margin: 0.3rem 0 0 0; color: #6b7280; font-size: 0.9rem;">Enhanced visualization for improved diagnostic accuracy</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
        
        if image_path and os.path.exists(image_path):
            col1, col2, col3 = st.columns([1, 3, 1])
            with col2:
                try:
                    image = Image.open(image_path)
                    st.image(image, use_container_width=True)
                    
                    file_ext = os.path.splitext(image_path)[1].upper().replace('.', '')
                    st.markdown(f"""
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
                <div style="display: flex; justify-content: space-around; text-align: center;">
                    <div>
                        <div style="color: #6b7280; font-size: 0.8rem;">Format</div>
                        <div style="font-weight: 600; color: #1e3a5f;">{file_ext}</div>
                    </div>
                    <div>
                        <div style="color: #6b7280; font-size: 0.8rem;">Dimensions</div>
                        <div style="font-weight: 600; color: #1e3a5f;">{image.size[0]} x {image.size[1]}</div>
                    </div>
                    <div>
                        <div style="color: #6b7280; font-size: 0.8rem;">Enhancement</div>
                        <div style="font-weight: 600; color: #22c55e;">AI-Enhanced</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error loading image: {str(e)}")
        else:
            st.markdown("""
        <div style="text-align: center; padding: 4rem 2rem; background: #f8fafc; border-radius: 12px; border: 2px dashed #d1d5db;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">🖼️</div>
            <h3 style="color: #374151; margin: 0;">No Image Available</h3>
            <p style="color: #6b7280; margin-top: 0.5rem;">Enhanced medical image will appear here once linked to this patient record.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Tab 3: Raw Data
    with tab3:
        st.markdown("""
    <div class="section-card">
        <div class="section-header">
            <span class="section-icon">💾</span>
            <h3 class="section-title">Raw EHR Data (JSON Format)</h3>
        </div>
    </div>
    """, unsafe_allow_html=True)
        
        json_str = json.dumps(patient, indent=2)
        st.download_button(
            label="📥 Download JSON",
            data=json_str,
            file_name=f"patient_{patient_id}_ehr.json",
            mime="application/json"
        )
        
        st.json(patient)
    
    # Footer
    st.markdown("""
<div class="footer">
    <div style="display: flex; justify-content: center; align-items: center; gap: 2rem; flex-wrap: wrap;">
        <span>🏥 AI-Enhanced EHR System</span>
        <span>•</span>
        <span>Streamlit-based EHR Viewer</span>
        <span>•</span>
        <span>© 2026 Healthcare AI Solutions</span>
    </div>
    <p style="margin-top: 0.5rem; font-size: 0.8rem; color: #9ca3af;">
        Powered by AI | Secure & HIPAA Compliant
    </p>
</div>
""", unsafe_allow_html=True)

# ============== PAGE ROUTING ==============
if __name__ == "__main__":
    if st.session_state.page == "landing":
        landing_page()
    elif st.session_state.page == "dashboard":
        dashboard_page()