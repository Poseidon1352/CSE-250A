from math import log
import matplotlib.pyplot as plt

with open('vocab.txt') as file:
    words = file.read().splitlines()

with open('unigram.txt') as file:
    unigrams = file.read().splitlines()    
unigrams = [int(x) for x in unigrams]
N = sum(unigrams)
uprobs = [x/N for x in unigrams]

print("Words starting with 'B' and their probabilites.")
for i in range(500):
    if words[i][0] == 'B':
        print(words[i]+' '+str(uprobs[i]))
    if words[i] == 'ONE':
        one_loc = i
        
bigrams = [[0]*500 for x in range(500)]
bSum = 0
with open('bigram.txt') as file:
    for line in file:
        val = line.split()
        val = [int(x) for x in val]
        bigrams[val[0]-1][val[1]-1] = val[2]
condprobs = [[0]*500 for x in range(500)]
for i in range(500):
    uSum = sum(bigrams[i])
    if uSum != 0:
        condprobs[i] = [x/uSum for x in bigrams[i]]

print('\nWords that follow ONE with greatest probability.')
K = bigrams[one_loc]
top10 = sorted(range(len(K)), key=lambda x: K[x])[-10:]
for i in range(len(top10)):
    print(words[top10[i]])

sentence = '\nTHE STOCK MARKET FELL BY ONE HUNDRED POINTS LAST WEEK'
#sentence = '\nTHE FOURTEEN OFFICIALS SOLD FIRE INSURANCE'
print(sentence)
sentence = sentence.split()
Lu = 0; Lb = 0;
lambdas = [0.01*x for x in range(100)]
Lm = [0]*100
for i in range(len(sentence)):
    Pu = uprobs[words.index(sentence[i])]
    Lu = Lu + log(Pu)
    try:
        if i == 0:
            Pb = condprobs[words.index('<s>')][words.index(sentence[i])]
            Lb = Lb + log(Pb)
        else:
            Pb = condprobs[words.index(sentence[i-1])][words.index(sentence[i])]
            Lb = Lb + log(Pb)
    except ValueError:
        print('ValueError: '+sentence[i-1]+' '+sentence[i]+' Probability ='+str(Pb))
    for j in range(100):
            Lm[j] = Lm[j] + log((1 - lambdas[j])*Pu + lambdas[j]*Pb)

print('Lu='+str(Lu)+' Lb='+str(Lb))
#print('Optimal \lambda ='+str(lambdas[Lm.index(max(Lm))]))

#plt.plot(lambdas,Lm)
#plt.ylabel('Lm')
#plt.xlabel('Lambdas')
plt.show()
