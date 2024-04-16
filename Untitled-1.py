

print ('Vítejte v obchodě počítačových komponentů')

print ('Zde máte na výběr grafické karty')

           #1           #2          #3         #4            #5

zbozi = ['GTX 1660', 'RTX 2070', 'RTX 3060', 'RTX 4080', 'AMD RX 7800']
kosik = []

def vypis_zbozi():
print('Zde je zboží')


def vypis_kosik():
print('Zde je váš košík')


def vypis_pole(prvek):

    for x in range (len(prvek)):
    
    print('Komponent s číslem') (x+1): (prvek(x))

        While(True)
        vypis_zbozi()
        vypis_pole(zbozi)

vyber = int(input)('Zde zadejte vaši volbu')
    
    if 0 < vyber <= len(zbozi):
    kosik.append(zbozi[vyber])
    vypis_kosik()
    vypis_pole(kosik)
    

        
        
           



