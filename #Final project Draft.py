"""
Practical Computer Concepts of Bioinformatics
Final Project draft
Group members: Kaizen, Taoyu, Yijun
"""

#Import the required package
import re

def seq_reader():
    """
    Function 1: seq_reader
    :param file:
    :return: Dictionary of Header:sequence
    Usage: To read FASTA sequence file from computer folder and return it as a dictionary for further use
    Author: Kaizen
    Date created: 04/25/2023
    """
    #Ask user for File name or File path for the FASTA file
    file = input('Please enter the name or the path of the FASTA sequence File:')
    #Flag variable to check if the file exist or not
    file_flag=False
    #Sequence dictionary to store FASTA sequence and header
    sequence = {}
    #Open sequence file in try and except block to handle IO error
    while not file_flag:
        try:
            # Opens the sequence file in read mode
            f = open(file)
            print('STATUS : File Found. Extracting the FASTA sequence...')
            #If file opened and exists then proceed with extracting sequence
            file_flag=True
        except IOError:
            #If file name not found print the error message and retry
            print('ERROR: The file path entered does not exist. Please enter again')
            file = input('Please enter the name or the path of the FASTA sequence File:')

    #If file found proceed with extracting the FASTA sequence
    if file_flag:
        #Defines the empty dictionary variable to store and return sequence and header
        header = ""  # To store Sequence Header
        #Exclude the header line when returning the sequence by checking for '>' in lines
        for line in f:
            if not line.startswith('>'):
                #Appending sequence of each line in the sequence variable converting it into uppercase
                sequence[header] += line.strip().upper()
            else:
                header = line.strip()
                sequence[header] = ""
        #Closing the file
        f.close()
    #Printing function output status
    print(f'STATUS : FASTA sequence extracted from file.\nNumber of Sequences found: {len(sequence)} ')
    # Return the sequence with header dictionary
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
    #If the frame is specified 4-6 first reverse compliment the sequence
    if n > 3:
        seqs = reverse_comp(seqs)
        n = n-3
    #Defining variables to store the orf sequence for each input sequence and frame
    allFram = []
    fram = ""
    #Flag operator variable to indicate if start codon is found or not
    starts = False
    #Checks for each codon if it is a START or STOP. If start then stores until STOP codon identified
    for i in range(n-1, len(seqs), 3):
        codon = seqs[i:i+3]
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
    if len(allFram)>0:
        if len(allFram[0]) >= minORF:
            #Append ORF sequence
            framL.append(allFram[0])
            #Calculate the position append to pos list
            pos.append(re.search(allFram[0],seqs).start() + 1)
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
    Author: Yijun
    """
    #Assigning position sign based on frame
    sign=''
    if n > 3:
        sign = '-'
    for index in range(0,len(fram),1):
        #Printing output header in required format
        print(f"{title}|FRAME={n + 1} POS={sign}{pos[index]} LEN={len(fram[index])}")
        #Printing the ORF sequence in required format
        for i in range(0, len(fram[index]), 3 * 15):
            print(' '.join(fram[index][i:i + 3 * 15][j:j + 3] for j in range(0, min(3 * 15, len(fram[index]) - i), 3)))


def main():
    """
    Main Function
    Authors: Kaizen, Yijun
    """

    #Reading the fasta sequence file using seq_reader() function
    proSeq = seq_reader()

    #Extracting all the sequence headers in title variable
    title = list(proSeq.keys())
    #Extracting all the sequences in seq variable
    seqs = list(proSeq.values())

    #Ask user to chaconfigure nge the minimum ORF sequence length. Default =50
    change = input('Do you wants to change the minimum ORF to search for (Default: 50)? (Y/N)')
    #If user wants to change ORF collect the input if not set minORF=50
    if change == 'Y':
        minORF = int(input('Enter the minimum ORF to search for:'))
    else:
        minORF = 50
    print(f'The minimum ORF sequence length is set to: {minORF}')
    
    #RUN AND OUTPUT
    #For each sequence present in Fasta file
    for ind in range(0,len(seqs)):
        #For each frame 1-
        for n in range(6):
            #Call the framsRead function to identify ORF sequences and their positions in each frame
            fram, pos = framsRead(seqs[ind],minORF,n+1)
            #If ORF sequence returned then print the output in required format
            if len(fram)>0:
                #Call the output display function to return the output in required format
                output_display(title[ind],fram,pos,n)


#Calling main function
main()



