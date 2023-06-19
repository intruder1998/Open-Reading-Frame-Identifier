# Open Reading Frame Identifier
Python code to extract all the open reading frames in all frames 1-6 for ALL the sequences in a given FASTA File

**Functions:**
**1. Seq_reader()**: Prompts the user to input the FASTA file directory location, loads all the valid FASTA sequence in a python dictionary where sequence header are keys and the sequence are values. It checks for valid file name and fasta sequence.
**2. reverse_comp(seq)**: Produces the reverse complimentary sequence for a given input sequence. Takes the input sequence as the argument
**3. framsRead(seqs, minORF,n)**: Function to return all the ORF sequences identified in a given sequence(seqs) and  having the provided minimum sequence length(minORF)  and a given frame (n). This function also returns the start and end positions of the open reading frames identified.
**4. output_display(title,fram,pos,n**): This function is used to display the ouput of the framsRead() function in a strucutred manner where each line does not display more than 32 bases and for each ORF identified, its corresponding header, frame number and lenght is displayed.
