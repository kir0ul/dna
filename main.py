def GenSequence(N):
    """Generate a DNA sequence of length N """
    
    import random
    seq = [random.choice(["G", "A", "T", "C"]) for i in range(N)]
    # print(seq)
    return seq
        
