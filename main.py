import hashlib


#################################
def str_encode(string):
    return string.encode('utf-8')

def zisti_heslo():
    return input('Zadajte heslo: ')
	
def vstup_heslo():
       return ulozene_heslo.hexdigest() == hashlib.sha512(str_encode(zisti_heslo())).hexdigest()

def not_found(string):
    print("Príkaz \"" + string + "\" nenájdený!")

#################################  
  
#while True:
#   vstup = input.split(" ")
#    commnad = {
#        
#    }.get(vstup[0], not_found(vstup))

ulozene_heslo = hashlib.sha512(str_encode(zisti_heslo()));

print("Zadaj este raz heslo na otestovanie.")
print(vstup_heslo())
    
