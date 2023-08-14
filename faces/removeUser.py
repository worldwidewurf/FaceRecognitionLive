import os
import shutil

def removeUser(username):
    """this removes a user from the system by moving the user's picture from the images folder to the removedUsers folder

    Args:
        username (str): The name/username of the user to be removed
    """
    source_file = os.path.join("faces", "images", username + ".jpg")
    destination_folder = os.path.join("faces", "removedUsers")
    destination_path = os.path.join(destination_folder, username + ".jpg")

    if os.path.exists(source_file):
        os.makedirs(destination_folder, exist_ok=True)
        shutil.move(source_file, destination_path)
        print(f"User '{username}' removed from system.'")
    else:
        print(f"User '{username}' does not exist.")


