# %%
#Final project Draft
import re

def fileRead(filePath): #Define a function called fileRead to read the file and store the titles and their correspoding sequence into a dictionary.
    with open(filePath, 'r') as file: #Open the file.
        lines = file.readlines()
    proSeq = {}
    title = ""
    for i in range(len(lines)):
        if lines[i].startswith('>'):
            title = lines[i].rstrip()
            proSeq[title] = ""
        else:
            proSeq[title] += lines[i].rstrip().upper()
    print(proSeq)
    return proSeq
fileRead('/Users/kaizennathani/Downloads/sequenceS.fasta')

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

def revFram(seqs,minORF,n):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    framL = []
    pos = []
    for dna in seqs:
        rdna = ''.join(complement[base] for base in reversed(dna))
        allFram = []
        fram = ""
        starts = False
        for i in range(n-4, len(rdna), 3):
            codon = rdna[i:i+3]
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
            pos.append(re.search(allFram[0],rdna).start() + 1)
        else:
            framL.append('0')
            pos.append(0)
    return framL, pos

def main():
    filePath = input('Please enter the name or the path of the File:') #Get the name or path of the file and store as a variable.

    proSeq = fileRead(filePath)

    title = list(proSeq.keys())
    seqs = proSeq.values()

    #minORF input
    change = input('Do you wants to change the minimum ORF to search for (Default: 50)? (Y/N)')
    if change == 'Y':
        minORF = int(input('Enter the minimum ORF to search for:'))
    else:
        minORF = 50

    #Run & Output
    for n in range(6):
        if n < 3:
            fram, pos = forFram(seqs,minORF,n+1)
        else:
            fram, pos = revFram(seqs,minORF,n+1)
        for index in range(len(title)):
            if fram[index] != '0':
                print(f"{title[index]}|FRAME={n+1}|POS={pos[index]}|LEN={len(fram[index])}")
                for i in range(0, len(fram[index]), 3 * 15):
                    print(' '.join(fram[index][i:i + 3 * 15][j:j + 3] for j in range(0, min(3 * 15, len(fram[index]) - i), 3)))

main()





