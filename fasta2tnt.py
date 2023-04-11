#!/usr/bin/python3

######### usage:    input: fasta_alignment output: tnt_matrix
#########           python3 fasta2tnt.py <fasta_alignment> <data_type> <missing_data> <output_file>
##### Import python libraries #####
from Bio import SeqIO
import sys

##### Define functions #####
def check_alignment_count(fasta_obj):
    '''Check if fasta sequences are aligned by comparing the lengh of each sequence. Returs True if sequences have the same lenght and the number of characters'''
    lst_lengh = []
    is_alignment = False
    for seq in al:
        lst_lengh.append(len(seq))
    if len(set(lst_lengh)) == 1:
           is_alignment = True
    else:
        is_alignment = False

    return is_alignment, lst_lengh[0]

def count_taxa(fasta_obj):
    '''Counts the number of taxa in a fasta file and ruturns a Int'''
    counter = 0
    for seq in fasta_obj:
        counter = counter + 1
    return counter


def fastaseqs2hennigseqs(fasta_obj, data_type='dna', missing='-'):
    '''Writes a string with all the information and format of a fucking TNT matrix'''

    f_string = ''

    f_string += 'nstates ' + str(data_type) + ';\nxread\n' + str(check_alignment_count(fasta_obj)[1]) + ' ' + str(count_taxa(fasta_obj)) + '\n'

    for seqs in fasta_obj:
        missing_string = str(seqs.seq).replace('-', missing)

        f_string += str(seqs.id) + '\t' + str(missing_string) + '\n'

    f_string += ';'

    return f_string


file_write = open(str(sys.argv[4]), 'w')

al = list(SeqIO.parse(str(sys.argv[1]),'fasta'))
taxon_names = []

for seq in al:
    taxon_names.append(seq.id)

file_write.write(fastaseqs2hennigseqs(al, str(sys.argv[2]), str(sys.argv[3])))
file_write.close()

print('Enjoy it! But why do you need a TNT matrix?')
