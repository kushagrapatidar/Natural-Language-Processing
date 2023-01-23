file= open("rawCorpus.txt",'r')
rawCorpus=file.read()
print(f"Total no. of characters in read dataset: {len(rawCorpus)}")