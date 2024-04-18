def find_longest_word(word_list):
    longest_words=[]
    max_length=0
    for word in word_list:
        word_length=len(word)
        if word_length>max_length:
            longest_words=[word]
            max_length=word_length
        elif word_length==max_length:
            longest_words.append(word)
    return longest_words
word_list=["hii","hello","happy","infidata"]
result=find_longest_word(word_list)
print("longest words:",result)



