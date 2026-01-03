import json
import os

input_dir = "Milestone1/DATA/EHR_Text_Data/EHR_json_entries"
output_dir = "data"
output_file = os.path.join(output_dir, "ehr_processed.json")

merged_data = {}

for file in sorted(os.listdir(input_dir)):
    if file.endswith(".json"):
        with open(os.path.join(input_dir, file), "r", encoding="utf-8") as f:
            content = json.load(f)

        encounter = content.get("encounter", {})
        assessment = encounter.get("assessment", {})
        examination = encounter.get("examination", {})

        # Build a proper clinical note
        clinical_note = (
            f"Chief Complaint: {encounter.get('chief_complaint', '')}\n\n"
            f"History of Present Illness: {encounter.get('history_of_present_illness', '')}\n\n"
            f"Examination Findings: {examination.get('findings_summary', '')}\n\n"
            f"Diagnosis: {assessment.get('diagnosis', '')}\n\n"
            f"Plan: {', '.join(encounter.get('plan', []))}"
        )

        icd_code = assessment.get("icd_10", {}).get("code", "")

        patient_id = content.get("record_id", file.replace("ehr_", "P").replace(".json", ""))

        merged_data[patient_id] = {
            "clinical_note": clinical_note.strip(),
            "icd10": icd_code
        }

os.makedirs(output_dir, exist_ok=True)

with open(output_file, "w", encoding="utf-8") as out:
    json.dump(merged_data, out, indent=2)

print("✅ Clean EHR JSON created for Streamlit app.")
