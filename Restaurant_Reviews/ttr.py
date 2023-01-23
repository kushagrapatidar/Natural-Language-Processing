from vocab import build_vocab
from prepro import preprotxt
from windowsize import get_wsize

def build_ottr(words,l):
    vocab=build_vocab(words)
    print(vocab)
    vl=len(vocab)
    print(vl)
    ttr=vl/l
    return ttr

def build_nttr(words,l):
    wsize=int(get_wsize(l))
    nwin=int(l//wsize)
    print(wsize,nwin)
    ttr_lst=list()
    for i in range(nwin-1):
        ttr_lst.append(ottr(words[i*wsize:(i+1)*wsize],wsize))
    ttr=sum(ttr_lst)/len(ttr_lst)
    return ttr

fname='Restaurant_Reviews.txt'
words=preprotxt(fname)
l=len(words)

ottr=build_ottr(words,l)
nttr=build_nttr(words,l)
print(f"Old TTR: {ottr}")
print(f"New TTR: {nttr}")

