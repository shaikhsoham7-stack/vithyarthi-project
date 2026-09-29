def analyze_sequence(sequence):
    """Return basic information about a valid DNA sequence."""
    sequence = sequence.upper()
    length = len(sequence)

    a_count = sequence.count("A")
    t_count = sequence.count("T")
    g_count = sequence.count("G")
    c_count = sequence.count("C")

    gc_content = ((g_count + c_count) / length) * 100
    at_content = ((a_count + t_count) / length) * 100

    return {
        "length": length,
        "A": a_count,
        "T": t_count,
        "G": g_count,
        "C": c_count,
        "GC": gc_content,
        "AT": at_content
    }
