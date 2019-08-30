with open("nyc.txt","r") as f:
    f  = f.readlines()
    #print(f)
    memory = {}
    D = {}
    
    for l in f:
        l = l.strip() # clean the data
        l = l.split(',')
        memory[l[0]] = l[1:]
    #print(memory)
    
    
    total = 0
    highest = 0

    for states in memory:
        data2 = memory[states]
        for x in data2:
            if x in D.keys():
                D[x] = D[x] + 1
            else:
                if x != '':
                    D[x] = 1
                    total = total + 1

    datas = ''
    #print(D)
    for b in D:
        if highest < D[b]:
            highest = D[b]
            datas = b
            
    print('-----------')
    for c in D:
        print(c,': ', D[c])
    
    print('-----------')
    print('total states:' ,total)
    print('The city which returned many time is: ',datas, ': ',D[datas])
    print("gabby challenge")