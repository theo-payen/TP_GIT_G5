import list_nombre
import  clone_repo 

print ("1: clone repo")
print ("2: list nombre")
print ("selectionner votre options")
choix = input(">")
print (choix)
if choix == "1" :
    print ("saisir votre url")
    url = input(">")
    clone_repo.clone(url)
elif choix == "2" :
    print("saisir votre nombre minimal")
    min = input(">")
    print("saisir votre nombre maximal")
    max = input(">")
    list_nombre.compteurNb(int(min),int(max))
else:
    print ("error votre nombre ne correspond pas")