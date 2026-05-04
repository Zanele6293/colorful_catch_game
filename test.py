def primeNum(numb):
    if numb<=0:
        return "Not prime number"
    if numb == 1 :
        return 2
    numbers =[]
    results = []
    for i in range(2,numb+1):
        numbers.append(i)
    count = 0    
    for a in range(2,numb+1):
        for k in numbers:
            if a% k ==0:
                count +=1
                if count >1:
                    pass
                results.append(a)
    return results
print(primeNum(12))          