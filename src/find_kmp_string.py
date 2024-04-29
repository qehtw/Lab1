def compute_prefix_function(needle):
    length_of_word = len(needle)
    pi = [0] * length_of_word
    k = 0
    for i in range(1, length_of_word):
        print('k its:', k ,'i its:',i , needle[k] , needle[i] , pi)
        if k > 0 and needle[k] != needle[i]:
            k = pi[k - 1]
        if needle[k] == needle[i]:
            k += 1
        pi[i] = k
    return pi

def kmp_match(haystack, needle):
    pi = compute_prefix_function(needle)
    q = 0
    indices = []
    for i in range(len(haystack)):
        if q > 0 and needle[q] != haystack[i]:
            q = pi[q - 1]
        if needle[q] == haystack[i]:
            q += 1
        if q == len(needle):
            indices.append(i - len(needle) + 1)
            q = pi[q - 1]
    return indices



haystack = "ababcbcbabcabdcabcabc"
needle = "abcabd"
print(kmp_match(haystack, needle))

