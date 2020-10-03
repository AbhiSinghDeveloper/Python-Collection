
def reverse_words_in_sentence(sentence):
    arr = [c for c in sentence] # or just arr = list(sentence)
    n = len(arr)
    last_idx = n - 1
    start = 0

    # reverse all words
    for i in range(n):
        if arr[i] == ' ':
            # in this moment we're sure that the word is complete
            reverse_array(arr, start, i - 1)
            start = i + 1
    # reverse the last word
    reverse_array(arr, start, last_idx)
    # reverse the whole sentence
    reverse_array(arr, 0, last_idx)

    return ''.join(arr)

def reverse_array(arr, start, end):
    # reverse the array from the start index to the end index
    while start < end:
        arr[start], arr[end] = arr[end], arr[start] # swap
        start += 1
        end -= 1
