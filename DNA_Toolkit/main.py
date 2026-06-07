from DNA_Toolkit import *
from utilities import *
import random 

# generate a random DNA seq, with length of 20
rndDNASeq = "".join([random.choice(Nucleotides) for nuc in range(50)])

print(f'Sequence length: {validateSeq(rndDNASeq)}\n')
print(f'[1] + Sequence length: {len(rndDNASeq)}\n')
print(f'[2] + Nucleotide Frequency: {countNucFrequency(rndDNASeq)}\n')

print(f'[3] + DNA/RNA transcription: {transcription(rndDNASeq)}\n')

print(f"[4] + DNA double strand:\n5'{colored(rndDNASeq)}3'")
print(f"  {''.join('|' for i in range(len(rndDNASeq)))}")
print(f"3'{colored(reverse_complement(rndDNASeq))}5'")

print(f'[5] + GC Content: {gc_content(rndDNASeq)}%\n')
print(f'[6] + GC Content in subsequence k=10: {gc_content_subsec(rndDNASeq, k=5)}\n')

print(f'[7] + Amino acid sequence: {translation(rndDNASeq)}\n')
print(f'[8] + Codon frequency (L): {codon_usage(rndDNASeq, "L")}\n')
print('[9] + Reading_frames:')
frames = []
for frame in gen_reading_frames(rndDNASeq):
    frames.append(frame)
print(frames)

proteins = []
for frame in frames:
    print(frame)
    r = proteins_from_readingframe(frame)
    proteins.append(r)

print(f'[10] + Proteins:{proteins}')