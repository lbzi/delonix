import re
from Bio import SeqIO
# protein list
pmlist = "/home/dell/Documents/Projects/MVF-7//Extracellular_gene/Newman_EXTRA_genelist.1"
# find proteins from ..
gb_file = "/home/dell/Documents/Projects/MVF-7//Extracellular_gene/Newman.gbk"
gb_record = SeqIO.read(open(gb_file,"r"), "genbank")
# name the output file
output = open("/home/dell/Documents/Projects/MVF-7//Extracellular_gene/Newman_EXTRA.gbk","w")

c = 0
cds_num = 0
pm_num = 0
accession_id = []
file = open(pmlist, "r")
for line in file:
    pm_num += 1
    line = line.rstrip('\n')
    accession_id.append(line)

for id in accession_id:
    print("Processing " + id + " ...")
    for feature in gb_record.features:
        if feature.type == "CDS":
           if re.search(id, str(feature.qualifiers.get("protein_id"))):
              c += 1
              gb_record.features.append(feature)
              break

# save as genbank file
SeqIO.write(gb_record, output, 'genbank')
output.close()

print("Successfully read " + str(pm_num) + " plasma membrane related genes from accession list.")
print("Successfully find " + str(c) + " matched cds features in gbk file")


