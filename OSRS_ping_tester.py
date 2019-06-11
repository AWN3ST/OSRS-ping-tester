''' ***** PING TESTER MADE BY @AWN3ST ON ALL PLATFORMS *****

    I am not a good programmer by any means, everything written in this program
has been self-taught from the knowledge I've acquired over the past 3 months
on python since I started coding. I understand the code looks very sloppy in
terms of industry standards, but I'm hoping to make it look better overtime as
I become more familiar/skilled at programming. With that said, I hope you do
appreciate the work and effort I've put into this project thus far!

'''


from pythonping import ping
import sys
from operator import itemgetter
import collections
import time


#Tests NA servers
def NA_pings(): 
    avg_pings = []
    servers = open('NA_servers.txt','r')
    list_servers = [line.strip() for line in servers]
    world_numbers = [line.strip('oldschool.runescape.com') for line in list_servers]
    ping_worlds = dict(zip(world_numbers, avg_pings))
    
    for x in list_servers:
        if not x:
            continue                
        A = ping(x, count = 3)
        avg_pings.append(A.rtt_avg_ms)
    ping_worlds = dict(zip(world_numbers, avg_pings))

    
    best_5 = sorted(ping_worlds.items(), key=lambda kv: kv[1])
    print(f'\nYour top 10 worlds to play on are (WORLD, PING):\n {best_5[0:10]}\n')
    world, lowest_ping = min(ping_worlds.items(), key = itemgetter(1))
    print(f'Your best world is: w{world} with a ping of {lowest_ping}ms.')


#Tests EU servers
def EU_pings():
    avg_pings = []
    servers = open('EU_servers.txt','r')
    list_servers = [line.strip() for line in servers]
    world_numbers = [line.strip('oldschool.runescape.com') for line in list_servers]
    ping_worlds = dict(zip(world_numbers, avg_pings))
    
    for x in list_servers:
        if not x:
            continue                
        A = ping(x, count = 3)
        avg_pings.append(A.rtt_avg_ms)
    ping_worlds = dict(zip(world_numbers, avg_pings))

    
    best_5 = sorted(ping_worlds.items(), key=lambda kv: kv[1])
    print(f'\nYour top 10 worlds to play on are (WORLD, PING):\n {best_5[0:10]}\n')
    world, lowest_ping = min(ping_worlds.items(), key = itemgetter(1))
    print(f'Your best world is: w{world} with a ping of {lowest_ping}ms.')


#Tests AUS servers
def AUS_pings():
    avg_pings = []
    servers = open('AUS_servers.txt','r')
    list_servers = [line.strip() for line in servers]
    world_numbers = [line.strip('oldschool.runescape.com') for line in list_servers]
    ping_worlds = dict(zip(world_numbers, avg_pings))
    
    for x in list_servers:
        if not x:
            continue                
        A = ping(x, count = 3)
        avg_pings.append(A.rtt_avg_ms)
    ping_worlds = dict(zip(world_numbers, avg_pings))

    
    best_5 = sorted(ping_worlds.items(), key=lambda kv: kv[1])
    print(f'\nYour top 10 worlds to play on are (WORLD, PING):\n {best_5[0:10]}\n')
    world, lowest_ping = min(ping_worlds.items(), key = itemgetter(1))
    print(f'Your best world is: w{world} with a ping of {lowest_ping}ms.')
    

#Asks user to select their region and calls the function of that region and after testing, asks user if they would like to test again.
def main():
    region = input("Welcome to AWN3ST's Old School Runescape ping tester! To begin, please type what region you are from (AUS, EU, NA): ")
    region = region.lower()
    while True:
        if region == 'na': 
            print('\nTesting NA worlds... Please be patient...\n')
            NA_pings()
            while True:
                region = input('Would you like to test again? (Y/N): ')
                region = region.lower()
                if region == 'y':
                    print('\nTesting NA worlds again... Please be patient...\n')
                    NA_pings()
                elif region != 'y':
                    quit()
            
        elif region == 'eu':
            print('\nTesting EU worlds... Please be patient...\n')
            EU_pings()
            while True:
                region = input('Would you like to test again? (Y/N): ')
                region = region.lower()
                if region == 'y':
                    print('\nTesting EU worlds again... Please be patient...\n')
                    EU_pings()
                elif region != 'y':
                    quit()

        elif region == 'aus':
            print('\nTesting AUS worlds... Please be patient...\n')
            AUS_pings()
            while True:
                region = input('Would you like to test again? (Y/N): ')
                region = region.lower()
                if region == 'y':
                    print('\nTesting AUS worlds again... Please be patient...\n')
                    AUS_pings()
                elif region != 'y':
                    quit()
        else: 
            region = input('\nYou did not enter a valid region, please enter either AUS, EU, or NA:') #If user doesn't enter a valid region
            region = region.lower()
            
main()
