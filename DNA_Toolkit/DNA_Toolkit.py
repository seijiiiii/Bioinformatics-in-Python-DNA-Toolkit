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

def translation(seq, init_pos=0):
    return [DNA_Codons[seq[pos:pos+3]] for pos in range(init_pos, len(seq)-2, 3)]

def codon_usage(seq, aminoacid):
    tmplist = []
    for i in range(0, len(seq)-2, 3):
        if DNA_Codons[seq[i:i+3]] == aminoacid:
            tmplist.append(seq[i:i+3])

    freqDict = dict(collections.Counter(tmplist))
    totalWight = sum(freqDict.values())
    for seq in freqDict:
        freqDict[seq] = round(freqDict[seq]/totalWight, 2)
    return freqDict

def gen_reading_frames(seq):
    frames = []
    frames.append(translation(seq, 0))
    frames.append(translation(seq, 1))
    frames.append(translation(seq, 2))
    # frames.append(translation(reverse_complement(seq), 0))
    # frames.append(translation(reverse_complement(seq), 1))
    # frames.append(translation(reverse_complement(seq), 2))
    return frames

def proteins_from_readingframe(aa_seq):
    tmp_proteins = []
    proteins = []
    for aa in aa_seq:
        if aa == "_":
            if tmp_proteins:
                for p in tmp_proteins:
                    proteins.append(p)
                tmp_proteins = []
        else:
            if aa == "M":
                tmp_proteins.append("")
            for j in range(len(tmp_proteins)):
                tmp_proteins[j-1] += aa
    return proteins

def all_proteins_from_orfs(seq, startReadPos=0, stopReadPos=0, order=False):
    if startReadPos < stopReadPos:
        rfs = gen_reading_frames(seq[startReadPos:stopReadPos])
    else:
        rfs = gen_reading_frames(seq)
    res = []
    for rf in rfs:
        proteins = proteins_from_readingframe(rf)
        for p in proteins:
            res.append(p)  

    if order:
        return sorted(res, key=len, reverse=True)
    return res
