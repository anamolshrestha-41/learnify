import numpy as np

def preprocess(data):
    print('---PreProcessing Started---')
    #Indexing
    print(f'First Student: {data[0]}')
    print(f'Last Student: {data[-1]}')
    #column indexing 
    print(f'Age: {data[:, 0]}')
    print(f'MidTerm: {data[:, 6]}')
    #Slicing
    print(f' First 20: {data[:20]}')
    print(f'Columns up to 10: {data[:,0:9]}')
    #searching
    good= np.where(data[:,6]>40)
    print(f'40 Above MidTerm Marks: {good}')
    #filter
    finalGood= data[data[:,7]>80]
    print(f'Good final Marks: {finalGood} ')
    #sorting
    sortedData= data[data[:, 2].argsort()]
    print(f'Data sorted according to the attendance: {sortedData}')
    #Reshape
    age= data[:, 0]
    age= age.reshape(-1,1) #converting
    age=age.flatten() #flatten
    #copy
    copyData= data.copy()
    viewData= data.view()
    viewData[0,0]= 99 #modifying
    #iterate
    for stu in data[:10]:
        print(stu)

    return data   