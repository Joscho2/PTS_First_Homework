import hashlib
import getpass
import sys

def str_encode(string):
    return string.encode('utf-8')

#Získa heslo z terminálu
def zisti_heslo():
    return getpass.getpass('Zadajte heslo: ')

#Vypýta si heslo a porovná ho s heslom v pamäti
def vstup_heslo():
       return ulozene_heslo.hexdigest() == hashlib.sha512(str_encode(zisti_heslo())).hexdigest()

#hracovi name prida number bodov (ak neexistuje, prida ho do zoznamu s name bodmi)
#parameter je slovnik d, name sa ziska ako d[1], number ako d[2]
def cmd_points(d):
    name = d[1]
    number = d[2]
    if name not in hrac:
        hrac[name] = int(number)
    else:
        hrac[name] += int(number)

#parameter je slovnik d, number sa ziska ako d[1]
def cmd_reduce(d):
    number = d[1]
    for h in hrac: hrac[h] -= int(number)

#parameter je slovnik d, name sa ziska ako d[1]
def cmd_junior(d):
    name = d[1]
    if name not in hrac:
        print("Hrac nenájdený!")
        return
    if name not in junior: junior.append(name)

#parameter je slovnik l, ak je v slovniku nejake slovo vola sa funkcia rank_junior,
#inak rank all (mohlo by sa kontrolovať, či je v slovniku prave jedno slovo a ci je to
#slovo "junior", inak by mohlo hodiť chybu)
def cmd_ranking(l):
    if len(l) >= 1:
        rank_junior()
    else:
        rank_all()

#vypíše poradie medzi všetkými hráčmi, utriedene od najväčšieho
def rank_all():
    for name in sorted(hrac, key = hrac.get, reverse = True):
        print(name, hrac[name])

#vypíše poradie juniorov, utriedene od najväčšieho
def rank_junior():
    for j in sorted(filter(lambda x:x in junior, hrac), key = hrac.get, reverse = True):
        print(j, hrac[j])

#ukončí program bez ohľadu na parametre
def quit(d):
    exit()

#################################  

#uložené zahešované heslo
ulozene_heslo = hashlib.sha512(str_encode(zisti_heslo())); 

#list v slúži na spracovanie vstupu
v = []

#reprezentácia hráčov v pamäti
hrac = {}

#označenie hráčov, ktorí sú juniori
junior = []

#slovník, slúžiaci na použitie správnej funkcie podľa vstupu
command = {
    'points' : cmd_points,
    'reduce' : cmd_reduce,
    'junior' : cmd_junior,
    'ranking': cmd_ranking, 
    'quit' : quit
}
while True:
    #dekorácia terminálu
    sys.stdout.write('$ ')
    sys.stdout.flush()

    #načítavanie a spracovanie vstupu
    v = input().split()
    #ak je to neznámi príkaz hneď to dáme užívateľovi vedieť (nebudeme pýtať heslo)
    if v[0] in command.keys():
    	#ak je príkaz iný ako ranking, používateľ musí zadať heslo
        if v[0] == 'ranking' or vstup_heslo():
            try:
	        #volanie funkcie podľa užívateľom zadaného príkazu
		#parameter je slovník, v ktorom sa nachádza všetko čo je na vstupe
		#(čo bolo oddelené medzerou), kľúče slovníka sú v podstate "indexy"
		#(0 je samotný príkaz, 1,2,... nasledujúce slová v poradí v akom sú na
		# vstupe)
                command[v[0]](dict((i, v[i]) for i in range(1, len(v))))
            except KeyError:
                print("Neplatný vstup!")
            except ValueError:
                print("Zle uvedené argumenty!")
        else:
            print('Nesprávne heslo!')
    else:
        print("Neznámy príkaz " + v[0])
