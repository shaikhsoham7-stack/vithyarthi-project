def complement(sequence):
    """Return the complementary DNA sequence."""
    pairs = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }

    return "".join(pairs[nucleotide] for nucleotide in sequence.upper())


def reverse_sequence(sequence):
    """Return the DNA sequence in reverse order."""
    return sequence.upper()[::-1]


def reverse_complement(sequence):
    """Return the reverse complement of a DNA sequence."""
    return complement(sequence)[::-1]
