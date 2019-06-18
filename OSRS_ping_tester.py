''' ***** PING TESTER MADE BY @AWN3ST ON ALL PLATFORMS *****

    I am not a good programmer by any means, everything written in this program
has been self-taught from the knowledge I've acquired over the past 3 months
on python since I started coding. I understand the code looks very sloppy in
terms of industry standards, but I'm hoping to make it look better overtime as
I become more familiar/skilled at programming. With that said, I hope you do
appreciate the work and effort I've put into this project thus far!'''




from pythonping import ping
import sys
from operator import itemgetter
import collections
import time


#Tests NA servers
def NA_pings(): 
    avg_pings = []
    servers = open('NA_servers.txt','r')
    all_servers = [line.strip() for line in servers]
    f2p_servers = []
    p2p_servers = []

    #Tests NA f2p servers if user input = f2p
    for free in all_servers:
        if free.startswith('f2p'):
            f2p_servers.append(free)
            f2p_servers = [line.strip('f2p.') for line in f2p_servers]
    f2p_world_numbers = [line.strip('f2p.oldschool.runescape.com') for line in f2p_servers]

    #Tests NA p2p servers if user input = p2p
    for pay in all_servers:
        if pay.startswith('p2p'):
            p2p_servers.append(pay)
            p2p_servers = [line.strip('p2p.') for line in p2p_servers]
    p2p_world_numbers = [line.strip('oldschool.runescape.com') for line in p2p_servers]
    

    ask_user = input('\nWould you like to test f2p or p2p worlds? ')
    ask_user = ask_user.lower()
    if ask_user == 'p2p':
        print('\nTesting NA P2P worlds... Please be patient...')
        for x in p2p_servers:
            if not x:
                continue                
            result = ping(x, count = 3)
            avg_pings.append(result.rtt_avg_ms)
        ping_worlds = dict(zip(p2p_world_numbers, avg_pings))

    elif ask_user == 'f2p':
        print('\nTesting NA F2P worlds... Please be patient...')
        for z in f2p_servers:
            if not z:
                continue
            result = ping(z, count = 3)
            avg_pings.append(result.rtt_avg_ms)
        ping_worlds = dict(zip(f2p_world_numbers, avg_pings))

    
    best_10 = sorted(ping_worlds.items(), key=lambda kv: kv[1])
    print(f'\nYour top worlds to play on are (WORLD, PING):\n {best_10[0:10]}\n')
    world, lowest_ping = min(ping_worlds.items(), key = itemgetter(1))
    print(f'Your best world is: w{world} with a ping of {lowest_ping}ms.')


#Tests EU servers
def EU_pings():
    avg_pings = []
    servers = open('EU_servers.txt','r')
    all_servers = [line.strip() for line in servers]
    f2p_servers = []
    p2p_servers = []
    
    #Tests EU f2p servers if user input = f2p
    for free in all_servers:
        if free.startswith('f2p'):
            f2p_servers.append(free)
            f2p_servers = [line.strip('f2p.') for line in f2p_servers]
    f2p_world_numbers = [line.strip('f2p.oldschool.runescape.com') for line in f2p_servers]

    #Tests EU p2p servers if user input = p2p
    for pay in all_servers:
        if pay.startswith('p2p'):
            p2p_servers.append(pay)
            p2p_servers = [line.strip('p2p.') for line in p2p_servers]
    p2p_world_numbers = [line.strip('oldschool.runescape.com') for line in p2p_servers]
    

    ask_user = input('\nWould you like to test f2p or p2p worlds? ')
    ask_user = ask_user.lower()
    if ask_user == 'p2p':
        print('\nTesting EU P2P worlds... Please be patient...')
        for x in p2p_servers:
            if not x:
                continue                
            result = ping(x, count = 3)
            avg_pings.append(result.rtt_avg_ms)
        ping_worlds = dict(zip(p2p_world_numbers, avg_pings))

    elif ask_user == 'f2p':
        print('\nTesting EU F2P worlds... Please be patient...')
        for z in f2p_servers:
            if not z:
                continue
            result = ping(z, count = 3)
            avg_pings.append(result.rtt_avg_ms)
        ping_worlds = dict(zip(f2p_world_numbers, avg_pings))

    
    best_10 = sorted(ping_worlds.items(), key=lambda kv: kv[1])
    print(f'\nYour top worlds to play on are (WORLD, PING):\n {best_10[0:10]}\n')
    world, lowest_ping = min(ping_worlds.items(), key = itemgetter(1))
    print(f'Your best world is: w{world} with a ping of {lowest_ping}ms.')


#Tests AUS servers'''
def AUS_pings():
    avg_pings = []
    servers = open('AUS_servers.txt','r')
    all_servers = [line.strip() for line in servers]
    f2p_servers = []
    p2p_servers = []

    for free in all_servers:
        if free.startswith('f2p'):
            f2p_servers.append(free)
            f2p_servers = [line.strip('f2p.') for line in f2p_servers]
    f2p_world_numbers = [line.strip('f2p.oldschool.runescape.com') for line in f2p_servers]

    #Tests AU p2p servers if user input = p2p
    for pay in all_servers:
        if pay.startswith('p2p'):
            p2p_servers.append(pay)
            p2p_servers = [line.strip('p2p.') for line in p2p_servers]
    p2p_world_numbers = [line.strip('oldschool.runescape.com') for line in p2p_servers]
    

    ask_user = input('\nWould you like to test f2p or p2p worlds? ')
    ask_user = ask_user.lower()
    if ask_user == 'p2p':
        print('\nTesting AUS p2p worlds... please be patient...')
        for x in p2p_servers:
            if not x:
                continue                
            result = ping(x, count = 3)
            avg_pings.append(result.rtt_avg_ms)
        ping_worlds = dict(zip(p2p_world_numbers, avg_pings))

    #Test AU f2p servers if user input = f2p
    elif ask_user == 'f2p':
        print('\nTesting AUS f2p worlds... Please be patient...')
        for z in f2p_servers:
            if not z:
                continue
            result = ping(z, count = 3)
            avg_pings.append(result.rtt_avg_ms)
        ping_worlds = dict(zip(f2p_world_numbers, avg_pings))

    
    best_10 = sorted(ping_worlds.items(), key=lambda kv: kv[1])
    print(f'\nYour top worlds to play on are (WORLD, PING):\n {best_10[0:10]}\n')
    world, lowest_ping = min(ping_worlds.items(), key = itemgetter(1))
    print(f'Your best world is: w{world} with a ping of {lowest_ping}ms.')

    

#Asks user to select their region and calls the function of that region and after testing, asks user if they would like to test again.
def main():
    region = input("Welcome to AWN3ST's Old School Runescape ping tester! To begin, please type what region you are from (AUS, EU, NA): ")
    region = region.lower()
    while True:
        if region == 'na': 
            NA_pings()
            while True:
                region = input('Would you like to test again? (Y/N): ')
                region = region.lower()
                if region == 'y':
                    NA_pings()
                elif region != 'y':
                    quit()
            
        elif region == 'eu':
            EU_pings()
            while True:
                region = input('Would you like to test again? (Y/N): ')
                region = region.lower()
                if region == 'y':
                    print('\nTesting EU worlds again... Please be patient...\n')
                    NA_pings()
                elif region != 'y':
                    quit()
            
        elif region == 'aus':
            AUS_pings()
            while True:
                region = input('\nWould you like to test again? (Y/N): ')
                region = region.lower()
                if region == 'y':
                    AUS_pings()
                elif region != 'y':
                    quit()
        else: 
            region = input('\nYou did not enter a valid region, please enter either AUS, EU, or NA:') #If user doesn't enter a valid region
            region = region.lower()
            
main()
