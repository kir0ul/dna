def GenSequence(N):
    """Generate a DNA sequence of length N """
    
    import random
    seq = [random.choice(["G", "A", "T", "C"]) for i in range(N)]
    return seq

def QuerySubSequence(seq, substr):
    """Return True if `substr` is contained inside `seq`"""

    import re

    # Convert sequence in string
    seqStr = ""
    for i in seq:
        seqStr += i

    # Search for substring
    p = re.compile(substr)
    m = p.search(seqStr)
    if m == None:
        found = False
    else:
        found = True

    return found
