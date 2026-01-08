# AI‑Enhanced EHR Imaging & Documentation System

## Milestone 4 – Streamlit‑Based EHR Dashboard

---

## Project Overview

Milestone 4 focuses on the implementation of a web‑based Electronic Health Record (EHR) dashboard using Streamlit.

The objective of this milestone is to integrate outputs generated from previous milestones—such as enhanced medical images, structured clinical summaries, and ICD‑10 codes—into a single interface for patient record visualization.

---

## Scope of Milestone 4

This milestone implements a browser‑based EHR interface that allows users to view and interact with patient clinical data in a structured and organized manner.

The system integrates clinical text data and medical imaging outputs and presents them through an interactive dashboard.

---

## Functionalities Implemented

### Patient Selection
- Dropdown‑based selection of patient records (e.g., `EHR_01`, `EHR_02`)
- Dynamic loading of patient‑specific information

### Clinical Summary View
Displays structured clinical information including:
- Chief Complaint  
- Medical History  
- Diagnosis  
- Treatment Plan  
- ICD‑10 Code  

Data is sourced from processed EHR records.

### Medical Imaging View
- Displays enhanced medical images generated in earlier milestones
- Fallback handling when an image is not linked to a patient record

### Raw EHR Data View
- Displays raw EHR data in JSON format
- Enables inspection of underlying patient information

---

## Folder Structure

Milestone4/
│
├── app.py # Streamlit application

├── Data/
│ └── ehr_processed.json # Processed EHR records

├── Images/
│ └── enhanced/ # Enhanced medical images

├── README.md # Milestone 4 documentation



## Technology Stack

- Python 3  
- Streamlit (Web Interface Framework)  
- JSON (EHR Data Representation)  
- Pillow (Image Handling)

---

## Execution Instructions

### Step 1: Install Dependencies
pip install streamlit pillow
### Step 2: Navigate to Milestone 4 Directory
cd Milestone4
### Step 3: Run the Application
streamlit run app.py
### Step 4: Access via Browser
https://aienhancedehrteamb-tjlu7ezaqcy94sgwnecrhc.streamlit.app/

# Milestone Status
Milestone 1: Data Collection and Preprocessing – Completed

Milestone 2: Medical Image Enhancement – Completed

Milestone 3: Clinical Note Generation and ICD‑10 Mapping – Completed

Milestone 4: Streamlit‑Based EHR Interface – Completed

# Team – Team B
Manasvi Bhaskar

Abhishek Kanoujiya

M. Navya Sri

Naveen Sannena

Naveen Kumar

Sneha Raghuwanshi

Bhawana

Lokesh

Sai Teja

# Conclusion
Milestone 4 demonstrates the integration of enhanced medical imaging and structured clinical data into a Streamlit‑based EHR dashboard.

The implementation consolidates outputs from earlier milestones into a unified interface, completing the end‑to‑end workflow of the system.

