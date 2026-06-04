import collections
from structures import *

# Check the sequence to make sure it is a DNA string
def validateSeq(dna_seq):
    temseq = dna_seq.upper()
    for nuc in temseq:
        if nuc not in Nucleotides:
            return False
    return temseq

# Count nucleotide frequency
def countNucFrequency(dna_seq):
    tmpFreqDict = {"A":0, "C":0, "G":0, "T":0}
    for nuc in dna_seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict
    # can also write like this:
    return(dict(collections.Counter(dna_seq)))


def transcription(dna_seq):
    return dna_seq.replace("T","U")

def reverse_complement(seq):
    return("".join(DNA_reverse_complement[nuc] for nuc in seq))[::-1]

    # another method: pythonic method
    # mapping = str.maketrans('ATCG','TAGC')
    # return seq.translate(mapping)[::-1]

def gc_content(seq):
    return round((seq.count('C') + seq.count('G'))/len(seq)*100)

def gc_content_subsec(seq, k=10):
    res = []
    for i in range (0,len(seq)-k+1, k):
        subseq = seq[i:i+k]
        res.append(gc_content(subseq))
    return res

seq = 'ACTGCCGAATA'
