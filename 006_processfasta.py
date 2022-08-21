#!\Users\Azka\Desktop\GenomicDS practice
"""
processfasta.py builds a dictionary with all sequences 
from a FASTA file.
"""
import sys
filename=sys.argv[1]

try:
    f = open("fastafile")
except IOError:
    print("File %s does not exist!!"%filename)
seqs={}
for line in f:
    # let's discard the newline at the end (if any)
    line=line.rstrip() 
    # distinguish header from sequence
    if line[0]=='>': # or line.startswith('>')
        words=line.split()
        name=words[0][1:]
        seqs[name]=""
    else : # sequence, not header
        seqs[name] = seqs[name] + line
f.close()