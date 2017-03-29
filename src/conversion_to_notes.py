# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 11:46:43 2017

@author: Spencer
"""

from Bio import SeqIO

NoteDictionary = {"TTT":"C4e", "TTC":"C4q", "TTA":"D2h", 
                  "TTG":"D2w", "CTT":"D2e", "CTC":"D2q", 
                  "CTA":"D2h", "CTG":"D2w", "ATT":"C2e", 
                  "ATC":"C2q", "ATA":"C2h", "ATG":"A0w",
                  "GTT":"B2e", "GTC":"B2q", "GTA":"B2h", 
                  "GTG":"B2w", "TCT":"E3e", "TCC":"E3q", 
                  "TCA":"E3h", "TCG":"E3w", "CCT":"D1e", 
                  "CCC":"D1q", "CCA":"D1h", "CCG":"D1w", 
                  "ACT":"A2e", "ACC":"A2q", "ACA":"A2h",
                  "ACG":"A2w", "GCT":"A1e", "GCC":"A1q", 
                  "GCA":"A1h", "GCG":"A1w", "TAT":"B0e", 
                  "TAC":"B0q", "TAA":"stop", "TAG":"stop", 
                  "CAT":"B2e", "CAC":"B2q", "CAA":"G1h", 
                  "CAG":"G1w", "AAT":"E1e", "AAC":"E1q", 
                  "AAA":"G2h", "AAG":"G2w", "GAT":"F2e", 
                  "GAC":"F2q", "GAA":"C2h", "GAG":"C2w", 
                  "TGT":"G0e", "TGC":"G0q", "TGA":"stop", 
                  "TGG":"C0w", "CGT":"F1e", "CGC":"F1q", 
                  "CGA":"F1h", "CGG":"F1w", "AGT":"E2e",
                  "AGC":"E2q", "AGA":"F1h", "AGG":"F1w", 
                  "GGT":"B1e", "GGC":"B1q", "GGA":"B1h", 
                  "GGG":"B1h"
                 }


record = SeqIO.read("../data/human_ins.fasta", "fasta")

n = 3
Codons = [record.seq[i:i+n] for i in range(0, len(record.seq), n)] #Splits into codons.

NoteList = []

for x in Codons:
    NoteList.append( NoteDictionary[x] )
