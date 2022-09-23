from time import sleep as wait
import itertools
import os
class color:
    global pallet
    global logo
    pallet = [
        '\033[1;31m',
        '\033[1;32m',
        '\033[1;33m',
        '\033[1;34m'
    ]
    logo = """
    

{0} __    __              _ _ _     _   _           _ _     _           
{0}/ / /\ \ \___  _ __ __| | (_)___| |_| |__  _   _(_) | __| | ___ _ __ 
{0}\ \/  \/ / _ \| '__/ _` | | / __| __| '_ \| | | | | |/ _` |/ _ \ '__|
{0} \  /\  / (_) | | | (_| | | \__ \ |_| |_) | |_| | | | (_| |  __/ |   
{0}  \/  \/ \___/|_|  \__,_|_|_|___/\__|_.__/ \__,_|_|_|\__,_|\___|_|   

                                        {1}   Coded by Devil                                               

    
    """.format(pallet[1],pallet[2])

if __name__ == '__main__':
    print(logo)
    chrs = 'ABCDEFGHIJKLMOPQSTUVWXYZabcdefghijlmnopqrstuvwxyz0123456789@!#\|][}{"`~$%^&*()_-+=,<.>/?'
    mini = int(input("{0}Minimum password length [{2}Only type number{0}] : {1}".format(pallet[2],pallet[3],pallet[0])))
    maxlen = int(input("{0}Max password length [{2}Only type number{0} : {1}".format(pallet[2],pallet[3],pallet[0])))
    output = input("{0}Output file name [ {2}Saving File Name, Default = outuput.txt{0} ] : {1}".format(pallet[2],pallet[3],pallet[0])) 
    if len(output) == 0:
        output = 'outuput.txt'
    else:
        pass
    if os.path.exists(output):
        open(output, 'w').close()
    else:
        pass
    print("\033[1;32m This May take while Please wait ......")
    wait(2)
    for n in range(mini,maxlen+1):
        for xs in itertools.product(chrs, repeat=n):
            lines = (''.join(xs))
            #print(lines)
            with open(output, 'a') as f:
               f.write('%s\n'%(lines))
