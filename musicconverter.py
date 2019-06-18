notes = ['c','cs','d','eb','e','f','fs','g','ab','a','bb','b']
guitarTune = ['e4', 'b3', 'g3', 'd3', 'a2', 'e2']
banjoTune  = ['d4','b3','g3','d3','g5']

#convert the input file into a 2d list containing all the notes (each sublist is a string)
def generateArray(instrument, file):
	if(instrument.lower() == 'guitar'):
		strings = [[],[],[],[],[],[]]
		i = 0
		for line in file:
			for x in line:
				if(x.isdigit() or x == '-' or x == 'h' or x == 'p'):
					strings[i].append(x)
			i = i + 1
			if(i >= 6):
				i = 0
	elif(instrument.lower() == 'banjo'):
		strings = [[],[],[],[],[]]
		i = 0
		for line in file:
			for x in line:
				if(x.isdigit() or x == '-' or x == 'h' or x == 'p'):
					strings[i].append(x)
			i = i + 1
			if(i >= 6):
				i = 0
	else:
		print "Instrument not currently supported"
	return(strings)

#returns -1 if note1 is lower, 0 if the same, 1 if note2 is higher
def compare(note1, note2):
	semi1 = note1[0:len(note1)-1]
	oct1 = int(note1[len(note1)-1])
	semi2 = note2[0:len(note2)-1]
	oct2 = int(note2[len(note2)-1])
	if(notes.index(semi1) == notes.index(semi2) and oct1 == oct2):
		return 0
	elif(oct1 < oct2 or (oct1 == oct2 and notes.index(semi1) < notes.index(semi2))):
		return -1
	return 1

#increase the input note the amount of half steps specified
#this is used both for translating tabs and for generating notes
#(i.e. add fret to open tune)
def increase(innote, halfsteps):
	note = innote[0:len(innote)-1]
	octave = int(innote[len(innote)-1])
	i = notes.index(note)
	i += halfsteps
	while(i >= len(notes)):
		i -= len(notes)
	newOctave = octave + halfsteps*1.0/12 + notes.index(note)*1.0/12
	return(notes[i] + str(int(newOctave)))

#convert the tab into a series of notes
def convertToNotes(instrument, inputTab):
	noteTab = inputTab
	if(instrument.lower() == "guitar"):
		for i in range(0,len(guitarTune)):
			for j in range(0,len(inputTab[i])):
				if(inputTab[i][j].isdigit()):
					noteTab[i][j] = increase(guitarTune[i],int(inputTab[i][j]))
	return noteTab

#find the loewst note in the tab (used for rescaling tab)
def findLowestNote(noteTab):
	lowNote = 'e6'
	for string in noteTab:
		for note in string:
			if(note != 'p' and note != 'h' and note != '-' and compare(lowNote,note) == 1):
				lowNote = note
	return lowNote

#gets input runs code
def runCode():
	file = open(raw_input("Please specify file name:"),'r')
	original = raw_input("Please specify original instrument:")
	novel = raw_input("Please specify new instrument:")
	inputTab =  generateArray(original, file)
	ignoreNotes = raw_input("Ignore out of range notes?")
	noteTab = convertToNotes(original, inputTab)

	if(ignoreNotes.lower() ==  "no" or ignoreNotes.lower() ==  "n"):
		lowNote = findLowestNote(noteTab)
	elif(ignoreNotes.lower() ==  "yes" or ignoreNotes.lower() ==  "y"):
		#todo
	else:
		print "Input not recognized."
		return

runCode()