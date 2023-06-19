import re

def main():
    filename = input("Enter the file name: ") #Open the file (test file name: sequence)
    s = ReadSeq(filename)

    title = list(s.keys())
    seqs = s.values()

    minORF = input("is the ORF = 50? (Y/S)?: ")
    if minORF == 'Y':
        minORF = 50
    else:
        minORF = input("Enter the minORF values: ")

def ReadSeq(filename): #Read the test file in lines
    file = open(filename,'r')
    s = {}
    title = ''
    line = file.read()
    for i in range(len(line)):
        if line[i].startswith('>'):
            title = line[i].rstrip()
            s[title] = ''
        else:
            s[title] = s[title] + line[i].rstrip()
    print (s)
    return s

def reverse(seq):
    replace = {"A":"T","C":"G","T":"A","G":"C"}
    revseq = seq[::-1]
    newseq=''
    for i in revseq:
        newseq = newseq + replace[i]
    return newseq

def codon(seqs, minORF,n):
    fram1 = []
    if n>3:
        seqs = reverse(seqs)
    allfram = []
    fram = ''
    for i in range (n-1,len(seqs),3):
        codon = seqs[i:i+3]
        fram = fram + codon
    if codon == 'ATG':
        fram += codon
    elif (codon == "TAG" or codon == "TAA" or codon == "TGA"):
        fram = fram + codon
        allfram.append(fram)
        fram = ''
    else:
        fram = fram + codon
    return fram1



# need discussed, I have trouble with finished this function
# and how to finish display two outputs?











main()