# Problem Set 4A
# Name: Jatin
# Collaborators: None
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    list = []
    # Base case
    if len(sequence) == 1:
        return [sequence]
    
    # Recursive case
    else:
        for permutation in get_permutations(sequence[1 : ]):
            for i in range(len(permutation) + 1):
                new_permutation = permutation[ : i] + sequence[0] + permutation[i : ]
                list.append(new_permutation)
    return list
            

if __name__ == '__main__':
#    #EXAMPLE
   example_input = 'abcd'
   print('Input:', example_input)
   print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
