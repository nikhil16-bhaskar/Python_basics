def count_substring(string, sub_string):
    pos=0
    j=0
    length=len(string)
    sub_length=len(sub_string)
    #i=0
    count=0
    while j!=length:
        if string[pos:j+sub_length]==sub_string:
            count+=1
        pos+=1
        j+=1
        #i+=1
    return count
