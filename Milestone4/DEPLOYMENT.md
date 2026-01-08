# AI-Enhanced EHR System - Deployment Guide

## Project Structure for Deployment

```
Milestone4/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── .streamlit/
│   └── config.toml                # Streamlit configuration
├── Data/
│   └── ehr_processed.json         # Patient EHR data
└── Images/
    └── ehr_processedimages/       # Medical images
```

## Deployment Steps

### Step 1: Prepare Your GitHub Repository

```bash
cd C:\Users\Manasvi\OneDrive\Desktop\AI Enhanced ehr - final1\AI_Enhanced_EHR_TeamB
git add .
git commit -m "Add Streamlit deployment configuration"
git push origin main
```

### Step 2: Deploy on Streamlit Cloud

1. Go to **https://share.streamlit.io**
2. Click **"New app"**
3. Sign in with your GitHub account
4. Select your repository
5. Set the following details:
   - **Repository**: `AI_Enhanced_EHR_TeamB` (or your repo name)
   - **Branch**: `main`
   - **Main file path**: `Milestone4/app.py`
6. Click **Deploy**

### Step 3: Wait for Deployment

Your app will be live in 2-5 minutes! You'll get a public URL like:
```
https://aienhancedehrteamb-tjlu7ezaqcy94sgwnecrhc.streamlit.app/
```

## Important Notes

### ✅ What's Included
- Landing page with feature cards
- Dashboard with patient EHR data
- Medical imaging viewer
- Responsive design
- Navy blue (#000080) theme for readability

### ⚠️ Data Requirements
Make sure these files are in your repository:
- `Data/ehr_processed.json` - Patient records
- `Images/ehr_processedimages/` - Medical images with patient ID naming

### 🔧 Configuration Files Created
- **requirements.txt** - All Python dependencies
- **.streamlit/config.toml** - Theme and server settings

### 📱 Features on Deployment
1. **Landing Page**: Beautiful intro with feature highlights
2. **Dashboard**: Full EHR interface with:
   - Patient selection
   - Clinical summaries
   - Medical imaging
   - Raw JSON data download
3. **Navigation**: Seamless page switching

## Environment Variables (Optional)

If you need secrets/API keys, create a `.streamlit/secrets.toml` file:
```toml
[database]
url = "your_database_url"
api_key = "your_api_key"
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Data files not found | Ensure `Data/` and `Images/` folders are in repo |
| Images not loading | Check image paths and filenames in app.py |
| Slow deployment | It may take 5-10 minutes on first deploy |

## Need Help?

- Streamlit Docs: https://docs.streamlit.io
- Streamlit Community: https://discuss.streamlit.io

---

**Your app is ready to deploy! 🚀**
