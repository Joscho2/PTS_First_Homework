import hashlib

def str_encode(string):
    return string.encode('utf-8')

def zisti_heslo():
    return input('Zadajte heslo: ')
	
def vstup_heslo():
       return ulozene_heslo.hexdigest() == hashlib.sha512(str_encode(zisti_heslo())).hexdigest()

def cmd_points(d):
    name = d[1]
    number = d[2]
    if name not in hrac:
        hrac[name] = int(number)
    else:
        hrac[name] += int(number)  
def cmd_reduce(d):
    number = d[1]
    print("Reduce " + number)

def cmd_junior(d):
    name = d[1]
    print("Junior " + name)

def cmd_ranking(l):
    if len(l) >= 1:
        rank_junior()
    else:
        rank_all()

def rank_all():
    for name, score in sorted(hrac.items()):
        print(name, score)
def rank_junior():
    print("Junior")
def quit(d):
    exit()

#################################  
 
ulozene_heslo = hashlib.sha512(str_encode(zisti_heslo())); 

v = []
hrac = {}

command = {
    'points' : cmd_points,
    'reduce' : cmd_reduce,
    'junior' : cmd_junior,
    'ranking': cmd_ranking, 
    'quit' : quit
}
while True:
    print('$')
    v = input().split()  
    if v[0] in command.keys():
        if v[0] == 'ranking' or vstup_heslo():
            try:
                command[v[0]](dict((i, v[i]) for i in range(1, len(v))))
            except KeyError:
                print("Neplatný vstup!")
        else:
            print('Nesprávne heslo!')
    else:
        print("Neznámy príkaz " + v[0])
