sentence = str(input('type a sentence: ')).strip().upper()
gf = sentence.count('A')
gh = sentence.find('A') + 1
gt = sentence.rfind('A') + 1
print('the letter "A" appeared 8 times in the sentence'.format(gf))
print('the first letter "A" appeared in {} in the sentence'.format(gh))
print('the last letter "A" appeared in {} in the sentence'.format(gt))

#gh = frase.count('a')
#fh = frase.count('A')
#s =(gh) + (fh)
#print(s)

