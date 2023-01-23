import math

def calc_wsize(fact_lst):
    wsize=fact_lst[-1]
    i=2
    while wsize<500:
        wsize*=fact_lst[-i]
        i+=1
    return wsize

def get_wsize(n):
    fact_lst=list()
    while n % 2 == 0:
        fact_lst.append(2)
        n = n // 2
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            fact_lst.append(int(i))
            n = n // i
    if n > 2:
        fact_lst.append(int(n))
    wsize=calc_wsize(fact_lst)
    return wsize