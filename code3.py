if __name__ == '__main__':
    n = int(raw_input())
    #arr=n.split()
    arr = map(int, raw_input().split())
    maximum=max(arr)
    minimum=min(arr)
    for each in arr:
        if each>=minimum and each<maximum:
            minimum=each
    print minimum #this is second largest number   
