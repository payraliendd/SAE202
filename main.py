from arbreBinaire import *
from NoeudHuffman import *

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

table_effectif_finale = NoeudBinaire.construction_arbre(t2)
print(table_effectif_finale)


