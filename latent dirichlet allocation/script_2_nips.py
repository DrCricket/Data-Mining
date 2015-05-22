''' NIPS full papers: 
    orig source: books.nips.cc 
    D=1500 
    W=12419 
    N=1,900,000 (approx) '''

''' For each text collection, D is the number of documents, W is the 
    number of words in the vocabulary, and N is the total number of words 
    in the collection '''



import numpy as np
import lda
import lda.datasets
import os

X = []
D = 1500            ## Change according to the dataset
W = 12419           ## Change according to the dataset
for i in range(0,D):
    X.append([0]*W)


'''' READ THE DATA FILE '''
    
path_f = os.path.join(os.getcwd(),"docword.nips.txt")
f = open(path_f)

index = 0
for i in f:
    if index > 2:
        data = i.split()
        X[int(data[0])-1][int(data[1])-1] = int(data[2])
        ## print X[int(data[0])][int(data[1])]
    index = index+1

X = np.array(X)



# X = lda.datasets.load_reuters()

''' READ THE VOCAB FILE '''

path_v = os.path.join(os.getcwd(),"vocab.nips.txt")
v = open(path_v)

vocab = []

for i in v:
    vocab.append(i)
vocab = tuple(vocab)

# vocab = lda.datasets.load_reuters_vocab()

num_topics = 15          ## Number of topics to be extracted
num_iterations = 30      ## Number of iterations of the algorithm

model = lda.LDA(n_topics=num_topics,n_iter=num_iterations,random_state=42,alpha=0.3)
model.fit(X)





''' DISPLAY THE TOP 'n' WORDS FOR EACH TOPIC '''


topic_word = model.topic_word_

n = 5

for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n+1):-1]
    print('*Topic {}\n- {}'.format(i, ' '.join(topic_words)))



f.close()
v.close()


