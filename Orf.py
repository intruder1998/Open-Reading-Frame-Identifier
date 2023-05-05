
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
        #print(codon)
        #print(orf)
        if codon == 'ATG':
            orf+=codon
            #print('start')
            start =True
        elif codon == 'TAA' or codon =='TGA' or codon == 'TAG':
            #print('stop')
            orf+=codon
            if len(orf)>=minORF:
                print('Here')
                print(len(orf))
                print(orf[0:3])
                print(orf[-3:])
                allorf.append(orf)
                #print(allorf)
                start =False
                #print(orf)
                orf=''
            else:
                orf=''
        elif start:
            #print(codon)
            orf+=codon
            #print(orf)
    print(allorf)
    return allorf

def reverse_comp(seq):
    """
        Function 2: reverse_comp
        :param seq:
        :return: reverse compliment sequence
        Usage: To reverse compliment a sequence
        Author: Kaizen
        Date created: 04/25/2023
        """
    #Defining the dictionary that contains compliment bases rules
    replace ={'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    #Reversing the input sequence
    revseq = seq[::-1]
    #Defining separate variable to store reverse compliment
    compseq=''
    #For each base in reversed sequence convert to its compliment
    for i in revseq:
        compseq+= replace[i]
    #Returning the reverse complimented string
    return compseq

def reverse_complement(sequence):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    reverse_seq = sequence[::-1]
    rev_complement = ''.join([complement[base] for base in reverse_seq])
    return rev_complement

# ci = reversecomp('ATGC')
# print(ci)
# print('---')


c =reversecomp('ATGC') #CGTA GCAT
print(c)


seq = seq_reader('/Users/kaizennathani/Downloads/sequenceS.fasta')
allorf=[]
a=[]
b=[]
minORF=300
for i in seq.values():
    print(i)
    for j in range(1,7,1):
        print(j)
        if j <=3:

            a=orf(i,minORF,j,a)
            allorf.append(a)
        if j>3:
            print('Reverse compliment')
            seqi = reversecomp(i)
            print(i)
            print('-----')
            print(seqi)

            b=orf(seqi,minORF,j,b)
            allorf.append(b)

print('---***')
print(len(allorf))
for i in allorf:
    print(i)
    print(len(i))




