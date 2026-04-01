class NoeudB():
    def __init__(self, v, g, d):
        self.v=v
        self.g=g
        self.d=d
    def __str__(self):
        
    def get_v(self):
        return self.v
    def get_g(self):
        return g
    def get_d(self):
        return d
    def arbre_gauche(self):
        return self.g!=None
    def arbre_droit(self):
        return self.d!=None
    def arbre_f(self):
        return self.g==None and self.d==None
    def arbre_v(self):
        return self.v==None
    def hauteur(self):
        if arbre_v():
            return 0
        return 1+max(hauteur(self.g), hauteur(self.d))
