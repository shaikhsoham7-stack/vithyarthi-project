def validate_sequence(sequence):
    """Return True if the sequence contains only A, T, G and C."""
    if not sequence:
        return False

    sequence = sequence.upper()

    for nucleotide in sequence:
        if nucleotide not in "ATGC":
            return False

    return True
