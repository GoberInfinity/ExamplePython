def prefix_array(string):
    length = len(string)
    prefixes = [0] * length
    
    for current_index in range(1, length):
        # When there is a missmatch, start_comparing tells about where to start comparing next
        # the main idea is to skip the letters that already matched
        start_comparing = prefixes[current_index-1]
        while start_comparing > 0 and string[current_index] != string[start_comparing]:
            start_comparing = prefixes[start_comparing-1]
        if string[current_index] == string[start_comparing]:
            # The index of the string where you should begin to compare after a missmatch (non matching chars)
            start_comparing += 1 
        prefixes[current_index] = start_comparing
    return prefixes
    
def kmp(word, text):
    prefixes = prefix_array(word)
    word_index = 0
    text_index = 0
    while text_index < len(text):
        if word[word_index] != text[text_index]:
            if word_index == 0:
                # Didn't match, try next letter in text
                text_index += 1
            else:
                # prefixes[word_index-1] will tell from where to compare next
                word_index = prefixes[word_index-1]
        else:
            word_index += 1
            text_index += 1
            if word_index == len(word):
                print(f"found pattern at {str(text_index - word_index)}") 
                # if we want to find more patterns, we can 
                # continue as if no match was found at this point.
                word_index = prefixes[word_index-1]
                
kmp("acabacacd", "acfacabacabacacdk")
kmp("ABABCABAB", "ABABDABACDABABCABAB")