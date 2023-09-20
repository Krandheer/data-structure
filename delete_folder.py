import shutil
import os
import socket

root = os.path.expanduser("~")
AI_DEV = os.path.join(root, "AI_DEV")
to_delete = os.path.join(root, "to_delete")
mod_jpg = os.path.join(AI_DEV, "mod_jpg")
res_out = os.path.join(AI_DEV, "res_out")


def delete_folder(repository_path):
    try:
        # Delete the repository
        shutil.rmtree(repository_path)
        print("Repository deletion successful.")
    except Exception as e:
        print(f"Error: {e}")


delete_folder(to_delete)
