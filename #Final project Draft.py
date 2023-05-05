"""
Practical Computer Concepts of Bioinformatics
Final Project draft
Group members: Kaizen, Taoyu, Yijun
"""

#Import the required package
import re

def seq_reader(file):
    """
    Function 1: seq_reader
    :param file:
    :return: Dictionary of Header:sequence
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

def reverse_comp(seq):
    """
        Function 2: reverse_comp
        :param seq: Input DNA sequence
        :return: reverse compliment sequence
        Usage: To reverse compliment a sequence
        Author: Taoyu
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

def framsRead(seqs,minORF,n):
    """
    Function 3: To identify the ORF sequence in a given frame and given minimum length
    :param seqs: Input sequence list extracted from multi-fasta file
    :param minORF: Minimum length to identify ORF sequence
    :param n: Frame number
    :return: Returns the ORF sequence and their corresponding positions in the sequence
    Authors: Yijun, Kaizen and Toayu
    """
    #Defining the LIST variables to store ORF sequence and their positions in the sequence
    framL = []
    pos = []
    #For each sequence in list of sequences in the Fasta file
    for dna in seqs:
        #If the frame is specified 4-6 first reverse compliment the sequence
        if n > 3:
            dna = reverse_comp(dna)
            n = n-3
        #Defining variables to store the orf sequence for each input sequence and frame
        allFram = []
        fram = ""
        #Flag operator variable to indicate if start codon is found or not
        starts = False
        #Checks for each codon if it is a START or STOP. If start then stores until STOP codon identified
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
        """Sorting all the identified ORF sequence in reverse and check if maximum 
        orf sequence is more than minimium ORF length specified"""
        allFram.sort(key=len, reverse=True)
        if len(allFram[0]) >= minORF:
            #Append ORF sequence
            framL.append(allFram[0])
            #Calculate the position append to pos list
            pos.append(re.search(allFram[0],dna).start() + 1)
        else:
            framL.append('0')
            pos.append(0)
    #Return the ORF sequence and their corresponding sequence
    return framL, pos


def output_display(title,fram,pos,n):
    """
    Function 4: To display the output in the specified format
    :param title: The header of the sequence
    :param fram: The orf seqeunce
    :param pos: Position of Start codon of ORF sequence
    :param n: Frame Number
    :return: It prints the output in required format
    """
    #For each sequence
    for index in range(len(title)):
        #If the list has an ORF sequence
        if fram[index] != '0':
            #Printing output header in required format
            print(f"{title[index]}|FRAME={n + 1}|POS={pos[index]}|LEN={len(fram[index])}")
            #Printing the ORF sequence in required format
            for i in range(0, len(fram[index]), 3 * 15):
                print(' '.join(fram[index][i:i + 3 * 15][j:j + 3] for j in range(0, min(3 * 15, len(fram[index]) - i), 3)))


def main():
    """
    Main Function
    Authors: Kaizen, Yijun
    """
    #Asking the user for the FASTA sequence file path
    filePath = input('Please enter the name or the path of the File:')
    #Reading the fasta sequence file using seq_reader() function
    proSeq = seq_reader(filePath)

    #Extracting all the sequence headers in title variable
    title = list(proSeq.keys())
    #Extracting all the sequences in seq variable
    seqs = proSeq.values()
    
    #Ask user to chaconfigure nge the minimum ORF sequence length. Default =50
    change = input('Do you wants to change the minimum ORF to search for (Default: 50)? (Y/N)')
    #If user wants to change ORF collect the input if not set minORF=50
    if change == 'Y':
        minORF = int(input('Enter the minimum ORF to search for:'))
    else:
        minORF = 50
    
    #RUN AND OUTPUT
    for n in range(6):
        #Call the framsRead function to identify ORF sequences and their positions in each frame
        fram, pos = framsRead(seqs,minORF,n+1)
        #Call the output display function to return the output in required format
        output_display(title,fram,pos,n)

#Calling main function
main()



