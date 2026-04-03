"# SAE202" 

Ce projet vise à implémenter l'algorithme de Huffman, une méthode de compression de données sans perte.

Le code permet :
- Analyse de la fréquence de chaque caractère dans un texte donné et l'ajoute à un dictionnaire.
- Utilisation d'une classe NoeudBinaire avec héritage pour gérer la classe huffman.
- Construction de l'arbre avec un algorithme qui le crée en fonction du poids de chaque lettre.
- Création de la table de correspondance caractère -> code binaire.
- Affichage de l'arbre dans la console( __str__ ).


Fonctionnalités implémentées :
NoeudBinaire
- Constructeurs, Getters, Setters.
- Tests d'état, si un noeud a un fils droit/gauche s'il est une feuille ou vide.
- Calcule la hauteur de l'arbre.
- Parcours préfixe, infixe, suffixe et en largeur.
- Affichage visuel de l'arbre.

Arbre Huffman
- Construction de l'arbre, algorithme itératif (construction_arbre) fusionnant les deux noeuds de poids minimal jusqu'a l'obtention de la racine finale.
- Génération des codes uniques à l'aide d'un parcours récursif pour attribuer 0 à gauche et 1 à droite, générant ainsi le dictionnaire Huffman.
- Compression permettant de transformer un texte en suite de 0 et de 1 à partir du dictionnaire généré.


Fonctions externes
comptage et tri d'une chaine de caractère.

Structure du projet: 
- arbreBinaire.py contient la classe NoeudBinaire
- NoeudHuffman.py contient la class NoeudHuffman
- main.py script principal pour tester la compresion.

Utilisation dans le terminal:
python main.py

Le terminal affichera l'arbre de Huffman généré visuellement suivi du dictionnaire contennat le nouvelle encodage de chaque lettre.