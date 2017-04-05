#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 20:21:44 2017

@authors: BYS602 Spring 2017ll
"""

import sys

from Bio import SeqIO

import lilypond

input_filename = "../data/human_ins.fasta"

# If provided, use the filename from the command line arg...
if( len(sys.argv) > 1 ):
   input_filename = sys.argv[1] 


###############################################################################


infile = SeqIO.read( input_filename, "fasta" )
OutFile = "outfile.txt"
#Deactivate the above line and activate the below line if you wish to output the path of the fasta file in the terminal
#OutFile = input(">")
outfile = open(OutFile,"w")

outfile.write("***********************************************************\n\n")
outfile.write("This project contains 2 parts.\n")
outfile.write("Part I is to convert a DNA sequence into a musical note and play it.\n")
outfile.write("Part II is to convert a new musical note into DNA and do a sequence alignment in BLAST/NCBI.\n\n")
outfile.write("***********************************************************\n")
#PART 1 of project follows
outfile.write("PART I: \n")
outfile.write("***********************************************************\n\n")
outfile.write("Fasta file has the following information:\n\n")
outfile.write(str(infile))
outfile.write("\n\n***********************************************************\n")

###############################################################################

# rules for abbreviations, C0 is low C, C1 is middle C, C2 is high C, C3 is highest C, etc.
# rules for abbreviations, e = eighth note, q = quarter note
    # these are determined by the last of the nucleotide triplet, or the wobble position
        # if U or A it will be an eighth note
        # if C or G it will be a quarter note

# below part before the colon is from codon table: after the colon is the musical note

NoteDictionary = {"UUU":"C0e", "UUC":"C0q", "UUA":"G0e", 
                  "UUG":"G0q", "CUU":"C1e", "CUC":"C1q", 
                  "CUA":"C2e", "CUG":"C2q", "AUU":"A1e", 
                  "AUC":"A1q", "AUA":"B0e", "AUG":"B0q",
                  "GUU":"A2e", "GUC":"A2q", "GUA":"B2e", 
                  "GUG":"B2q", "UCU":"D0e", "UCC":"D0q", 
                  "UCA":"A0e", "UCG":"A0q", "CCU":"D1e", 
                  "CCC":"D1q", "CCA":"D2e", "CCG":"D2q", 
                  "ACU":"G3e", "ACC":"G3q", "ACA":"A3e",
                  "ACG":"A3q", "GCU":"B1e", "GCC":"B1q", 
                  "GCA":"F3e", "GCG":"F3q", "UAU":"E0e", 
                  "UAC":"E0q", "UAA":"stop", "UAG":"stop", 
                  "CAU":"E1e", "CAC":"E1q", "CAA":"E2e", 
                  "CAG":"E2q", "AAU":"B3e", "AAC":"B3q", 
                  "AAA":"C4e", "AAG":"C4q", "GAU":"D3e", 
                  "GAC":"D3q", "GAA":"E3e", "GAG":"E3q", 
                  "UGU":"F0e", "UGC":"F0q", "UGA":"stop", 
                  "UGG":"C1h", "CGU":"F1e", "CGC":"F1q", 
                  "CGA":"G1e", "CGG":"G1q", "AGU":"F2e",
                  "AGC":"F2q", "AGA":"G2e", "AGG":"G2q", 
                  "GGU":"C3e", "GGC":"C3q", "GGA":"A4q", 
                  "GGG":"B4q"
                 }
###############################################################################

outfile.write("\nThe NoteDictionary used is \n\n")
outfile.write(str(NoteDictionary))
ndl = len(NoteDictionary)
outfile.write("\n\nThe length of the NoteDictionary is ")
outfile.write(str(ndl)) 
outfile.write("\n\n***********************************************************\n")

n = 3
m = [str(infile.seq[i:i+n]) for i in range(0, len(infile.seq)- (len(infile.seq)%3), n)] #Splits into codons.
outfile.write("\nThe codons are \n\n")
outfile.write(str(m))
outfile.write("\n\nThe number of codons available in the input sequence is ")
outfile.write(str(len(m)))
outfile.write("\n\n***********************************************************\n\n")

###############################################################################

#Conversion of Codons to Notes
outfile.write("The codons converted to musical notes are as follows: \n\n")
for codon in m:
    codon = codon.replace('T', 'U')
    outfile.write(NoteDictionary[codon] + ' ')
    

outfile.write("\n\n***********************************************************\n")

###############################################################################            

#PART 2 of project follows
outfile.write("PART II: \n")
outfile.write("***********************************************************\n\n")

#Back coding Dictionary - from notes to DNA
CodonDictionary = {'G3q': 'ACC', 'A4q': 'GGA', 'C2q': 'CUG',
                   'B0e': 'AUA', 'E2q': 'CAG', 'D0q': 'UCC',
                   'D2q': 'CCG', 'G1e': 'CGA', 'E2e': 'CAA',
                   'C0e': 'UUU', 'E0q': 'UAC', 'B0q': 'AUG',
                   'F3q': 'GCG', 'D0e': 'UCU', 'B1e': 'GCU',
                   'G3e': 'ACU', 'C2e': 'CUA', 'C0q': 'UUC',
                   'B4q': 'GGG', 'E0e': 'UAU', 'D2e': 'CCA',
                   'G1q': 'CGG', 'F3e': 'GCA', 'A2q': 'GUC',
                   'F1q': 'CGC', 'E3q': 'GAG', 'F1e': 'CGU',
                   'C3q': 'GGC', 'A0q': 'UCG', 'B2q': 'GUG',
                   'C3e': 'GGU', 'E3e': 'GAA', 'A2e': 'GUU',
                   'B2e': 'GUA', 'A0e': 'UCA', 'F0e': 'UGU',
                   'C1h': 'UGG', 'D1q': 'CCC', 'F2e': 'AGU',
                   'G2q': 'AGG', 'E1q': 'CAC', 'G0e': 'UUA',
                   'stop': 'UGA','C1e': 'CUU', 'D3q': 'GAC',
                   'D1e': 'CCU', 'F2q': 'AGC', 'G2e': 'AGA',
                   'F0q': 'UGC', 'B1q': 'GCC', 'C1q': 'CUC',
                   'D3e': 'GAU', 'E1e': 'CAU', 'G0q': 'UUG',
                   'C4q': 'AAG', 'A3q': 'ACG', 'A1q': 'AUC',
                   'C4e': 'AAA', 'B3q': 'AAC', 'A1e': 'AUU',
                   'A3e': 'ACA', 'B3e': 'AAU'}

MusicalNote = 'C1q G0q E1q D1q A0q F1q B0q D1q F1q A1q G1e G1q F1e E1e C2q G1q E1q D1e F1e A1e D2e F2q G2e A2e G0e E1e G1e C2e B1e D2e F2e B1e B1q C2e D2e C2q'
outfile.write("The Musical Note given for part 2 of the project is \n\n")
outfile.write(MusicalNote)
outfile.write("\n\n")
MusicalNote = MusicalNote.replace(" ","")

###############################################################################

#Definition to back code
def translate(MusicalNote):
    RNA = ""
    for i in range(0,len(MusicalNote),3):
        if MusicalNote[i:i+3] != 'sto' and MusicalNote[i:i+3] != 'pst' and MusicalNote[i:i+3] != 'ops' and MusicalNote[i:i+3] != 'top':
            codon = MusicalNote[i:i+3]
            RNA += CodonDictionary[codon] + " "
        else:
            for j in range(i,len(MusicalNote),4):
                if MusicalNote[j:j+4] == 'stop':
                    codon = MusicalNote[j:j+4]
                    RNA += CodonDictionary[codon] + " "
    return RNA

RNA = translate(MusicalNote)
DNA = RNA.replace("U","T").replace(' ','')
outfile.write("The DNA sequence encoded by the musical note is \n\n")
outfile.write(DNA)
outfile.write("\n\n***********************************************************\n")

###############################################################################

outfile.close()

lilypond.transform_to_lilypond( MusicalNote )


