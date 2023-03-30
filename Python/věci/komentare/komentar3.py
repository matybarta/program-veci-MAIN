#zjistí zdali je řetězec symetrický nebo palindrome

#definování funkce palindrome, která zjistí jestli je string palindrome nebo ne
def palindrome(a):
    #definování proměnné mid
    mid = (len(a)-1)//2   
    #definování proměnné start
    start = 0               
    #definování proměnné last
    last = len(a)-1
    #definování proměnné flag
    flag = 0
    #cyklus který zjistí jestli se slovo dá číst z obou stran
    while(start <= mid):
        #podmínka která říká jestli slovo má na obou stranách stejný znak, tak ať zkontroluje další znak dokud nezkontroluje všechny znaky a nebo aby ukončila kontrolování znaků pokdu se znaky nebudou rovnat sami sobě
        if (a[start]== a[last]):
            #zkontroluje další písmeno
            start += 1
            #zkontroluje předešlé písmeno jelikož se to bere od konce
            last -= 1
             
        else:
            #prostě pokud to neni palindrome tak to neni palindrome a přestane to kontrolovat
            flag = 1
            break;
    #podmínka která říká jestli se slovo dá přečíst z obou stran ať napíše, že se dá... Jinak ať napíše, že se nedá
    if flag == 0:
        #vytiskne jestli je string palindrome
        print("Zadaný řetězec je palindrome")
    else:
        #vytiskne jestli string neni palindrome
        print("Zadaný řetězec není palindrome")

#definování funkce symmetry, která zjistí jestli je string symetrický nebo ne      
def symmetry(a):
    #definování n jako počet písmen ve slově
    n = len(a)
    #definuje hodnotu flag jako 0
    flag = 0
    #podmínka která říká jestli délka slova má nějaký zbytek
    if n%2:
        #deklarace proměnné mid která celočíselně vydělí délku slova 2 a přičte k tomu 1
        mid = n//2 +1
    else:
        #pokud slovo nemá zbytek, celočíselně se to vydělí 2
        mid = n//2
         
    #definování proměnná start1
    start1 = 0
    #definování proměnné start2 která je mid
    start2 = mid
    #cyklus který se bude opakovat dokud start bude menší než mid a zároveň start2 bude menší jak délka slova 
    while(start1 < mid and start2 < n):
        #pokud první písmeno je stejné jako prostřední písmeno tak se k start1 a start2 přičte 1 (jako jít na další písmeno)
        if (a[start1]== a[start2]):
            #start1 se změní na součet start1 a 1
            start1 = start1 + 1
            #start2 se změní na součet start2 a 1
            start2 = start2 + 1
        #pokud se první písmeno nerovná prostřednímu písmenu tak to přestane fakat a flag se změní na 1
        else:
            #definuje proměnnou flag jako 1
            flag = 1
            #přestane fakat cyklus
            break
    #podmínka která říká jestli je slovo symetrický ať napíše, že je... A pokud neni ať napíše, že neni
    if flag == 0:
        #vypíše, že string je symetrický
        print("Zadaný řetězec je symetrický")
    else:
        #vypíše, že string neni symetrický
        print("Zadaný řetězec není symetrický")

#DEFINOVÁNÍ STRINGU
string = 'amaama'
#napíše jestli string je palindrome nebo ne
palindrome(string)
#napíše jestli string je symetrický nebo ne
symmetry(string)