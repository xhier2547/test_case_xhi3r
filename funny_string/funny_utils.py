def isubin_funny(subin):
    a=subin[::-1]
    for i in range(len(subin)-1):
        if abs(ord(subin[i])-ord(subin[i+1]))!=abs(ord(a[i])-ord(a[i+1])):
            return "Not Funny"
    return "Funny"

if __name__ == '__main__':

    qin = int(input().strip())

    for qin_itr in range(qin):
        subin = input()

        resubinult = isubin_funny(subin)
        print(resubinult + '\n')