import hashlib


#################################
def str_encode(string):
    return string.encode('utf-8')

def zisti_heslo():
    return input('Zadajte heslo: ')
	
def vstup_heslo():
       return ulozene_heslo.hexdigest() == hashlib.sha512(str_encode(zisti_heslo())).hexdigest()

def error():
    print("Neplatný vstup!")

def cmd_points(d):
    name = d[1]
    number = d[2]
    print("Points " + name + " " + number)

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
    print("All")

def rank_junior():
    print("Junior")
def quit(d):
    exit()
#################################  
 
ulozene_heslo = hashlib.sha512(str_encode(zisti_heslo())); 

v = []

command = {
    'points' : cmd_points,
    'reduce' : cmd_reduce,
    'junior' : cmd_junior,
    'ranking': cmd_ranking, 
    'quit' : quit
}
while True:
    v = input().split()  
    try:
        command[v[0]](dict((i, v[i]) for i in range(1, len(v))))
    except KeyError:
        error()     
