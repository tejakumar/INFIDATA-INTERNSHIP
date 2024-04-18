with open('word.txt') as f:
    data=f.read()
    data.replace('','')
    count=len(data.split())
print("num of words in a file:",count)
