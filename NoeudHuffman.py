
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
            if lettre in self.get_g().get_v()[0]:
                encodage += "0"
                return self.get_g().encodage_huffman(lettre,encodage)
        
        #On vérifie que la branche droite n'est pas vide comme le premier test vérifie uniquement que la branche est une feuille
        if self.get_d() is not None:
            if lettre in self.get_d().get_v()[0] :
                encodage += "1"
                return self.get_d().encodage_huffman(lettre,encodage)
    
    @staticmethod
    def compression(texte,liste_encodage):
        resultat = ""
        for chr in texte:
            for cle in liste_encodage:
                if chr == cle[0]:
                    resultat += cle[1]
        return resultat
    
    @staticmethod
    def tri_noeuds(liste_noeud):
        """Trie une liste d'objets NoeudHuffman par ordre décroissant de poids."""
        for i in range(len(liste_noeud)):
            maxi = i
            for j in range(i + 1, len(liste_noeud)):
                poids_maxi = liste_noeud[maxi].get_v()[1]
                poids_actuel = liste_noeud[j].get_v()[1]
                
                if poids_maxi < poids_actuel:
                    maxi = j
                    
            temp = liste_noeud[i]
            liste_noeud[i] = liste_noeud[maxi]
            liste_noeud[maxi] = temp

    @staticmethod
    def construction_arbre(table_effectif):
        #On trie la table d'effectif par ordre décroissant
        liste_noeud = []
        for i in table_effectif:
            liste_noeud.append(NoeudHuffman(i,None,None))
        
        while len(liste_noeud) > 1:
            noeud_gauche = liste_noeud.pop()
            noeud_droit = liste_noeud.pop()

            tuple_g = noeud_gauche.get_v()
            tuple_d = noeud_droit.get_v()

            nouveau_t = (tuple_g[0] + tuple_d[0], tuple_g[1] + tuple_d[1])

            nouveau_noeud = NoeudHuffman(nouveau_t,noeud_gauche,noeud_droit)
            liste_noeud.append(nouveau_noeud)

            NoeudHuffman.tri_noeuds(liste_noeud)
        
        return liste_noeud[0]


        
        
    