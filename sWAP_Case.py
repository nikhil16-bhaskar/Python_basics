def swap_case(s):
    length=len(s)
    new=''
    for each in s:
        if ord(each)>=ord('a') and ord(each)<=ord('z'):
            each=each.upper()
        elif ord(each)>=ord('A') and ord(each)<=ord('Z'):
            each=each.lower()
        new+=each    
        
 
    return new
