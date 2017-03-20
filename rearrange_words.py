def rearrangeWord(word):
        if len(word) <2:
            return
        # iterate through the word, starting at the end, check the last 2 characters - if last bigger than 2nd to last, swap them
        for i in range(1, len(word)+1):
            for j in range(1+i, len(word)+1):
                if word[-i] > word[-j]:
                    i_char = word[-i]
                    j_char = word[-j]
                    if j == len(word):
                        beg_word = ""
                    else:
                        beg_word = word[:-j]
                    if j - i == 1:
                        mid_word = ""
                    else:
                        mid_word = word[-j-1:-i]
                    if i == 1:
                        end_word = ""
                    else:
                        end_word = word[-i+1:]
                    word = beg_word + i_char + mid_word + j_char + end_word
                    print word
                    return
rearrangeWord("abcdaaa")