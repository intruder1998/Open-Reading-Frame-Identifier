
def seq_reader(file):
    """
    Function 1: seq_reader
    :param file:
    :return: sequence
    Usage: To read FASTA sequence file from computer folder and return it as a dictionary for further use
    Author: Kaizen
    Date created: 04/25/2023
    """
    #Opens the sequence file in read mode
    f = open(file)
    #Defines the empty dictionary variable to store and return sequence and header
    sequence ={}
    header = ""  # To store Sequence Header
    #Exclude the header line when returning the sequence by checking for '>' in lines
    for line in f:
        if not line.startswith('>'):
            #Appending sequence of each line in the sequence variable converting it into uppercase
            sequence[header] += line.strip().upper()
        elif line.startswith('>'):
            header = line.strip()
            sequence[header] = ""
    #Closing the file
    f.close()
    #Return the sequence without header
    return sequence
def forFram(seqs,minORF,n): #Define a function with argument sequences, minORF, and a intege to perfrom the ORF 1~3 reading and return the ORF sequences and their positions.
    framL = []
    pos = []
    for dna in seqs:
        allFram = []
        fram = ""
        starts = False
        for i in range(n-1, len(dna), 3):
            codon = dna[i:i+3]
            if codon == 'ATG':
                fram += codon
                starts = True
            elif (codon == 'TAA' or codon == 'TAG' or codon == 'TGA') and starts:
                fram += codon
                allFram.append(fram)
                starts = False
                fram = ""
            elif starts:
                fram += codon
        allFram.sort(key=len, reverse=True)
        if len(allFram[0]) >= minORF:
            framL.append(allFram[0])
            pos.append(re.search(allFram[0],dna).start() + 1)
        else:
            framL.append('0')
            pos.append(0)
    return framL, pos

def orf(seq,minORF,n,allorf):
    orf=''
    start = False
    for i in range(n-1, len(seq),3):
        codon = seq[i:i+3]
        print(codon)
        print(orf)
        if codon == 'ATG':
            orf+=codon
            print('start')
            start =True
        elif codon == 'TAA' or codon =='TGA' or codon == 'TAG':
            print('stop')
            orf+=codon
            if len(orf)>=minORF:
                allorf.append(orf)
                print(allorf)
                start =False
                print(orf)
                orf=''
            else:
                orf=''
        elif start:
            print(codon)
            orf+=codon
            print(orf)
    print(allorf)

seq = seq_reader('/Users/kaizennathani/Downloads/sequenceS.fasta')
allorf=[]
for i in seq.values():
    print(i)
    orf(i,10,1,allorf)



