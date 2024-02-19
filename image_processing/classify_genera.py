from Bio import Entrez, SeqIO
import os
import json

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
input_dir = "/media/chasuelt/MICROBES/microbe_images/"
for dirname in os.listdir(input_dir):
    genus_name = input("Enter genus name: ")
    results[genus_name] = get_taxonomy_info(genus_name)

with open("/media/chasuelt/MICROBES/index.json", "w") as f:
    json.dump(results, f, indent=4)
