# these codes can be combined into one loop
with open("data.txt","r") as f:
    f  = f.readlines()
    #print(f)
    memory = {}
    D = {}
    
    # put elements into a dictionary
    for l in f:
        l = l.strip() # clean the data
        l = l.split(' ')
        memory[l[0]] = l[1:]
    
    
    total = 0 
    highest = 0

    # find the times the state occur in a  file
    for states in memory:
        data2 = memory[states]
        for x in data2:
            if x in D.keys():
                D[x] = D[x] + 1
            else:
                D[x] = 1
                total = total + 1

    datas = ''
    
    # find the state which occur many times in the list
    for b in D:
        if highest < D[b]:
            highest = D[b]
            datas = b
            
    
    print('-----------')
    
    # printing elements from the dictionary 
    for c in D:
        print(c,': ', D[c])
    
    print('-----------')
    print('total states:' ,total)
    print('The city which returned many time is: ',datas, ': ',D[datas])