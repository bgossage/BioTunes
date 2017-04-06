# -*- coding: utf-8 -*-
"""

@author: Brett
"""

import string

##
## Transform a Simple Music Format (SMF) string to lilypond sheet music file.
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
               if note[2] == "e": lp_note += "8"
               if note[2] == "q": lp_note += "4"
               if note[2] == "h": lp_note += "2"

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

#end transform_to_lilypond

#transform_to_lilypond( MusicalNotes )




## EOF
