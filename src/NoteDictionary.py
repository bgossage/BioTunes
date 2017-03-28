#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 20:21:44 2017

@author: vickymcconnell
"""


# rules for abbreviations, C0 is low C, C1 is middle C, C2 is high C, C3 is highest C, etc.
# rules for abbreviations, e = eighth note, q = quarter note, h = half note, w = whole note, these
# are determined by the last of the nucleotide triplet, or the wobble position, if U there will be
# eight note,
# if C there a quarter note, if A there a half note, and if G there a whole note

# below part before the colon is from codon table: after the colon is the musical note
# I have assigned to it
NoteDictionary = {"UUU":"C4e", "UUC":"C4q", "UUA":"D2h", 
                  "UUG":"D2w", "CUU":"D2e", "CUC":"D2q", 
                  "CUA":"D2h", "CUG":"D2w", "AUU":"C2e", 
                  "AUC":"C2q", "AUA":"C2h", "AUG":"A0w",
                  "GUU":"B2e", "GUC":"B2q", "GUA":"B2h", 
                  "GUG":"B2w", "UCU":"E3e", "UCC":"E3q", 
                  "UCA":"E3h", "UCG":"E3w", "CCU":"D1e", 
                  "CCC":"D1q", "CCA":"D1h", "CCG":"D1w", 
                  "ACU":"A2e", "ACC":"A2q", "ACA":"A2h",
                  "ACG":"A2w", "GCU":"A1e", "GCC":"A1q", 
                  "GCA":"A1h", "GCG":"A1w", "UAU":"B0e", 
                  "UAC":"B0q", "UAA":"stop", "UAG":"stop", 
                  "CAU":"B2e", "CAC":"B2q", "CAA":"G1h", 
                  "CAG":"G1w", "AAU":"E1e", "AAC":"E1q", 
                  "AAA":"G2h", "AAG":"G2w", "GAU":"F2e", 
                  "GAC":"F2q", "GAA":"C2h", "GAG":"C2w", 
                  "UGU":"G0e", "UGC":"G0q", "UGA":"stop", 
                  "UGG":"C0w", "CGU":"F1e", "CGC":"F1q", 
                  "CGA":"F1h", "CGG":"F1w", "AGU":"E2e",
                  "AGC":"E2q", "AGA":"F1h", "AGG":"F1w", 
                  "GGU":"B1e", "GGC":"B1q", "GGA":"B1h", 
                  "GGG":"B1h"
                 }

