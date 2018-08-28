import itertools

def is_palindrome(dna):
    k = len(dna)
    revcomp = ''

    for i in range(k):
        if dna[k - 1 - i] == 'A':
            revcomp += 'T'
        elif dna[k - 1 - i] == 'T':
            revcomp += 'A'
        elif dna[k - 1 - i] == 'C':
            revcomp += 'G'
        elif dna[k - 1 - i] == 'G':
            revcomp += 'C'

    if revcomp == dna:
        return True
    else:
        return False

'''Produce all k-mer palindromes'''
def palindromes(k):
    reverse_conjugates = []
    neucleotides = 'ATCG'
    permutations = list(map(list, itertools.product(neucleotides, repeat=k)))
    str = ''

    for p in permutations:
        if is_palindrome(str.join(p)):
            reverse_conjugates.append(str.join(p))

    return reverse_conjugates



if __name__ == '__main__':
    k = int(input('Enter a value for k: '))
    print(palindromes(k))

