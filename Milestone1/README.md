Milestone 1 — Data Collection & Preprocessing
---------------------------------------------
Milestone 1 focuses on gathering, organizing, and preparing all imaging and clinical datasets required for the AI-powered EHR system.  
The objective is to create a clean, consistent, well-structured dataset used later for:

- Medical image enhancement  
- Clinical note generation  
- ICD-10 prediction  
- Workflow automation  

---------------

1. Data Sources
- Patient records (demographics, medical history)  
- Medical images (X-ray, MRI, CT, ultrasound, DXA)  
- Lab reports (blood tests, pathology reports, diagnostics)  
- Doctor inputs (notes, prescriptions, observations)  
- Public healthcare datasets (optional)  

---------------

2. Purpose of Data Collection
- Store patient data in structured digital format  
- Train AI models for image enhancement  
- Reduce manual documentation errors  
- Enable automated clinical note generation  
- Assist ICD-10 mapping  
- Improve clinical decision-making  

---------------

3. Data Fields
Patient_ID — Unique identifier (e.g., P001)  
Name — Patient's full name  
Age — Age in years  
Gender — Male/Female  
DOB — Date of birth  
Medical_Image — Image path  
Image_Type — X-ray/MRI/CT/etc.  
Lab_Reports — PDF report path  
Diagnosis — Doctor or AI-assisted diagnosis  
Treatment_Plan — Medication/Therapy  
Doctor_Notes — Doctor observations  
Timestamp — Data entry date  
Data_Status — Verified/AI-Predicted  

---------------

4. Data Formats
- Text: Name, Gender, Diagnosis, Doctor Notes  
- Numeric: Age, Patient ID  
- Date/Time: DOB, Timestamp  
- Files: Medical Images (JPG/PNG), Reports (PDF)  

---------------

5. Data Cleaning & Preprocessing
- Removed duplicate entries  
- Corrected DOB/age mismatches  
- Filled missing fields with NA  
- Standardized naming (PatientID_ImageType_Date)  
- Linked images and reports to Patient_ID  
- Normalized text fields  
- Organized dataset into structured folders  

---------------

6. Metadata Codes
NA — Data not available  
AI-Predicted — Suggested by AI  
Verified — Clinician-validated   

Dataset Credibility Statement
-----------------------------
The dataset used in this milestone is prepared using:

- Hospital-style patient record structures  
- Publicly available medical imaging datasets  
- Standardized EHR formats used in clinical settings  
- Lab report formats used in medical environments  

These datasets were created solely for academic, training, and demonstration purposes, following documentation guidelines provided.


Milestone 1 Summary
-------------------
- All imaging and clinical data collected  
- Cleaned, standardized, and labeled  
- Dataset structured for AI model training  
- Ready for image enhancement & documentation automation  

Contributors
------------
- Manasvi Bhaskar  
- Abhishek Kanoujiya
- M.Navya Sri 
- Naveen Sannena
- Sneha Raghuwanshi
- Bhawana
- Lokesh
- Naveen Kumar
- Ayush 
- Sai teja

