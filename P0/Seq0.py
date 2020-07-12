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