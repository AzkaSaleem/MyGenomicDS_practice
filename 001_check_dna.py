#!\Users\Azka\Desktop\GenomicDS practice

dna=input('Enter DNA sequence:')

if 'n' in dna :
        nbases=dna.count('n')
        print("dna sequence has %d undefined bases " % nbases)
else:
        print("dna sequence has no undefined bases")