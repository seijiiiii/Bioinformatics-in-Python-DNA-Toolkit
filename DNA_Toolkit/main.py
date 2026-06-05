'''
# DNA Toolset/Code testing file

from bio_seq import bio_seq
from utilities import read_FASTA, readTextFile, writeTextFile

test_dna = bio_seq()
test_dna.generate_rnd_seq(40, "RNA")

print(test_dna.get_seq_info())
print(test_dna.nucleotide_frequency())
print(test_dna.transcription())
print(test_dna.reverse_complement())
print(test_dna.gc_content())
print(test_dna.gc_content_subsec())
print(test_dna.translate_seq())
print(test_dna.codon_usage('L'))

for rf in test_dna.gen_reading_frames():
    print(rf)


print(test_dna.all_proteins_from_orfs())
'''

from DNA_Toolkit import *
from utilities import *
import random 

# generate a random DNA seq, with length of 20
rndDNASeq = "".join([random.choice(Nucleotides) for nuc in range(20)])

print(f'Sequence length: {validateSeq(rndDNASeq)}\n')
print(f'[1] + Sequence length: {len(rndDNASeq)}\n')
print(f'[2] + Nucleotide Frequency: {countNucFrequency(rndDNASeq)}\n')

print(f'[3] + DNA/RNA transcription: {transcription(rndDNASeq)}\n')

print(f"[4] + DNA double strand:\n5'{colored(rndDNASeq)}3'")
print(f"  {''.join('|' for i in range(len(rndDNASeq)))}")
print(f"3'{colored(reverse_complement(rndDNASeq))}5'")

print(f'[5] + GC Content: {gc_content(rndDNASeq)}%\n')
print(
    f'[6] + GC Content in subsequence k=10: {gc_content_subsec(rndDNASeq, k=5)}\n')

print(
    f'[7] + Amino acid sequence: {translation(rndDNASeq)}\n'
)
print(f'[8] + Codon frequency (L): {codon_usage(rndDNASeq, "L")}')