from arbreBinaire import *

class NoeudHuffman(NoeudBinaire):
    
    def __init__(self,v,g,d,):
        super().__init__(v,g,d)
        self.v_g = 0
        self.v_d = 1

    def encodage_huffman(self,lettre,encodage):
        #Si le branche est une feuille, on arrete la récursivité et on renvoye l'encodage
        if self.get_g() == None and self.get_d() == None:
            return (lettre,encodage)
        
        #On vérifie que la branche gauche n'est pas vide comme le premier test vérifie uniquement que la branche est une feuille
        if self.get_g() is not None:
            if lettre in self.get_g().get_v():
                encodage += "0"
                return self.get_g().encodage_huffman(lettre,encodage)
        
        #On vérifie que la branche droite n'est pas vide comme le premier test vérifie uniquement que la branche est une feuille
        if self.get_d() is not None:
            if lettre in self.get_d().get_v() :
                encodage += "1"
                return self.get_d().encodage_huffman(lettre,encodage)
    
    def compression(texte,liste_encodage):
        resultat = ""
        for chr in texte:
            for cle in liste_encodage:
                if chr == cle[0]:
                    resultat += cle[1]
        return resultat

        
        
    