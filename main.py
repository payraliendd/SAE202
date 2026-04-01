from arbreBinaire import *
from NoeudHuffman import *

def construction_arbre(table_effectif):
        #fin de récursivité quand il reste une valeur dans le liste (racine de l'arbre)
        if len(table_effectif) == 1:
            return table_effectif
        
        #Variables qui représentent la valeurs et l'effectif de la combinaison des 2 dernier tuples de la table des effectifs
        somme_valeur = table_effectif[-1][0] + table_effectif[-2][0]
        somme_effectif = table_effectif[-1][1] + table_effectif[-2][1]

        #On créé le noeud avec la branche et les 2 sous branches
        a = NoeudHuffman((somme_valeur,somme_effectif),(table_effectif[-2][0],table_effectif[-2][1]),(table_effectif[-1][0],table_effectif[-1][1]))
        print(a)
        
        #On supprime les 2 dernières valeurs
        table_effectif.pop()
        table_effectif.pop()

        insertion = False #variable qui vérifie qu'il y a eu une insertion

        #On parcourt la liste à l'envers et on place la combinaison avant le premier élément lu qui a le même effectif que celui de la combinaison
        for i in reversed(table_effectif):
            if i[1] >= somme_effectif:
                position = table_effectif.index(i)
                table_effectif.insert(position+1,(somme_valeur,somme_effectif))
                insertion = True
                break

        #S'il n'y pas eu d'insertion (la somme est supérieure à tous les effectifs)
        if not insertion:
            table_effectif.insert(0,(somme_valeur,somme_effectif))

        #On répète l'opération avec la nouvelle table des effecitifs
        return construction_arbre(table_effectif)

def comptage(txt):
    dic={}
    for i in txt:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    return dic

def dic_to_tab(dic):
    tab=[]
    j=0
    for i in dic:
        tab.append((i,dic[i]))
    return tab

def tri_tab(tab):
    for i in range (len(tab)):
        maxi=(tab[i], i)
        for j in range (i+1,len(tab)):
            if maxi[0][1]<tab[j][1]:
                maxi=(tab[j], j)
        tab[maxi[1]]=tab[i]
        tab[i]=maxi[0]
    return tab

t1= comptage("Line 13 : def deplace(self, dx: Any, dy: Any, dz: Any) -> AnyLine 13 : Number of parameters was 3 in Point2D.deplace and is now 4 in overriding 'Point3D.deplace' methodIt looks like the method has a different number of arguments than in the implemented interface or in an overridden method. Extra arguments with default values are ignored.Point2D.pyLine 11 : Redefining name 'p2' from outer scope (line 56)It looks like the local variable is hiding a global variable with the same name.Most likely there is nothing wrong with this. I just wanted to remind you that you can't access the global variable like this. If you knew it then please ignore the warning.If you don't want to see this reminder in the future, then add redefined-outer-name (without quotes) into Tools → Options → Assistant → Disabled checks.Line 29 : Redefining name 'p2' from outer scope (line 56)It looks like the local variable is hiding a global variable with the same name.Most likely there is nothing wrong with this. I just wanted to remind you that you can't access the global variable like this. If you knew it then please ignore the warning.If you don't want to see this reminder in the future, then add redefined-outer-name")
t2=dic_to_tab(t1)
tri_tab(t2)
print(t2)

    
        
g = NoeudHuffman('g', None, None) # Arbre de valeur 'G', sans sous-arbre (feuille)
# Arbre de valeur 'F'. Sous-arbre gauche : g. Pas sous-arbre droit.
f = NoeudHuffman('fg', g, None)
# Arbre de valeur 'E'. Pas de sous-arbre gauche. Sous-arbre droit : f
e = NoeudHuffman('efg', None, f)
d = NoeudHuffman('c', None, None) # Arbre de valeur 'D', sans sous-arbres (feuille)
c = NoeudHuffman('ab', None, None) # Arbre de valeur 'C', sans sous-arbres (feuille)
# Arbre de valeur 'B', sous-arbre gauche : c. Sous-arbre droit : d.
b = NoeudHuffman('abc', c, d)
# Arbre de valeur 'A', sous-arbre gauche : b. Sous-arbre droit : e.
a = NoeudHuffman('abcefg', b, e)

table_effectif_finale = construction_arbre(t2)
print(table_effectif_finale)


