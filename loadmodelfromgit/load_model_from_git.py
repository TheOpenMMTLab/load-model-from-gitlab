import gitlab
import os


def load_model_from_git(branch_name: str, input_path: str, output_path: str):
    """Load a model file from a GitLab repository and save it to the local filesystem.
    Args:
        input_path (str): Relative path of the model file inside the GitLab repository.
        output_path (str): Local filesystem path where the downloaded file should be saved.
    """

    URL = os.environ.get('GITLAB_URL')
    TOKEN = os.environ.get('GITLAB_TOKEN')
    PROJECT_ID = os.environ.get('GITLAB_PROJECT_ID')

    gl = gitlab.Gitlab(url=URL, private_token=TOKEN)
    gl.auth()  # Executing of authentication in Gitlab

    # get project
    p = gl.projects.get(PROJECT_ID)
    print(f'Project Name: {p.name}')

    f = p.files.get(file_path=input_path, ref=branch_name)
    print(f"File Name: {f.file_name}")

    # Write to file
    with open(output_path, "wb") as file:
        file.write(f.decode())
        print("File written successfully.")
