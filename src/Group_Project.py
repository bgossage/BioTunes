#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 20:21:44 2017

@authors: BYS602 Spring 2017ll
"""

import numpy as np
import scipy as sp
from Bio import SeqIO

###############################################################################

InFile = "../data/human_ins.fasta"
#Deactivate the above line and activate the below line if you wish to input the path of the fasta file in the terminal
#InFile = input(">")
infile = SeqIO.read(InFile, "fasta")
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
                  "CUA":"C1e", "CUG":"C1q", "AUU":"A1e", 
                  "AUC":"A1q", "AUA":"B0e", "AUG":"B0q",
                  "GUU":"A2e", "GUC":"A2q", "GUA":"B2e", 
                  "GUG":"B2q", "UCU":"D0e", "UCC":"D0q", 
                  "UCA":"A0e", "UCG":"A0q", "CCU":"D1e", 
                  "CCC":"D1q", "CCA":"D1e", "CCG":"D1q", 
                  "ACU":"C2e", "ACC":"C2q", "ACA":"C2e",
                  "ACG":"C2q", "GCU":"B1e", "GCC":"B1q", 
                  "GCA":"F3e", "GCG":"F3q", "UAU":"E0e", 
                  "UAC":"E0q", "UAA":"stop", "UAG":"stop", 
                  "CAU":"E1e", "CAC":"E1q", "CAA":"E1e", 
                  "CAG":"E1q", "AAU":"D2e", "AAC":"D2q", 
                  "AAA":"E2e", "AAG":"E2q", "GAU":"D3e", 
                  "GAC":"D3q", "GAA":"E3e", "GAG":"E3q", 
                  "UGU":"F0e", "UGC":"F0q", "UGA":"stop", 
                  "UGG":"C1q", "CGU":"F1e", "CGC":"F1q", 
                  "CGA":"G1e", "CGG":"G1q", "AGU":"F2e",
                  "AGC":"F2q", "AGA":"G2e", "AGG":"G2q", 
                  "GGU":"C3e", "GGC":"C3q", "GGA":"C3e", 
                  "GGG":"C3q"}

###############################################################################

outfile.write("\nThe NoteDictionary used is \n\n")
outfile.write(str(NoteDictionary))
ndl = len(NoteDictionary)
outfile.write("\n\nThe length of the NoteDictionary is ")
outfile.write(str(ndl)) 
outfile.write("\n\n***********************************************************\n")

n = 3
m = [infile.seq[i:i+n] for i in range(0, len(infile.seq), n)] #Splits into codons.
outfile.write("\nThe codons are \n\n")
outfile.write(str(m))
outfile.write("\n\nThe number of codons available in the input sequence is ")
outfile.write(str(len(m)))
outfile.write("\n\n***********************************************************\n\n")

###############################################################################

#Conversion of Codons to Notes
outfile.write("The codons converted to musical notes are as follows: \n\n")
for y in NoteDictionary:
    for x in m:
        if x == y:
            for t in NoteDictionary[y]:
                outfile.write(' '.join(str(s) for s in t) + ' ')
            outfile.write(str(NoteDictionary[y])) #OutFile is whatever you want the output file name to be. Change as you see fit.
outfile.write("\n\n***********************************************************\n")

###############################################################################            

#PART 2 of project follows
outfile.write("PART II: \n")
outfile.write("***********************************************************\n\n")

#Back coding Dictionary - from notes to DNA
CodonDictionary = {"C4e":"UUU", "C4q":"UUC", "D2h":"UUA",
                   "D2w":"UUG", "D2e":"CUU", "D2q":"CUC",
                   "D2h":"CUA", "D2w":"CUG", "C2e":"AUU",
                   "C2q":"AUC", "C2h":"AUA", "A0w":"AUG",
                   "B2e":"GUU", "B2q":"GUC", "B2h":"GUA",
                   "B2w":"GUG", "E3e":"UCU", "E3q":"UCC",
                   "E3h":"UCA", "E3w":"UCG", "D1e":"CCU",
                   "D1q":"CCC", "D1h":"CCA", "D1w":"CCG",
                   "A2e":"ACU", "A2q":"ACC", "A2h":"ACA",
                   "A2w":"ACG", "A1e":"GCU", "A1q":"GCC",
                   "A1h":"GCA", "A1w":"GCG", "B0e":"UAU",
                   "B0q":"UAC", "stop":"UAA", "stop":"UAG",
                   "B2e":"CAU", "B2q":"CAC", "G1h":"CAA", 
                   "G1w":"CAG", "E1e":"AAU", "E1q":"AAC",
                   "G2h":"AAA", "G2w":"AAG", "F2e":"GAU",
                   "F2q":"GAC", "C2h":"GAA", "C2w":"GAG",
                   "G0e":"UGU", "G0q":"UGC", "stop":"UGA",
                   "C0w":"UGG", "F1e":"CGU", "F1q":"CGC",
                   "F1h":"CGA", "F1w":"CGG", "E2e":"AGU",
                   "E2q":"AGC", "F1h":"AGA", "F1w":"AGG",
                   "B1e":"GGU", "B1q":"GGC", "B1h":"GGA",
                   "B1h":"GGG"}

MusicalNote = "A0w A1e A1h A1q A1w A2e A2h A2q A2w B0e B0q B1e B1h B1h B1q B2e B2e B2h B2q B2q B2w C0w C2e C2h C2h C2q C2w C4e C4q D1e D1h D1q D1w D2e D2h D2h D2q D2w D2w E1e E1q E2e E2q E3e E3h E3q E3w F1e F1h F1h F1q F1w F1w F2e F2q G0e G0q G1h G1w G2h G2w stop stop stop"
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
DNA = RNA.replace("U","T")
outfile.write("The DNA sequence encoded by the musical note is \n\n")
outfile.write(DNA)
outfile.write("\n\n***********************************************************\n")

###############################################################################

outfile.close()