from arbreBinaire import *



class NoeudHuffman(NoeudBinaire):
    
    def __init__(self,v,g,d):
        super().__init__(v,g,d)

    def encodage_huffman(self, code="", dic=None):
        if dic is None:
            dic={}
        if self.arbre_f():
            dic[self.v]=code
        else:
            if self.arbre_gauche():
                self.g.encodage_huffman(code + "0", dic)
            if self.arbre_droit():
                self.d.encodage_huffman(code + "1", dic)
        return dic
    
    @staticmethod
    def compression(texte,dic_encodage):
        resultat = ""
        for chr in texte:
            resultat += dic_encodage[chr]
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
                    
            t = liste_noeud[i]
            liste_noeud[i] = liste_noeud[maxi]
            liste_noeud[maxi] = t

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


        
        
    