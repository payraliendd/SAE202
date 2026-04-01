class NoeudBinaire():
    def __init__(self, v, g, d):
        self.v=v
        self.g=g
        self.d=d
    def __str__(self, h=0):
        if h == 0:
            chaine = str(self.v) + "\n"
        else:
            chaine = "     " * (h - 1) + "|--> " + str(self.v) + "\n"
        if self.g is None and self.d is None:
            return chaine
        if self.g is not None:
            chaine += self.g.__str__(h + 1)
        else:
            chaine += "     " * h + "|--> \n"
            
        if self.d is not None:
            chaine += self.d.__str__(h + 1)
        else:
            chaine += "     " * h + "|--> \n"
        return chaine
        
    
    def get_v(self):
        return self.v
    
    def get_g(self):
        return self.g
    
    def get_d(self):
        return self.d
    
    def arbre_gauche(self):
        return self.g!=None
    
    def arbre_droit(self):
        return self.d!=None
    
    def arbre_f(self):
        return self.g==None and self.d==None
    
    def arbre_v(self):
        return self.v==None
    
    def hauteur(self):
        if self.arbre_v():
            return 0
        if self.arbre_gauche():
            hg=self.g.hauteur()
        else:
            hg=0
        if self.arbre_droit():
            hd=self.d.hauteur()
        else:
            hd=0
        return 1+max(hg,hd)
    
    def prefixe(self):
        tab=[]
        if self.v is not None: 
            tab.append(self.v)
        if self.arbre_gauche():
            tab+=self.g.prefixe()
        if self.arbre_droit():
            tab+=self.d.prefixe()
        return tab
    
    def suffixe(self):
        tab=[]
        if self.arbre_gauche():
            tab+=self.g.suffixe()
        if self.arbre_droit():
            tab+=self.d.suffixe()
        tab.append(self.v)
        return tab
    
    def infixe(self):
        tab=[]
        if self.arbre_gauche():
            tab+=self.g.infixe()
        tab.append(self.v)
        if self.arbre_droit():
            tab+=self.d.infixe()
        return tab
    
    def Largeur(self):
        tab=[]
        file=[self]
        while len(file)>0:
            noeud= file.pop(0)
            tab.append(noeud.v)
            if noeud.g is not None:
                file.append(noeud.g)
            if noeud.d is not None:
                file.append(noeud.d)
        return tab
    
    def construction_arbre(self,table_effectif):
        #fin de récursivité quand il reste une valeur dans le liste (racine de l'arbre)
        if len(table_effectif) == 1:
            return table_effectif
        
        #Variables qui représentent la valeurs et l'effectif de la combinaison des 2 dernier tuples de la table des effectifs
        somme_valeur = table_effectif[-1][0] + table_effectif[-2][0]
        somme_effectif = table_effectif[-1][1] + table_effectif[-2][1]

        #On supprime les 2 dernières valeurs
        table_effectif.pop()
        table_effectif.pop()

        #On parcourt la liste à l'envers et on place la combinaison avant le premier élément lu qui a le même effectif que celui de la combinaison
        for i in reversed(table_effectif):
            if i[1] == somme_effectif:
                position = table_effectif.index(i)
                table_effectif.insert(position+1,(somme_valeur,somme_effectif))

        #On répète l'opération avec la nouvelle table des effecitifs
        return self.construction_arbre(table_effectif)


g = NoeudBinaire('G', None, None)
f = NoeudBinaire('F', g, None)
e = NoeudBinaire('E', None, f)
d = NoeudBinaire('D', None, None)
c = NoeudBinaire('C', None, None)
b = NoeudBinaire('B', c, d)
a = NoeudBinaire('A', b, e)
print(a.hauteur())
print(a)
print(a.prefixe())
print(a.suffixe())
print(a.infixe())
print(a.Largeur())
