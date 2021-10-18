# BEFORE RUNNING THIS CODE: 
# In workdir, you should put your cds and genome files into folders called cds and genome, separatively. The truncated result would be stored at result folder
# INITIALIZE FILE PATHES, EXPRESSIONS AND ARGUMENTS
# working directory
workdir = "/home/dell/animal_sa/"
# where the cds files put
cds_path = "/home/dell/animal_sa/cds"
# where the genome files put
genome_path = "/home/dell/animal_sa/genome"
result_file_prefix = "result" #the results would be output at result_file_prefix + gene_name folder
# whats the gene or protein name you interest in? - for now only one expression at a time
search_exp = "racE"
# number of bases you want to extend to be shown in the result file? - both before and after
interval = 2000

import re
import os, shutil
cds_files = os.listdir(cds_path)  # get cds file names

# get the reverse complement sequence
def reverse_complement(seq):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    reverse_complement = "".join(complement.get(base, base) for base in reversed(seq))
    return reverse_complement

# initialize parameters
c = 0 # number of found matches of expression
fn = 0 # number of cds file
lengene_all = 0

# iterate all files in cds
for cds_file in cds_files:
    fn += 1
    genome_file = cds_file[:-20] + "genomic.fna"
    file = open(cds_path + "/" + cds_file,"r")
    cds_num = 0
    line_num = 0
    #find if match
    for line in file:
        line_num += 1
        if line.split()[0][0] == ">":
            cds_num = cds_num + 1
            datum = line
            regex= re.search(search_exp, str(datum))
            if regex:
                c += 1
                race_line_start = line_num
                break
    file.close()
    # find the start and end of the gene on the genome
    location = re.search("location=", datum)
    start_loc = location.end()
    location2 = re.search("\.\.", datum)
    start_loc_e = location2.start()
    start_list = re.findall(r"[0-9]", datum[start_loc:start_loc_e])
    start = int(''.join(start_list))
    end_list = re.findall(r"[0-9]", datum[start_loc_e:start_loc_e + 10])
    end = int(''.join(end_list))
    # Which strand have this gene- if it's in complement strand
    comple = re.search("complement", datum)

    #GREP GENE FROM GENOME FILE
    file = open(genome_path + "/" + genome_file,"r")
    genome = []
    for line in file:
        line = line.rstrip('\n')
        if line[0] == ">":
            continue
        genome.append(line)
    genome = "".join(genome)
    file.close()
    lengene_all += end - start + 1
    lenseq = end - start + interval * 2 + 1
    # write the result seq
    result_seq_raw = genome[(start - interval): (end + interval + 1)]
    if comple:
        result_seq_raw = reverse_complement(result_seq_raw)
    # store the result seq into a list of strings
    result_seq = []
    for i in range(lenseq//70):
        result_seq.append(result_seq_raw[(i * 70): (70 + i * 70)])
    if (lenseq % 70) != 0:
        result_seq.append(result_seq_raw[-(lenseq % 70):])
    # create result dictionary
    result_path = workdir + result_file_prefix + "_" + search_exp
    if not os.path.exists(result_path):  # make directory if not exists
        os.makedirs(result_path)
    #else: 
        shutil.rmtree(result_path) # remove all the subdirectories
        os.makedirs(result_path)
    # output the result
    f = open(result_path + "/" + cds_file[:-20] + search_exp + "_result.fasta","w+")
    f.write(">" + cds_file[:-20] + search_exp + "_result\n")
    # write the result in every 70 bases in fasta file
    for i in range(lenseq//70):
        f.write(result_seq[i] + '\n')
    if (lenseq % 70) != 0:
        f.write(result_seq[-1] + '\n')
    f.close
    
print("Find "+str(c) + " " + search_exp + " matches within " + str(fn) + " input cds files! The average length of the targeted gene is: " + str(lengene_all//c) + ". check it!")
