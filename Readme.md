# Mélangeur de Lettres

Bienvenue dans le **Mélangeur de Lettres**, une application interactive qui vous permet de mélanger les lettres internes de mots d'un texte tout en respectant les règles suivantes :
- La première et la dernière lettre de chaque mot restent fixes.
- Les caractères spéciaux (apostrophes, tirets, ponctuation) ne sont pas déplacés.

Cette application est simple à utiliser et propose deux options : saisir manuellement du texte ou téléverser un fichier pour le traiter.

## Fonctionnalités principales

### 1. **Saisie directe de texte**
L'utilisateur peut entrer un texte dans une zone de saisie et le traiter immédiatement. 
- ![Menu principal avec l'option "Entrer du texte" sélectionnée.](src/Menu%20principal%20-%20Saisie%20de%20texte.png)
- ![Zone de saisie de texte avec le bouton "Mélanger les mots".](src/Saisie%20Texte.png)

### 2. **Téléversement de fichier**
L'utilisateur peut sélectionner un fichier à traiter. Les formats supportés sont :
- `.txt` (texte brut)
- `.pdf` (fichier PDF)
- `.docx` (Microsoft Word)

Une fois sélectionné, le fichier est analysé et son texte traité.
- ![Menu principal avec l'option "Téléverser un fichier" sélectionnée.](src/Menu%20principal%20-%20T%C3%A9l%C3%A9versement.png)
- ![Fenêtre de sélection de fichier, avec les formats disponibles affichés.](src/T%C3%A9l%C3%A9versement%20fichier.png)

### 3. **Enregistrement des résultats**
Les résultats du traitement peuvent être enregistrés dans les formats suivants :
- `.txt` : Texte brut.
- `.odt` : Document compatible OpenDocument.

Une fenêtre de dialogue permet de choisir l'emplacement, le nom, et le format du fichier.
- ![Fenêtre "Enregistrer sous" affichant les options de format et le bouton "Enregistrer".](src/Enregistrement%20d%27une%20saisie%20format%20txt%20ou%20odt.png)

## Tutoriel d'utilisation

### Étape 1 : Lancer l'application
Double-cliquez sur le fichier exécutable pour ouvrir l'interface du programme.

### Étape 2 : Choisir une option
#### **Option 1 : Entrer du texte**
1. Cliquez sur le bouton "Entrer du texte".
2. Une zone de saisie apparaît. Entrez votre texte.
3. Cliquez sur le bouton "Mélanger les mots" pour traiter le texte.
4. Une fenêtre de sauvegarde s'ouvre. Choisissez un format (txt ou odt), un nom et un emplacement pour enregistrer le fichier.

- ![Menu principal avec "Entrer du texte" sélectionné.](src/Menu%20principal%20-%20Saisie%20de%20texte.png)
- ![Zone de saisie de texte et bouton "Mélanger les mots".](src/Bouton%20m%C3%A9langeur%20-%20Saisie%20texte.png)
- ![Fenêtre "Enregistrer sous" avec les options d'enregistrement.](src/Enregistrement%20d%27une%20saisie%20format%20txt%20ou%20odt.png)

#### **Option 2 : Téléverser un fichier**
1. Cliquez sur le bouton "Téléverser un fichier".
2. Une fenêtre de sélection s'ouvre. Choisissez un fichier à traiter.
3. Une fois traité, une fenêtre de sauvegarde s'affiche. Enregistrez le fichier dans le format et à l'emplacement souhaités.

- ![Menu principal avec "Téléverser un fichier" sélectionné.](src/Menu%20principal%20-%20T%C3%A9l%C3%A9versement.png)
- ![Fenêtre de sélection de fichier avec le nom du fichier affiché.](src/S%C3%A9lection%20d%27un%20fichier.png)
- ![Fenêtre "Ouvrir" avec les options de format.](src/parcourir%20un%20fichier%20%C3%A0%20t%C3%A9l%C3%A9verser.png) (possibilité de modifier le format du fichier à téléverser)


- ![Fenêtre "Enregistrer sous" avec le bouton "Enregistrer".](src/bouton%20enregistrer.png)

### Étape 3 : Vérifiez vos résultats
Une fois enregistré, ouvrez le fichier pour visualiser le texte traité.

## Gestion des erreurs
- Si un problème survient (par exemple, un fichier non pris en charge ou une erreur de traitement), une fenêtre d'alerte s'affiche avec un message explicatif.
- Exemples d'erreurs :
  - Aucun fichier sélectionné.
    - ![Message d'erreur indiquant qu'aucun fichier n'a été sélectionné.](src/Erreur%20Aucun%20fichier%20s%C3%A9lectionn%C3%A9.png)
  - Format de fichier non supporté.
    - ![Message d'erreur indiquant que le format de fichier n'est pas supporté]()
  - Texte vide dans la zone de saisie.
    - ![Message d'erreur indiquant qu'aucune saisie n'a été renseignée par l'utilisateur](src/Erreur%20aucun%20texte%20dans%20la%20saisie.png)
 

## Configuration requise

### Prérequis système
- **Système d'exploitation** : Windows, macOS ou Linux.
- **Python** : 3.12 ou supérieur si vous utilisez le script directement.

### Dépendances
Si vous exécutez le programme depuis le code source, installez les bibliothèques suivantes :
```bash
pip install tkinter PyPDF2 python-docx odfpy
```

## Structure du projet
- **`gui_handler.py`** : Interface utilisateur.
- **`file_handler.py`** : Gestion des fichiers (lecture et sauvegarde).
- **`shuffle_logic.py`** : Logique de mélange des lettres.

## Exemple d'utilisation
1. Lancez l'application.
2. Entrez du texte ou téléversez un fichier.
3. Cliquez sur "Mélanger les mots".
4. Sauvegardez les résultats.

-  ![Fenêtre principale avec une saisie ou un fichier prêt à être traité.](src/Exemple%201.png)
-  ![Fenêtre de sauvegarde affichant les options de format.](src/Exemple%202.png)

---