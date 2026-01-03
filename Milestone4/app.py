import streamlit as st
import json
import os
from PIL import Image
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI-Enhanced EHR",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ----------------
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
        color:#0f172a;
        margin: 0;
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
    
    /* Sidebar Styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #1e3a5f 0%, #2d5a87 100%);
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e3a5f 0%, #2d5a87 100%);
    }
    
    [data-testid="stSidebar"] .stSelectbox label {
        color: white !important;
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
    
    /* ================= FIX FADED / INVISIBLE SECTION HEADINGS ================= */

/* Force section heading text color */
.section-title,
.section-header h3 {
    color: #000080 !important;   /* Navy Blue */
    opacity: 1 !important;
    font-weight: 600 !important;
}

/* Force icons to stay visible */
.section-icon {
    color: #000080 !important;
    opacity: 1 !important;
}

/* Ensure header container does not reduce opacity */
.section-header {
    opacity: 1 !important;
}

/* Prevent inherited opacity from parents */
.section-header *,
.section-card h3 {
    opacity: 1 !important;
}


/* ================= FIX TAB TEXT VISIBILITY ================= */

.stTabs [data-baseweb="tab"] {
    color: #000080 !important;
    font-weight: 500;
    opacity: 1 !important;
}

.stTabs [aria-selected="true"] {
    background: #1e3a5f !important;
    color: #ffffff !important;
    opacity: 1 !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_ehr():
    with open("Data/ehr_processed.json", "r", encoding="utf-8") as f:
        return json.load(f)

ehr_data = load_ehr()
patient_ids = sorted(ehr_data.keys())

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 1rem 0;">
        <h2 style="color: white; margin: 0;">🏥 EHR SYSTEM</h2>
        <p style="color: #a8c5e2; font-size: 0.85rem;">AI-Enhanced Portal</p>
    </div>
    """, unsafe_allow_html=True)
    
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

# ---------------- HEADER ----------------
st.markdown("""
<div class="main-header">
    <h1>🩺 AI-Enhanced Electronic Health Record</h1>
    <p>Integrated clinical summary, diagnostics, and medical imaging powered by AI</p>
</div>
""", unsafe_allow_html=True)

# ---------------- PARSE CLINICAL NOTE ----------------
note = patient.get("clinical_note", "")
sections = {}

for block in note.split("\n\n"):
    if ":" in block:
        key, value = block.split(":", 1)
        sections[key.strip()] = value.strip()

# ---------------- PATIENT INFO CARD ----------------
patient_name = patient.get("name", f"Patient {patient_id}")
patient_age = patient.get("age", "N/A")
patient_gender = patient.get("gender", "N/A")
patient_dob = patient.get("dob", "N/A")

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

# ---------------- METRIC CARDS ----------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card info">
        <div class="metric-label">Patient ID</div>
        <div class="metric-value">""" + patient_id + """</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">ICD-10 Code</div>
        <div class="metric-value">""" + patient.get("icd10", "N/A")[:10] + """</div>
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
    has_image = os.path.exists(f"Images/enhanced/{patient_id}.png")
    img_status = "Available" if has_image else "Pending"
    st.markdown(f"""
    <div class="metric-card {'info' if has_image else 'danger'}">
        <div class="metric-label">Medical Image</div>
        <div class="metric-value">{img_status}</div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- TABS ----------------
st.markdown("<br>", unsafe_allow_html=True)
tab1, tab2, tab3 = st.tabs([
    "📋 Clinical Summary",
    "🖼️ Medical Imaging",
    "📄 Raw EHR Data"
])

# ---------------- TAB 1: CLINICAL SUMMARY ----------------
with tab1:
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        # Chief Complaint
        st.markdown("""
        <div class="section-card">
            <div class="section-header">
                <span class="section-icon">🎯</span>
                <h3 class="section-title">Chief Complaint / Reason for Visit</h3>
            </div>
            <div class="section-content">
                """ + sections.get("Chief Complaint", "No chief complaint recorded.") + """
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # History of Present Illness
        st.markdown("""
        <div class="section-card">
            <div class="section-header">
                <span class="section-icon">📝</span>
                <h3 class="section-title">History of Present Illness</h3>
            </div>
            <div class="section-content">
                """ + sections.get("History of Present Illness", "No history recorded.") + """
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Examination Findings
        st.markdown("""
        <div class="section-card">
            <div class="section-header">
                <span class="section-icon">🔬</span>
                <h3 class="section-title">Clinical Findings & Examination</h3>
            </div>
            <div class="section-content">
                """ + sections.get("Examination Findings", "No examination findings recorded.") + """
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_right:
        # Diagnosis
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
        
        # Treatment Plan
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

# ---------------- TAB 2: IMAGE ----------------
with tab2:
    image_path = f"Images/enhanced/{patient_id}.png"
    
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
    
    if os.path.exists(image_path):
        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
            image = Image.open(image_path)
            st.image(image, use_column_width=True)
            
            # Image info
            st.markdown(f"""
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
                <div style="display: flex; justify-content: space-around; text-align: center;">
                    <div>
                        <div style="color: #6b7280; font-size: 0.8rem;">Format</div>
                        <div style="font-weight: 600; color: #1e3a5f;">PNG</div>
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
    else:
        st.markdown("""
        <div style="text-align: center; padding: 4rem 2rem; background: #f8fafc; border-radius: 12px; border: 2px dashed #d1d5db;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">🖼️</div>
            <h3 style="color: #374151; margin: 0;">No Image Available</h3>
            <p style="color: #6b7280; margin-top: 0.5rem;">Enhanced medical image will appear here once linked to this patient record.</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------- TAB 3: RAW DATA ----------------
with tab3:
    st.markdown("""
    <div class="section-card">
        <div class="section-header">
            <span class="section-icon">💾</span>
            <h3 class="section-title">Raw EHR Data (JSON Format)</h3>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Add download button
    json_str = json.dumps(patient, indent=2)
    st.download_button(
        label="📥 Download JSON",
        data=json_str,
        file_name=f"patient_{patient_id}_ehr.json",
        mime="application/json"
    )
    
    st.json(patient)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    <div style="display: flex; justify-content: center; align-items: center; gap: 2rem; flex-wrap: wrap;">
        <span>🏥 AI-Enhanced EHR System</span>
        <span>•</span>
        <span>Milestone 4 | Streamlit-based EHR Viewer</span>
        <span>•</span>
        <span>© 2026 Healthcare AI Solutions</span>
    </div>
    <p style="margin-top: 0.5rem; font-size: 0.8rem; color: #9ca3af;">
        Powered by AI | Secure & HIPAA Compliant
    </p>
</div>
""", unsafe_allow_html=True)
