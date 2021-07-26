def SwapFileData():
    file1=input("Enter your file name :  ")
    file2=input("Enter your file name :  ")

    with open(file1,'r') as sampleA:
        data_sampleA=sampleA.read()

    with open(fileTwoData, 'r') as sampleB:
        data_sampleB=sampleB.read()

    with open(fileOneData, 'w') as sampleA:
        data_sampleA.write(data_sampleB)

    with open(fileTwoData, 'w') as sampleB:
        data_sampleB.write(data_sampleA)

        
SwapFileData()        
