# Mon Projet Netmiko
I. Initialiser un dépôt Git local
  1. Créez un nouveau répertoire prenom-nom-netmiko pour votre projet.
    mkdir mbarki-houssem-netmiko && cd mbarki-houssem-netmiko
  2. Initialisez un dépôt Git dans ce répertoire.
    git init
II. Ajouter et commiter des fichiers
  1. Créez un fichier README.md et ajoutez-y le titre : Mon Projet Netmiko
    nano README.md
  2. Ajoutez ce fichier à l'index et commitez-le en utilisant le message "Ajout du fichier README".
    git commit -m Ajout du fichier README"
  3. Créez un fichier main.py et ajoutez-y un simple script Python : print("Hello, Git!")
    nano main.py
  4. Ajoutez et commitez ce fichier en utilisant le message "Ajout du script Python principal".
    git commit -m 
  5. Affichez tous les commits effectués.
    git log
III. Créer et fusionner des branches
  1. Créez une nouvelle branche feature/netmiko pour ajouter une fonctionnalité.
    git branch feature/netmiko
    git checkout feature/netmiko
  2. Modifiez main.py pour inclure une fonction acces_netmiko qui utilise la bibliothèque netmiko pour effectuer les opérations suivantes sur un routeur Cisco C8000V :
    nano main.py
  3. Ajoutez et commitez ces modifications avec le message "Ajout de la fonction acces_netmiko".
    git commit -m "Ajout de la fonction acces_netmiko"
  4. Revenez à la branche principale (main).
    git checkout main
  5. Fusionnez les modifications de la branche feature/netmiko dans main
    git merge feature/netmiko
IV. Travailler avec un dépôt distant sur GitHub
  1. Créez un nouveau dépôt sur GitHub (nommez-le prenom-nom-netmiko ).
    creation un nouveau dépôt sur GitHub (mbarki-houssem-netmiko)
  2. Ajoutez ce dépôt GitHub comme dépôt distant.
    git remote add origin https://github.com/Sen-Se1/mbarki-houssem-netmiko.git
  3. Poussez vos commits locaux vers GitHub.
    git branch -M main
    git push -u origin main
  4. Allez sur GitHub et vérifiez que les fichiers sont bien présents.
    vérifiez que les fichiers sont bien présents
  5. Créez une nouvelle branche sur GitHub nommée feature/salut
    Creation une nouvelle branche sur GitHub nommée feature/salut
  6. Sur votre machine locale, récupérez cette nouvelle branche.
    git fetch origin
    git checkout -b feature/salut origin/feature/salut
  7. Modifiez main.py pour ajouter une fonction qui dit salut.
    nano main.py
  8. Ajoutez et commitez ces modifications avec le message "Ajout de la fonction dire_salut".
    git commit -m "Ajout de la fonction dire_salut"
  9. Poussez cette branche vers GitHub
    git push origin feature/salut
  10. Sur GitHub, créez une Pull Request pour fusionner feature/salut dans main.
    creation une Pull Request pour fusionner feature/salut dans main.
  11. Acceptez la Pull Request et fusionnez la branche.
    Acceptation la Pull Request et fusionnez la branche.
  12. Revenez à la branche main locale et récupérez les dernières modifications.
    git checkout main
    git fetch origin
