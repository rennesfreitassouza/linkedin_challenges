from itertools import zip_longest, tee, chain


# without zip_longest
# another_sequence2 = sequence
# another_sequence2.extend([fillvalue] * offset)
# another_sequence = [fillvalue] * offset
# another_sequence.extend(sequence)
# l = list(zip(another_sequence2, another_sequence))
# return l
def pairwise_offset(sequence=[], fillvalue='*', offset=0):
    '''https://www.linkedin.com/learning/\
advanced-core-python-code-challenges/create-a-pairwise-offset'''
    # it1, it2 = tee(sequence, 2)
    # return zip_longest(it1, chain(fillvalue * offset, it2), fillvalue=fillvalue)
    another_sequence = [fillvalue] * offset
    another_sequence.extend(sequence)
    return zip_longest(sequence, another_sequence,
                       fillvalue=fillvalue)


if __name__ == "__main__":
    kwargs = {"sequence": ["a", "b", "c"], "fillvalue": '*', "offset": 2}
    pairwise_offset(**kwargs)
