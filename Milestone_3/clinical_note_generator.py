import json
from icd10_mapper import map_icd10

def generate_clinical_note(ehr):
    return f"""
Patient ID: {ehr['patient_id']}
Age/Gender: {ehr['age']} / {ehr['gender']}

Symptoms:
{', '.join(ehr['symptoms'])}

Doctor Observations:
{ehr['doctor_observations']}

Vitals:
BP: {ehr['vitals']['bp']}
Heart Rate: {ehr['vitals']['heart_rate']}

Assessment:
Diagnosed with {ehr['diagnosis']} (ICD-10: {map_icd10(ehr['diagnosis'])})

Plan:
Follow-up and appropriate treatment advised.
"""

with open("module2_processed_ehr.json") as f:
    patients = json.load(f)

for patient in patients:
    print(generate_clinical_note(patient))

