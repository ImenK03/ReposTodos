# Étape 1 : Mise en place du projet
print("=== Étape 1 : Mise en place du projet To-Dos ===")

# Stockage temporaire des To-Dos dans une liste
todos = []

# Fonctionnalités principales
def lister_todos():
    """Lister les tâches."""
    if not todos:
        print("Aucune tâche à afficher.")
    else:
        print("\nListe des tâches :")
        for i, todo in enumerate(todos, start=1):
            print(f"{i}. {todo['description']} - {'Fait' if todo['statut'] else 'À faire'}")
def creer_todo():
    """Créer une nouvelle tâche."""
    description = input("Entrez la description de la tâche : ")
    todos.append({"description": description, "statut": False})
    print("Nouvelle tâche ajoutée.")

def modifier_statut_todo():
    """Modifier le statut d'une tâche."""
    lister_todos()
    
    try:
        index = int(input("Entrez le numéro de la tâche à modifier : ")) - 1
        if 0 <= index < len(todos):
            todos[index]["statut"] = not todos[index]["statut"]
            print("Statut de la tâche modifié.")
        else:
            print("Numéro invalide.")
    except ValueError:
        print("Entrée invalide.")

def supprimer_todo():
    """Supprimer une tâche."""
    lister_todos()
    try:
        index = int(input("Entrez le numéro de la tâche à supprimer : ")) - 1
        if 0 <= index < len(todos):
            todos.pop(index)
            print("Tâche supprimée.")
        else:
            print("Numéro invalide.")
    except ValueError:
        print("Entrée invalide.")

# Étape 2 : Ajout de fonctionnalités
print("\n=== Étape 2 : Ajout de fonctionnalités ===")

# Simuler le menu principal avec branchement Git Flow
def menu_principal():
    choix = ''
    while choix != 'q':
        print('\n==== Menu principal ====')
        print('1: Lister les todos')
        print('2: Créer un todo')
        print('3: Modifier le statut d\'un todo')
        print('4: Supprimer un todo')
        print('q: Quitter')
        print('========================')
        choix = input('=> Choix : ')

        match choix:
            case '1':
                lister_todos()
            case '2':
                creer_todo()
            case '3':
                modifier_statut_todo()
            case '4':
                supprimer_todo()
            case 'q':
                print('Au revoir')
            case _:
                print('Choix invalide')

# Appeler le menu principal
menu_principal()

# Étape 3 : Tester les fonctionnalités sur la branche release
print("\n=== Étape 3 : Test des fonctionnalités sur la branche release ===")
# Simuler les tests (par exemple, ajouter des tests unitaires ici)
print("Tests en cours...")
print("Tous les tests sont passés avec succès !")

# Étape 4 : Correction d'un bug directement sur la branche main
print("\n=== Étape 4 : Correction d'un bug ===")
# Simuler un correctif sur la branche main
print("Correction d'un bug critique (exemple : gestion des tâches vides).")
