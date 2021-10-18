# filter proteins with less than 40 amino acids
import re
from Bio import SeqIO
prot_file = SeqIO.parse("/home/dell/Documents/Projects/MVF-7/membrane_gene_blast/MVF-7_clean.fasta", "fasta")
output = open("/home/dell/Documents/Projects/MVF-7/membrane_gene_blast/MVF-7_clean_","w")
acc_num = 0
c = 0
accession_id = []
for fasta in prot_file:
    acc_num += 1
    name, sequence = fasta.id, str(fasta.seq)
    for i in range(4):
        SeqIO.write(fasta, output + str(i+1), "fasta")
        c += 1
output.close()
print("Overall " + str(acc_num) + " proteins are read.")
print("Left " + str(c) + " protein sequences with more than 40 aa")


