def alternating_Characters(s):
    delete = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            delete += 1
    return delete
    
if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternating_Characters(s)
        
        print(result)