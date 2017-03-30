# -*- coding: utf-8 -*-
"""

@author: Brett
"""

import string
import re

MusicalNotes = 'C1h G0q E1q D1q A0q F1q B0q D1q F1q A1q G1e G1q F1e E1e C2h G1q E1q D1e F1e A1e D2e \
                F2q G2e A2e G0e E1e G1e C2e B1e D2e F2e B1e B1q C2e D2e C2q'

                
# rules for abbreviations, C0 is low C, C1 is middle C, C2 is high C, C3 is highest C, etc.
# rules for abbreviations, e = eighth note, q = quarter note
    # these are determined by the last of the nucleotide triplet, or the wobble position
        # if U or A it will be an eighth note
        # if C or G it will be a quarter note

def transform_to_lilypond( smf_string, filename="sheet_music.ly" ):
    
    notes = string.split( smf_string ) 
    
    with open( filename, "w" ) as output:

        output.write( "\\version \"2.18.2\"\n" )

        output.write( "\\score {\n" )
        output.write( "{\n" )

        lp_note = ""

        for note in notes:
            
           lp_note = string.lower( note[0] )
           
           level = int(note[1])
           lp_note += "\'" * level
           
           
           if note[2] == "e": lp_note += "8"
           if note[2] == "q": lp_note += "4"
           if note[2] == "h": lp_note += "2"
           
           output.write( "{:s} ".format( lp_note ) )
           
           lp_note = ""
           
        output.write( "\n}\n" )
        output.write( "\n\\midi { }\n" )
        output.write( "\n}\n" )
        
#end transform_to_lilypond
        
transform_to_lilypond( MusicalNotes )

## EOF
