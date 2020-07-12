from pathlib import Path


def seq_ping():
    """function used to test"""
    print('OK!')


def seq_read_fasta(file):
    """
    Read a 'dna' sequence in 'fasta' format
    """

    # -- Read the file
    contents = Path(file).read_text()

    # -- Remove the head
    body = contents.split('\n')[1:]

    # -- Return the body as a string
    return "".join(body)


def seq_len(seq):
    return len(seq)


def seq_count_base(seq, base):
    """
    Counting the individual bases on the sequence
    """
    return seq.count(base)


def seq_count(seq):
    """
    Calculate the number of bases in the sequence
    """
    result = {'A': seq_count_base(seq, 'A'), 'T': seq_count_base(seq, 'T'),
              'C': seq_count_base(seq, 'C'), 'G': seq_count_base(seq, 'G')}
    return result


def seq_reverse(seq):
    """
    Return the reverse sequence
    """
    return seq[::-1]


def seq_complement(seq):
    """
    Return the complement sequence
    """
    # -- Dictionary of complement bases
    base = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    result = ""
    for i in seq:
        result += base[i]

    return result
