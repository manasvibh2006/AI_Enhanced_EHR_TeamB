def map_icd10(diagnosis):
    icd10_map = {
        "Pneumonia": "J18.9",
        "Diabetes": "E11.9",
        "Hypertension": "I10",
        "Asthma": "J45.909",
        "COVID-19": "U07.1"
    }
    return icd10_map.get(diagnosis, "Code Not Available")
