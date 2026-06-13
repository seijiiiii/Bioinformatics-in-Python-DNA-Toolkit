from DNA_Toolkit import *
from utilities import *
import random 

# generate a random DNA seq, with length of 20
DNA_seq = "".join([random.choice(Nucleotides) for nuc in range(50)])

print(f'Sequence length: {validateSeq(DNA_seq)}\n')
print(f'[1] + Sequence length: {len(DNA_seq)}\n')
print(f'[2] + Nucleotide Frequency: {countNucFrequency(DNA_seq)}\n')

print(f'[3] + DNA/RNA transcription: {transcription(DNA_seq)}\n')

print(f"[4] + DNA double strand:\n5'{colored(DNA_seq)}3'")
print(f"  {''.join('|' for i in range(len(DNA_seq)))}")
print(f"3'{colored(reverse_complement(DNA_seq))}5'")

print(f'[5] + GC Content: {gc_content(DNA_seq)}%\n')
print(f'[6] + GC Content in subsequence k=10: {gc_content_subsec(DNA_seq, k=5)}\n')

print(f'[7] + Amino acid sequence: {translation(DNA_seq)}\n')
print(f'[8] + Codon frequency (L): {codon_usage(DNA_seq, "L")}\n')
print('[9] + Reading_frames:')
for frame in gen_reading_frames(DNA_seq):
    print(frame)

print(f'[10] + Proteins:')
for p in all_proteins_from_orfs(DNA_seq, 0,0,True):
    print(f'{p}')
