def binarySearch(a_numbers, e_lookup):
    found = False
    i_first = 0
    i_last = len(a_numbers)-1
    
    while i_first <= i_last and not found:
        i_mid = (i_first + i_last)//2
        if a_numbers[i_mid] == e_lookup:
            print(i_mid)
            found = True
        else:
            if e_lookup > a_numbers[i_mid]:
                i_first = i_mid+1
            else:
                i_last = i_mid-1
    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 13))