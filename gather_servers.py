#Gathers AUS servers into a txt file
def gather_AUS():
    with open('AUS_servers.txt','w') as f:
            listOne = list(range(87,93)) + list(range(124,128)) + list(range(226,235))
            servers = [f'oldschool{i}.runescape.com\n' for i in listOne]
            for x in servers:
                f.write(x)
gather_AUS()


#Gathers NA servers into a txt file
def gather_NA():
    with open('NA_servers.txt','w') as f:
            listOne = [6,7,13,15,19,20,23,24,31,32,38,40,47,48,55,56,57,74,78,118,119,120,121,122,128,
                       129,130,131,132,133,134,135,136,137,138,139,140,143,144,145,146,1,5,14,21,22,29,
                       30,37,45,46,53,54,61,62,69,70,77,85,86,93,94,115,116,117,167,168,169,170,171,
                       172,173,174,175,176,177,191,192,193,194,195,196,100]
            servers = [f'oldschool{i}.runescape.com\n' for i in listOne]
            for x in servers:
                f.write(x)
gather_NA()


#Gathers EU servers into a txt file
def gather_EU():
    with open('EU_servers.txt','w') as f:
            listOne = [2,8,9,10,16,17,18,25,26,33,34,41,42,49,50,58,64,65,66,71,72,73,79,80,81,82,197,
                       198,199,200,201,202,203,204,212,213,214,215,216,217,218,219,220,221,222,223,224,
                       225,3,4,11,12,27,28,35,36,43,44,51,52,59,60,67,68,75,76,83,84,95,96,97,98,99,113,
                       114,147,148,149,150,151,152,153,154,155,156,157,158,159,163,164,165,166]
            servers = [f'oldschool{i}.runescape.com\n' for i in listOne]
            for x in servers:
                f.write(x)
gather_EU()
        

        
