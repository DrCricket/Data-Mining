from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split,cross_val_score
from sklearn import metrics
from scipy.stats.stats import pearsonr
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

from sklearn.preprocessing import scale

import csv_reader
import random
import matplotlib.pyplot as plt
import numpy as np
import math
import statistics
import collections


def rsd(l):
    ''' Returns the relative standard deviation '''
    sd = statistics.pstdev(l)
    mean = statistics.mean(l)

    return (sd*100/mean)

def related_attributes(features,target):
    ''' Returns a list of correlated attributes - each list item is a tuple '''
    n_features = len(features[0])
    complete_list = []
    list_of_correlated_attr = []
    
    for i in range(0,n_features):
        l = []
        for elem in features:
            l.append(float(elem[i]))
        complete_list.append(l)
        
    for i in range(0,n_features):
        for j in range(i,n_features):
            if i != j:
                g = pearsonr(complete_list[i],complete_list[j])
                if (g[0] > 0.8) or (g[0] < -0.8):
                    print i,j,g
                    list_of_correlated_attr.append((i,j))

    return list_of_correlated_attr
                    
                

def get_data_stat(features,target):

    #### Check for class imbalance problem ####
    n = len(target)
    counter = collections.Counter(target)
    for i in counter.keys():
        print (counter[i]/float(n))*100

    #### RSD of features ####
    n_features = len(features[0])
    
    
    for i in range(0,n_features):
        l = []
        for elem in features:
            
            l.append(float(elem[i]))
        print i,statistics.pstdev(l)
    ### Pearson co-eff ###
    related_attributes(features,target)

    

        
def remove_correlated_attributes(features,tupl):
    ''' Returns a list of features after removing specified correlated attributes '''
    for item in features:
        item.pop(tupl[1])
    return features
    
    
def plot(X,Y,x_label,y_label):

    plt.plot(X,Y,'ro')
    #plt.plot(X,Y,X,[np.mean(Y)]*len(X),'r--') ##'ro' for dots, 'r--' for line
    #plt.axis([0,max(X),0,1])
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.show()
    


def create_dataset(data,invert):
    ''' Returns Features and Targets '''

    ## By default, class label is the last attribute. invert=1 specifies the first attribute to be the class label ##

    features = []
    target = []
    n = len(data[0])
     
    if invert == 0:
        features = [x[:n-1] for x in data] ## Last attribute is the class label
        features_new = []
        for i in features:
            features_new.append([float(t) for t in i])
            
        target = [float(x[n-1]) for x in data]
    else:
        features = [x[1:n] for x in data]  ## First attribute is the class label
        features_new = []
        for i in features:
            features_new.append([float(t) for t in i])
        target = [float(x[0]) for x in data]
    
    return features_new,target
        
    
def task(filename):
    data = csv_reader.read_csv(filename)
    
    
    n = len(data[0])
    
    features,target = create_dataset(data,1) ## Default is 0 (1 for invert)

    #features = scale(features)

    Y = []
    X = []

    get_data_stat(features,target)

    #### FIRST PLOT : Accuracy VS. Number of Classifiers ####
##
##    for i in range(5,100):
##        train_features,test_features,train_target,test_target = train_test_split(features,
##                                                     target,
##                                                     test_size=0.7,
##                                                     random_state=random.randint(0,100))
##
##        
##        Y.append(ensemble(train_features,test_features,train_target,test_target,15))
##        X.append(i)
##
##    plot(X,Y,"Number of Classifiers","Accuracy")
##
##    X = []
##    Y = []
##
##    lst = related_attributes(features,target)
##    features = remove_correlated_attributes(features,lst[2])
##
##    for i in range(5,100):
##        train_features,test_features,train_target,test_target = train_test_split(features,
##                                                     target,
##                                                     test_size=0.7,
##                                                     random_state=random.randint(0,100))
##
##        
##        Y.append(ensemble(train_features,test_features,train_target,test_target,15))
##        X.append(i)
##
##    plot(X,Y,"Number of Classifiers","Accuracy")
##
##    plt.show()
    #### SECOND PLOT : Accuracy VS. Test/Train split ####

##    rnge = map(lambda t: t/100.0, range(10, 100, 2))
##    
##    for i in rnge:
##        train_features,test_features,train_target,test_target = train_test_split(features,
##                                                     target,
##                                                     test_size=i,
##                                                     random_state=random.randint(0,100))
##
##        
##        Y.append(ensemble(train_features,test_features,train_target,test_target,15)) ## Fixed number of classifiers
##        X.append(i)
##
##    plot(X,Y,"Test Sample Size","Accuracy")


### SVM - THREE SUB-ITERATIONS PER ITERATION FOR A GIVEN PARAMETER VALUE ###
##    for i in range(15,200):
##        train_features,test_features,train_target,test_target = train_test_split(features,
##                                                     target,
##                                                     test_size=0.7,
##                                                     random_state=random.randint(0,100))
##
##        iter_1 = svm_poly(train_features,test_features,train_target,test_target,i)
##        iter_2 = svm_poly(train_features,test_features,train_target,test_target,i)
##        iter_3 = svm_poly(train_features,test_features,train_target,test_target,i)
##        
##        Y.append((iter_1+iter_2+iter_3)/3.0)
##        X.append(i)
##
##    print X
##    print Y
##    plot(X,Y,"Degree","Accuracy (SVM_POLY)")


################# K MEANS / PCA #####################
##    kmeans  = KMeans(init='k-means++',max_iter=300)
##    kmeans.fit(data)
##
##    reduced_data = PCA(n_components=2).fit_transform(data)
##    print len(reduced_data)
##    plot([i[0] for i in reduced_data],[i[1] for i in reduced_data], "", "")

    related_attr = related_attributes(features,target)
    
    

    


    


def print_metrics(test_target,test_predicted):
    
    return [metrics.classification_report(test_target,test_predicted),
            metrics.confusion_matrix(test_target,test_predicted),
            metrics.accuracy_score(test_target,test_predicted)]
    
    
def ensemble(train_features,test_features,train_target,test_target,estimators):
    

    clf = RandomForestClassifier(n_estimators=estimators,
                                 bootstrap = True,
                                 random_state = random.randint(0,100))

    clf.fit(train_features,train_target)

    test_predicted = clf.predict(test_features)

    #correct = 0
    #for i in range(0,len(test_features)):

    #    a = clf.predict(test_features[i])
    #    print a[0],test_target[i]
    #    if int(a[0]) == int(test_target[i]):
    #        correct += 1
    #print correct/float(len(test_features))
    
    return print_metrics(test_target,test_predicted)[2] ## To decide which metric to be returned
 


def d_tree(train_features,test_features,train_target,test_target,criteria,split):

    clf = tree.DecisionTreeClassifier(criterion=criteria,
                                      splitter=split)
    clf.fit(train_features,train_target)

    test_predicted = clf.predict(test_features)

    print_metrics(test_target,test_predicted)

def knn(train_features,test_features,train_target,test_target):

    k = KNeighborsClassifier(metric='minkowski',n_neighbors=3,p=4)
    k.fit(train_features,train_target)

    test_predicted = k.predict(test_features)

    print_metrics(test_target,test_predicted)

def svm_linear(train_features,test_features,train_target,test_target):
    ''' Painfully slow - Make changes to the cache size and other parameters '''
    
    s = svm.SVC(kernel='linear',
                multi_class='crammer_singer',
                cache_size=1000)
    s.fit(train_features,train_target)
    test_predicted = s.predict(test_features)

    print_metrics(test_target,test_predicted)

def svm_poly(train_features,test_features,train_target,test_target,degree_):
    
    s = svm.SVC(kernel='poly',
                degree=degree_,
                cache_size=1000)
    s.fit(train_features,train_target)
    test_predicted = s.predict(test_features)
    
    return (print_metrics(test_target,test_predicted)[2])
    
    

if __name__=="__main__":
    
    task("path to csv file")
    

    
