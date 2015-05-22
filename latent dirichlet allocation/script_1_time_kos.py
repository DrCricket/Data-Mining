import numpy as np
import lda
import lda.datasets
import os
import time
import matplotlib.pyplot as plt

X = []
D = 3430
W = 6906
for i in range(0,D):
    X.append([0]*W)


'''' READ THE DATA FILE '''
    
path_f = os.path.join(os.getcwd(),"docword.kos.txt")
f = open(path_f)

index = 0
for i in f:
    if index > 2:
        data = i.split()
        X[int(data[0])-1][int(data[1])-1] = int(data[2])
        ## print X[int(data[0])][int(data[1])]
    index = index+1

X = np.array(X)

timing_X = [] ## Number of iterations
timing_Y = [] ## Time in seconds

# X = lda.datasets.load_reuters()

''' READ THE VOCAB FILE '''

path_v = os.path.join(os.getcwd(),"vocab.kos.txt")
v = open(path_v)

vocab = []

for i in v:
    vocab.append(i)
vocab = tuple(vocab)

# vocab = lda.datasets.load_reuters_vocab()

for i in range(40,521,15):
    
    num_topics = 15         ## Number of topics to be extracted
    num_iterations = i      ## Number of iterations of the algorithm
    model = lda.LDA(n_topics=num_topics,n_iter=num_iterations,random_state=42,alpha=0.3)

    start = time.time()
    model.fit(X)
    end = time.time()
    
    timing_X.append(i)
    timing_Y.append(end-start)
    
    

plt.plot(timing_X,timing_Y,'bo')
plt.axis([0,max(timing_X),0,max(timing_Y)])
plt.show()

f.close()
v.close()


