import csv
import numpy as np
import matplotlib.pyplot as plt

def import_data():
    E=[]
    N=[]
    with open("C:\\Users\\Lucien Marey\\Downloads\\gnutella.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            E.append(row)
            if row[0] not in N:
                N.append(row[0])
            if row[1] not in N:
                N.append(row[1])
    return(E,N)
    
E,N = import_data()

def adjacency_matrix(E,N):
    A = np.zeros((len(N),len(N)))
    for edge in E:
        i,j=int(edge[0]), int(edge[1])
        A[i-1,j-1] += 1
        A[j-1,i-1] += 1
    return A
    
A = adjacency_matrix(E,N)

def CCDF(A):
    S = sum(A)
    Nb = len(S)
    x=[]
    y=[]
    last = 0
    for i in range(int(max(S))):
        x.append(i)
        temp=0
        for element in S:
            if element==i:
                temp += 1
        y.append(1-(temp/Nb+last))
        last = 1-y[-1]
    plt.figure()
    plt.plot(x,y)
    plt.xlabel("degree")
    plt.ylabel("probability")
    plt.show()

def ClusteringCoefficient(A):
    """
    Very inefficient but works
    """
    Nb = len(A)
    num = 0
    den = 0
    for i in range(Nb):
        ki = 0
        for j in range(Nb):
            ki += A[i,j]
            for k in range(Nb):
                num += A[i,j] * A[j,k] * A[k,i]
        den += ki*(ki-1)
    return(num/den)
    
def random_walk(A):
    S = sum(A)
    samples = []
    for seed in range(5):
        sample=[]
        node = np.random.randint(len(S))
        for step in range(400):
            neighbours = []
            for index,point in enumerate(A[node]):
                if point == 1:
                    neighbours.append(index)
            sample.append(S[node])
            node = np.random.choice(neighbours)
        samples.append(sample)
    plot_sample(samples)
    
def MCMC(A):
    S = sum(A)
    samples = []
    for seed in range(5):
        sample=[]
        node = np.random.randint(len(S))
        for step in range(400):
            neighbours = []
            for index,point in enumerate(A[node]):
                if point == 1:
                    neighbours.append(index)
            sample.append(S[node])
            temp_node = np.random.choice(neighbours)
            a = min(1,S[node]/S[temp_node])
            if np.random.binomial(1, a):
                node = temp_node
        samples.append(sample)
    plot_sample(samples)

    
    
def plot_sample(L):
    plt.figure()
    for i,sample in enumerate(L):
        y = [0]*(int(max(sample))+1)
        for node in sample:
            y[int(node)] += 1
        plt.plot(y,label="sample"+str(i))
    plt.legend()
    plt.show()
    
    
    
    
    
    