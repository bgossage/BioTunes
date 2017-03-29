from Bio import SeqIO
record = SeqIO.read("../data/human_ins.fasta", "fasta")
print record