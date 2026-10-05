# Calculatrice & Convertisseur d'Unités 

Application console en Python dotée d'une calculatrice, un convertisseur d'unités ainsi qu'un système d'exportation automatique d'historique.

---

## Fonctionnalités

### Calculatrice
- **Fonctions de base** : Addition (`+`), Soustraction (`-`), Multiplication (`*`), Division (`/`).
- **Fonctions bonus** :
  - Modulo (`%`)
  - Exponentielle (`**`)
  - Racine carrée (`root` / `racine`)
  - Trigonométrie (`sin`, `cos`, `tan`)
  - Logarithme décimal (`log`)
- **Chaînage dynamique** : Les opérations s'enchaînent jusqu'à entrer l'opérateur `=`.

### Convertisseur d'Unités
- **Distances** : Kilomètres $\leftrightarrow$ Miles
- **Poids** : Kilogrammes $\leftrightarrow$ Livres
- **Températures** : Celsius $\leftrightarrow$ Fahrenheit et Celsius $\leftrightarrow$ Kelvin
- **Prise en compte du zéro absolu**

### Gestion de l'Historique
- Sauvegarde automatique en mémoire au fil des calculs.
- Exportation automatique du journal de calculs dans le fichier `history/historique.txt` à la clôture de la session calculatrice.

---

## Structure du Projet

```
.
├── .gitignore
├── requirements.txt
├── main.py                    # Menu général
├── features/                  
│   ├── calculatrice.py        # Calculatrice 
│   ├── unit_conversion.py     # Menu et fonctions des conversions
│   └── history.py             # Gestion et exportation de l'historique
├── operations/                # Fonctions de calcul
│   ├── addition.py
│   ├── subtraction.py
│   ├── multiply.py
│   ├── division.py
│   ├── modulo.py
│   ├── exponentiation.py
│   ├── square_root.py
│   ├── trigonometry.py
│   └── logarithm.py
└── history/
    └── historique.txt         # Fichier contenant l'historique

```
## Installation et Lancement

### Prérequis

* Python 3.14.7 installé sur votre système.
* Installation des dépendances via le fichier requirements.txt.

### Installation des dépendances

Avant de lancer l'application, installez les paquets requis :

```
pip install -r requirements.txt
```

### Lancement

Exécutez le fichier principal depuis la racine de votre projet :

```
python main.py

```

## Guide d'Utilisation

1. **Menu Général** : Choisissez entre la Calculatrice (1) ou le Convertisseur (2).

2. **Saisie** : Les décimaux peuvent être entrés aussi bien avec un point (`12.5`) qu'avec une virgule (`12,5`).

3. **Quitter la calculatrice** : Entrez `=` comme opérateur pour afficher le résultat final et générer le fichier d'historique dans `history/historique.txt`.

## Gestion des Erreurs 

* **Saisies invalides** : Interception automatique des entrées non numériques.

* **Contraintes physiques** : Interdiction des températures sous le zéro absolu.

* **Calcul** : Gestion des exceptions pour la division par zéro et les racines de nombres négatifs.



