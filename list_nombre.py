#script pour le TP GIT 
#il doit afficher la liste des nombres premiers 
#acteurs @mohamed, @theo, @mukil 
def nombrepremier(n) :
    if n <= 1 :
        return False
    for i in range(2, n) :
        if (n % i == 0) :
            return False
    return True


def compteurNb(min, max):
    while min < max :
        min = min + 1
        if nombrepremier(min) == True:
            print (min)
