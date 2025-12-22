import json
from icd10_mapper import map_icd10

with open("module3_processed_ehr.json") as f:
    patients = json.load(f)

for patient in patients:
    patient["icd10_code"] = map_icd10(patient["diagnosis"])

with open("module3_output.json", "w") as f:
    json.dump(patients, f, indent=4)

print("Module 3 completed for 10 patients.")
