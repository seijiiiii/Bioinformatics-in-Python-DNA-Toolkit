def colored(seq):
    bcolor = {
        'A': '\033[92m',
        'C': '\033[94m',
        'G': '\033[93m',
        'T': '\033[91m',
        'U': '\033[91m',
        'reset':'\033[0;0m'
    }
    tmpStr = ''

    for nuc in seq:
        if nuc in bcolor:
            tmpStr += bcolor[nuc] + nuc
        else:
            tmpStr += bcolor['reset'] + nuc

    return tmpStr + '\033[0;0m'
