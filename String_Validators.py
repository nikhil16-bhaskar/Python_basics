def alpha(s):
    length=len(s)
    k=length
    i=0
    while(k):
        if s[i].isalpha():
            print "True"
            break
        i+=1
        k-=1
        
    if (length==i):
        print "False"
    
def digit(s):
    length=len(s)
    k=length
    i=0
    while(k):
        if s[i].isdigit():
            print "True"
            break            
        i+=1
        k-=1
        
    if (length==i):
        print "False"

def upper(s):
    length=len(s)
    k=length
    i=0
    while(k):
        if s[i].isupper():
            print "True"
            break
        i+=1
        k-=1
        
    if (length==i):
        print "False"        

def lower(s):
    length=len(s)
    k=length
    i=0
    while(k):
        if s[i].islower():
            print "True"
            break
        i+=1
        k-=1
        
    if (length==i):
        print "False"
        
def alphanum(s):
    length=len(s)
    k=length
    count=0
    i=0
    while(k):
        if s[-1]=='!' or s[-1]=='@' or s[-1]=='#' or s[-1]=='$' or s[-1]=='%' or s[-1]=='^' or s[-1]=='&' or s[-1]=='*':
            print "False"
            break
        if s[i].isalnum():
            count+=1
            if(count==2):
                print "True"
                break
        i+=1
        k-=1
        
    if (length-1==i):
        print "False"
        
if __name__ == '__main__':
    s=raw_input()
    alphanum(s)
    alpha(s)
    digit(s)
    lower(s)
    upper(s)
