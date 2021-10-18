import re
from Bio import SeqIO
# protein list
pmlist = "/home/dell/Documents/Projects/MVF-7/Extracellular_gene/MVF-7_EXTRA_genelist.1"
# find proteins from ..
prot_file = SeqIO.parse("/home/dell/Documents/Projects/MVF-7/Extracellular_gene/MVF-7.fasta", "fasta")
# name the output file
output = open("/home/dell/Documents/Projects/MVF-7/Extracellular_gene/MVF-7_EXTRA.fasta","w")

acc_num = 0
c = 0
accession_id = []
file = open(pmlist, "r")
for line in file:
    acc_num += 1
    line = line.rstrip('\n')
    accession_id.append(line)
for fasta in prot_file:
    name, sequence = fasta.id, str(fasta.seq)
    for id in accession_id:
        if id == fasta.id:
            SeqIO.write(fasta, output, "fasta")
            c += 1
output.close()
print("Successfully read " + str(acc_num) + " plasma membrane related genes from accession list.")
print("Successfully find " + str(c) + " matched genes in protein file")


