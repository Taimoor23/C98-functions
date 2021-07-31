def SwapFileData():
    file1=input("Enter your file name :  ")
    file2=input("Enter your file name :  ")

    with open(file1,'r') as sampleA:
        data_sampleA=sampleA.read()

    with open(file2, 'r') as sampleB:
        data_sampleB=sampleB.read()

    with open(file1, 'w') as sampleA:
       sampleA.write(data_sampleB)

    with open(file2, 'w') as sampleB:
       sampleB.write(data_sampleA)

        
SwapFileData()        
