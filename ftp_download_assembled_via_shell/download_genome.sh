#! /bin/bash
# rsync using variables

## INITILIZE:
# PLEASE SET OUTPUT DIRECTORY
OUTPUTDIR=/home/dell/human_sa_genome  
# PLEASE SET A LIST OF FTP LINKS
# WARNING: you should leave a line on the botton of the ftp list, otherwise the final line won't be read!!!
FTPLIST=/home/dell/Documents/code/ftp_download_assembled_via_shell/ftp_list_example 

# creat output directory
if [ ! -d $OUTPUTDIR ]; then
    mkdir $OUTPUTDIR
    echo Successfully make a new output directory!
else
    echo Output directory exist
fi
# delete all the prefix 'ftp:' in the file list
sed 's/....//' $FTPLIST | while read line
do
    FTPNAME=$line
    echo $line
    # It's time to download the assembled data!:)
    rsync --copy-links --recursive --times --verbose rsync:$FTPNAME/*[^from]_genomic.fna.gz $OUTPUTDIR
done
# Unzip all the files at once
gzip -d $OUTPUTDIR/*.gz