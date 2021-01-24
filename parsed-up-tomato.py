import Bio
from Bio import SeqIO
for seq_record in SeqIO.parse('''C:/Users/salma/Desktop/ACM-Research-Coding-Challenge-S21/Genome.gb''', "genbank"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))

sequence_NT = seq_record
print(sequence_NT.seq )
print("\n\n")
print(sequence_NT)
