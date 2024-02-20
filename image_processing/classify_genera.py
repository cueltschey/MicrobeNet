from Bio import Entrez, SeqIO
import os
import json
import time

def get_taxonomy_info(genus_name):
    Entrez.email = "chaseuelt@gmail.com"  # Enter your email here
    handle = Entrez.esearch(db="taxonomy", term=genus_name)
    record = Entrez.read(handle)
    if record['Count'] == '0':
        print(f"Genus {genus_name} not found.")
        return {"superkingdom": "None"}
    genus_id = record['IdList'][0]
    handle = Entrez.efetch(db="taxonomy", id=genus_id, retmode="xml")
    taxonomy = Entrez.read(handle)
    lineage = taxonomy[0]['LineageEx']
    result = dict()
    for info in lineage:
        result[info["Rank"]] = info["ScientificName"]
    return result

results = dict()
input_dir = "/home/chasuelt/Desktop/Backup_Images/"
for genus_name in os.listdir(input_dir):
    try:
        print(genus_name)
        time.sleep(0.3)
        results[genus_name] = get_taxonomy_info(genus_name)
        print(results[genus_name])
    except:
        continue

with open("/media/chasuelt/MICROBES/index.json", "w") as f:
    json.dump(results, f, indent=4)
