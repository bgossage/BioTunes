#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 20:21:44 2017

@authors: BYS602 Spring 2017ll
"""

# Python library imports.
import sys
import os
import string
import subprocess

# BioPython module imports.
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


#***********************************************************
#This project contains 2 parts.
#Part I is to convert a DNA sequence into a musical note and play it.\n")
#Part II is to convert a new musical note into DNA and do a sequence alignment in BLAST/NCBI.\n\n")
#***********************************************************\n")
#PART 1 of project follows


###############################################################################

"""
Define a dictionary to map codons to notes..

 Rules for abbreviations: C0 is low C, C1 is middle C, C2 is high C, C3 is highest C, etc.
                          e = eighth note, q = quarter note
    These are determined by the last of the nucleotide triplet, or the wobble position
         if U or A it will be an eighth note
         if C or G it will be a quarter note

  For the key/value pairs: the part before the colon is from codon table,
                           after the colon is the musical note or "stop"
"""
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

##
## Define a function to convert a DNA sequence to musical notes.
##
def dna_to_notes( sequence ):

# Split into codons.
    codon_length = 3
    seq_length = len(seq_record.seq)

    # Account for sequence length when not a multiple of the codon_length.
    seq_range = seq_length-(seq_length%codon_length)

    codons = [str(seq_record.seq[i:i+codon_length]) for i in range(0, seq_range, codon_length)]

    notes = ""

 ## Conversion of Codons to Notes
 ## The codons converted to musical notes are as follows:

    for codon in codons:
        codon = codon.replace('T', 'U')
        note = NoteDictionary[codon]
        notes += note + ' '

    return notes

#end function dna_to_notes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###############################################################################

#PART 2 of project follows


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

###############################################################################

##
## Define a function to translate musical notes in SMF format to an RNA sequence.
##
def translate( musical_notes ):

    RNA = ""
    notes = string.split( musical_notes )
    for note in notes:

            RNA += CodonDictionary[note]

    return RNA

# end function translate ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##
## Define a functions to transform a Simple Music Format (SMF) string to
## a lilypond sheet music file.
##
def transform_to_lilypond( smf_string, filename="sheet_music.ly" ):

    notes = string.split( smf_string )

    with open( filename, "w" ) as output:

    # Write the lilypond header...
        output.write( "\\version \"2.18.2\"\n" )
        output.write( "\\score {\n" )
        output.write( "{\n" )

        lp_note = ""

        for note in notes:
           try:
           # Skip stops...
               if note == 'stop': continue

           # Pitch...
               lp_note = string.lower( note[0] )
           # Octave...
               level = int(note[1])
               lp_note += "\'" * level
           # Duration
               if note[2] == "e": lp_note += "8" # 8 for a eigth note
               if note[2] == "q": lp_note += "4" # 4 for a quarter note
               if note[2] == "h": lp_note += "2" # 2 for a half note
               if note[2] == "w": lp_note += "1" # 1 for a whole note

           # Write the note in lilypond notation...
               output.write( "{:s} ".format( lp_note ) )

           # Clear the note string for the next note...
               lp_note = ""

           except(ValueError) as error:
              msg = str(error) + " for note: " + note
              raise Exception(msg)

    # Write the lilypond footer...
        output.write( "\n}\n" )
        output.write( "\n\\midi { }\n" )
        output.write( "\n\\layout { }\n" )

        output.write( "\n}\n" )

#end transform_to_lilypond ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

################################################################################
############################### MAIN PROGRAM ###################################
################################################################################

# Get the input filename from the command line...
if( len(sys.argv) < 2 ):
    print "Usage: " + sys.argv[0] + "  <fasta file>|<smf file>"
    sys.exit( "Missing Argument" )

input_filename = sys.argv[1]

# Build the output filenames from the input one...
inputfile_root, inputfile_ext = os.path.splitext( input_filename )

smf_filename = ""
musical_notes = ""
valid_input = False

basename = os.path.basename( inputfile_root )
lilypond_filename = basename + ".ly"


# If the input file extension is "fasta", do Part I...
if inputfile_ext == ".fasta":

    valid_input = True

    print "Converting FASTA sequence to music notes..."

   # Read the input FASTA file using BioPython...
    seq_record = SeqIO.read( input_filename, "fasta" )

 # Transform to the DNA to notes...
    musical_notes = dna_to_notes( seq_record.seq )

 # Write the notes an SMF file...
    smf_filename = basename + ".smf"

    print "Writing SMF file: ", smf_filename
    with open( smf_filename, "w" ) as output:
      output.write( musical_notes )

 # We are done with Part I


#end if fasta file ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# If given an input notes file, do Part II...
elif inputfile_ext == ".smf" :

    valid_input = True

    smf_filename = input_filename

    print "Converting Notes to FASTA sequence..."

    with open( input_filename, "r" ) as input_file:
       musical_notes = input_file.read()
   #end with

    RNA = translate( musical_notes )
    DNA = RNA.replace("U","T")

 # Build a BioPython sequence record for output...
    seq_rec = SeqRecord( seq=Seq(DNA),
                         id = basename,
                         description = "musical genome" )
    rec_list = [ seq_rec ]

 # Build the output filename from the input one...
    root, ext = os.path.splitext( input_filename )
    fasta_filename = basename + "_inv.fasta"

 # Write the DNA sequence to a fasta file...
    print "Writing fasta file: ", fasta_filename
    SeqIO.write( rec_list, fasta_filename, "fasta" )

#end if smf file ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if valid_input:

 # Write the notes to a lilypond file...
    lilypond_filename = basename + ".ly"
    transform_to_lilypond( musical_notes, lilypond_filename )

    """
    Set generate_music = True if you have installed the required music generation tools:
      > lilypond (www.lilypond.org) NOTE: configure the path to lilypond accordinly
      > timidity (linux package for .wav sound file from midi file)
      > lame (linux package for mp3 generation) 
    """

    generate_music = True
    if generate_music:
        midi_filename = basename + ".midi"
        mp3_filename = basename + ".mp3"

        lp_cmd = "$HOME/lilypond/usr/bin/lilypond " + lilypond_filename
        subprocess.check_call( lp_cmd, shell=True )
        tm_cmd = "timidity -Ow -o output.wav " + midi_filename
        lm_cmd = "lame -h output.wav " + mp3_filename

        subprocess.check_call( tm_cmd, shell=True )
        subprocess.check_call( lm_cmd, shell=True )

else:
# If we get here, we cannot process the input.
   sys.exit( "Unknown input file type" )


# EOF
