import numpy as np
import lda
import lda.datasets

X = []
for i in range(0,3430):
    X.append([0]*6906)


f = open("path to docword.kos.txt")

index = 0
for i in f:
    if index > 2:
        data = i.split()
        X[int(data[0])-1][int(data[1])-1] = int(data[2])
        ##print X[int(data[0])][int(data[1])]
    index = index+1

X = np.array(X)
v = open("path to vocab.kos.txt")

vocab = []

for i in v:
    vocab.append(i)
vocab = tuple(vocab)

model = lda.LDA(n_topics=15,n_iter=500,random_state=42)
model.fit(X)

topic_word = model.topic_word_

n = 5

for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n+1):-1]
    print('*Topic {}\n- {}'.format(i, ' '.join(topic_words)))

f.close()
v.close()


