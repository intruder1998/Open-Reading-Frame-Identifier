import re

def seq_reader(file):
    """
    Function 1: seq_reader
    :param file:
    :return: sequence
    Usage: To read FASTA sequence file from computer folder and return it as a string for further use
    Author: Kaizen
    Date created: 04/25/2023
    """
    #Opens the sequence file in read mode
    f = open(file)
    #Defines the empty string variable to store and return sequence
    sequence =''
    #Exclude the header line when returning the sequence by checking for '>' in lines
    for line in f:
        if not line.startswith('>'):
            #Appending sequence of each line in the sequence variable
            sequence += line.strip()
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
    print(cfind)
    cloc =re.search(r""+codon+r"",seq,re.M).end()
    #cloc = re.search(r"[\S|\w]+"+codon+r"[\S\w]+",seq,re.M).end()
    print(cloc)



codon_finder('ATG','AGCTATGCGATGCCGGGTAACATG')

s= seq_reader('/Users/kaizennathani/Downloads/sequence2.fasta')
#print(s)