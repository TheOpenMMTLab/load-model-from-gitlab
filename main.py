import argparse

from loadmodelfromgit.load_model_from_git import load_model_from_git


def parse_args():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Download and process a model file from GitLab.')
    parser.add_argument("--branch-name", default="main", help="Git branch name to fetch the file from (default: 'main').")
    parser.add_argument("--input-path", required=True, help="Relative path of the model file inside the GitLab repository.")
    parser.add_argument("--output-path", required=True, help="Local filesystem path where the downloaded file should be saved.")
    args = parser.parse_args()

    return args.branch_name, args.input_path, args.output_path


branch_name, input_path, output_path = parse_args()
load_model_from_git(branch_name, input_path, output_path)
