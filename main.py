from github import Github
from datetime import datetime
import os

# Fonction pour effectuer un commit
def make_commit(repo, file_path, commit_message):
    # Récupérer le contenu actuel du fichier
    contents = repo.get_contents(file_path)
    current_content = contents.decoded_content.decode()

    # Modifier le contenu du fichier
    new_content = current_content + f"\nCommit effectué le {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    # Effectuer le commit
    repo.update_file(contents.path, commit_message, new_content, contents.sha)

# Récupérer la clé d'API GitHub à partir de la variable d'environnement
access_token = os.getenv("API_GITHUB")

# Nom d'utilisateur GitHub
username = "Thesirix"

# Création de l'objet Github avec l'access token
g = Github(access_token)

# Récupérer le dépôt (repo)
repo_name = "StreakMaster"
repo = g.get_user(username).get_repo(repo_name)

# Définir le chemin du fichier à modifier
file_path = "empty_file.txt"

# Définir le message de commit
commit_message = "Commit quotidien"

# Effectuer un commit
make_commit(repo, file_path, commit_message)
