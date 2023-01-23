f=open("text.txt")
lines=f.readlines()

l=len(lines)

'''#for removing endlines
for _ in range(l):
	line=lines[_]
	if '\n' in line:
		lines[_]=line[:-1]		
	print(line)

#creating tokens
tokens=list()
count=dict()
for line in lines:
	word=""
	words=list()
	for chr in line:
		if chr==" ":
			if word in count.keys():
				count[word]+=1
			else:
				count[word]=1
			words.append(word)
			word=""
			continue
		elif chr==line[-1]:
			word+=chr
			if word in count.keys():
				count[word]+=1
			else:
				count[word]=1
			words.append(word)
			word=""
			continue
		word+=chr
	tokens.append(words)

print(tokens)
print(count)
'''
for _ in range(l):
	lines[_]=lines[_].lower()
	lines[_]=lines[_].strip('\n')
	line=lines[_]
count=dict()
for line in lines:
	for word in line:
		if word in count.keys():
			count[word]+=1
		else:
			count[word]=1

print(count)
print(lines)
