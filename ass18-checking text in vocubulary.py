#DSA-Assgn-18

def find_unknown_words(text,vocabulary):
    #Remove pass and write your logic here
    res=[]
    text=text.split(" ")
    for i in text:
        if i not in vocabulary:
            res.append(i)
    if len(res)==0:
        return -1
    return set(res)

#Pass different values of text and vocabulary to the function and test your program
text="The sun rises in the east and sets in the west."
vocabulary = ["sun","in","rises","the","east"]
unknown_words=find_unknown_words(text,vocabulary)
print("The unknown words in the file are:",unknown_words)
