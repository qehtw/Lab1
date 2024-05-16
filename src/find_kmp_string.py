def compute_prefix_function(needle):
    length_of_word = len(needle)
    prefix_sufix_list = [0] * length_of_word
    possition = 0
    for i in range(1, length_of_word):
        if possition > 0 and needle[possition] != needle[i]:
            possition = prefix_sufix_list[possition - 1]
        if needle[possition] == needle[i]:
            possition += 1
        prefix_sufix_list[i] = possition
    return prefix_sufix_list


def kmp_match(haystack, needle):
    prefix_sufix_list = compute_prefix_function(needle)
    current_pos = 0
    indicators = []
    for i in range(len(haystack)):
        if current_pos > 0 and needle[current_pos] != haystack[i]:
            current_pos = prefix_sufix_list[current_pos - 1]
        if needle[current_pos] == haystack[i]:
            current_pos += 1
        if current_pos == len(needle):
            indicators.append(i - len(needle) + 1)
            current_pos = prefix_sufix_list[current_pos - 1]
    return indicators

