character_possibles = ['a',"b",'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',0,1,2,3,4,5,6,7,8,9]
fichier = open("wordlist.txt", "w")

for i in range(0,len(character_possibles)):
    for j in range(0,len(character_possibles)):
        for k in range(0,len(character_possibles)):
            for l in range(0,len(character_possibles)):
                for m in range(0,len(character_possibles)):
                    fichier.write(str(character_possibles[i]))
                    fichier.write(str(character_possibles[j]))
                    fichier.write(str(character_possibles[k]))
                    fichier.write(str(character_possibles[l]))
                    fichier.write(str(character_possibles[m]))
                    fichier.write("\n")
fichier.close()
############## ATTENTION!!! N'executez ce script que si votre PC a la puissance Nécessaire
