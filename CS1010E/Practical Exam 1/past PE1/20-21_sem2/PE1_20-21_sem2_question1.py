#iterative
def dna_transcription_I(dna: str) -> str:
    rna = ''
    pairs = {
        "A": "U",
        "G": "C",
        "T": "A",
        "C": "G"
    }
    for character in dna:
        rna += pairs[character]

    return rna

#print(dna_transcription_I('AGCTGACGTA'))

#recursive
def dna_transcription_R(dna: str) -> str:
    rna = ''
    pairs = {
        "A": "U",
        "G": "C",
        "T": "A",
        "C": "G"
    }

    if dna == '':
        return ''
    else:
        rna += pairs[dna[0]]
        return rna + dna_transcription_R(dna[1:])

#print(dna_transcription_R('AGCTGACGTA'))

    
