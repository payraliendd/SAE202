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
    def set_v(self, nouveau_v):
        self.v=nouveau_v              
    def set_gauche(self, nouveau_g):
        if nouveau_g is not None and not isinstance(nouveau_g, NoeudBinaire):
            raise TypeError("L'enfant gauche doit être de type NoeudBinaire ou None.")
        self.g = nouveau_g
        
    def set_droit(self, nouveau_d):
        if nouveau_d is not None and not isinstance(nouveau_d, NoeudBinaire):
            raise TypeError("L'enfant droit doit etre de type NoeudBinaire ou None.")
        self.d = nouveau_d
    def arbre_gauche(self):
        return self.g is not None
    def arbre_droit(self):
        return self.d is not None
    def arbre_f(self):
        return self.g is None and self.d is None
    def arbre_v(self):
        return self.v is None and self.g is None and self.d is None
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
