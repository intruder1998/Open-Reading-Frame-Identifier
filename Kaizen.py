import re

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

def codon_finder(codon,seq):
    """
    Function 2:
    :param codon: start codon(ATG) | stop codon (TAA, TAG or TGA)
    :return: location of the codon
    Usage: Returns the location of the codon specified in argument in the input sequence string
    Author: Kaizen
    Date created: 04/25/2023
    """
    cfind = re.findall(r""+codon+r"",seq,re.M)
    #print(cfind)
    cfind2 = re.findall(r"" + codon + r"[\S|\w]+", seq, re.M)
    cfind3 = re.findall(r"" + codon + r"[^"+codon+"]+.+", seq, re.M)
    cfind4 = re.findall(r""+codon+"(?!.+ATG).+TAA$",seq,re.M)
    cfind5 = re.findall(r"(ATG(?:...)+)(?=TAA|TAG|TGA)",seq)
    #print(cfind2)
    for i in cfind5:
        print(i)
    print(cfind5)
    #print(cfind3)
    cloc =re.search(r""+codon+r"",seq,re.M).end()
    #cloc = re.search(r"[\S|\w]+"+codon+r"[\S\w]+",seq,re.M).end()
    #print(cloc)

def orf_finder(sequence):
    #Define the start codon pattern
    start_codon = re.compile(r'ATG')
    #Define the stop codon patter
    stop_codon = re.compile(r'[TAA|TAG|TGA]')

    #Compute all the instances of starts and stops in sequence
    starts = start_codon.finditer(sequence)
    ends = stop_codon.finditer(sequence)

    #Define the variables to store start and stop codon positions in sequence
    start_pos=[]
    stop_pos=[]

    #Get the positions of start  codon instances
    for m in starts:
        start_pos.append(m.start())
    #Get positions of stop codon instances
    for j in ends:
        stop_pos.append(j.start())

    #Define list to store the ORFs
    orfs=[]

    print(stop_pos,start_pos)
    #For each start and stop codon position check is the compile the ORF condition
    for s in start_pos:
        for e in stop_pos:
            if e>s and (e-s)%3==0:
                orfs.append(sequence[s:e+3])
                break
    print(orfs)



    #start_pos = [i.start]

seq2= 'GCTAGCATGACGGTGGAGTTGAAAGTCTGAAGACCATGACAGTGGGTTCTTACGAGTAA'
seq1='ATGCGATGCCGGGTAACATG'
#codon_finder('ATG',seq2)

s= seq_reader('/Users/kaizennathani/Downloads/sequenceS.fasta')
print(s)
#orf_finder(s)


#print(s)

def orf_findser(seq):
    orfs=[]
    for i in range(0,len(seq)-2,3):
        orf=''
        codon = seq[i:i+3]
        print('Main loop')
        print(codon)
        if codon == 'ATG':
            print('Start')
            orf = codon
            for j in range(i+3,len(seq)-2,3):
                nxcodon = seq[j:j+3]
                print(nxcodon)
                orf = orf+' '+nxcodon
                print(orf)
                if nxcodon in ('TAA|TGA|TAG'):
                    print('Stop found')
                    #orf=orf+nxcodo
                    orfs.append(orf)
                    print(orf)
                    orf=''
                    break
    return orfs

a=orf_findser()
print(a)


