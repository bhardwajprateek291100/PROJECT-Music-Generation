from music21 import converter, instrument, note, chord, stream
import glob
import pickle
import numpy as np
from keras.utils import np_utils


#### main
def main():
	notes = []
	for file in glob.glob("midi_songs/*.mid"):
	    midi = converter.parse(file) # Convert file into stream.Score Object
	    print("parsing %s"%file)
	    elements_to_parse = midi.flat.notes
	    for ele in elements_to_parse:
		    # If the element is a Note,  then store it's pitch
		    if isinstance(ele, note.Note):
		        notes.append(str(ele.pitch))
		    # If the element is a Chord, split each note of chord and join them with +
		    elif isinstance(ele, chord.Chord):
		        notes.append("+".join(str(n) for n in ele.normalOrder))

	with open("./Files/notes.pkl", "wb") as f:
		pickle.dump(notes, f)


if __name__=="__main__": 
    main() 