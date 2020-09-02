def reverse(string):
    """Returns the reverse of the given string."""
    return string[::-1]


def is_anagrams(string1, string2):
    """Checks whether two strings are anagrams of each other."""
    string1 = ''.join(sorted(list(string1.replace(' ', ''))))
    string2 = ''.join(sorted(list(string2.replace(' ', ''))))

    return string1 == string2


def reverse_sentence(sentence):
    """Reverses each words of the sentence while keeping word orders same."""
    return ' '.join([word[::-1] for word in sentence.split(' ')])


def hamming_distance(string1, string2):
    """Returns the hamming distance between two strings of equal length."""
    assert len(string1) == len(string2)

    distance = 0
    for i in range(len(string1)):
        if string[i] != string2[i]:
            distance += 1
    
    return distance
