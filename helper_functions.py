import os
from state import State
from agents import read_summarize, README, Judge
from colorama import Fore

def get_all_files(state: State) -> State:
    excluded_dirs = {'__pycache__', '.ipynb_checkpoints'}
    excluded_exts = {'.pyc', '.pyo', '~', ".txt", ".pdf", ".docx"}
    
    for root, dirs, files in os.walk(state["directory"]):
        # Remove excluded directories from the list of directories to walk into
        dirs[:] = [d for d in dirs if d not in excluded_dirs]
        
        for file in files:
            # Skip files with excluded extensions
            if any(file.endswith(ext) for ext in excluded_exts) or file.startswith('.'):
                continue
            
            file_path = os.path.join(root, file)
            state["filenames"].append(file_path)
    
    return state

def get_directory(state: State) -> State:
    state["directory"] = input("Enter directory name: ")
    return state

def get_summaries(state: State) -> State:
    print(Fore.GREEN + "******* Creating Summaries *******")
    
    for path in state["filenames"]:
        state["file_summary"][path] = read_summarize(path)
    
    return state

def judge(state: State) -> State:
    print(Fore.GREEN + "******* Judging Summaries *******")

    for path in state["file_summary"].keys():
        response = Judge(path)
        state["judge_decide"][path] = response
    
    return state

def rewrite(state: State) -> State:
    filtered_dict = {k: v for k, v in state["judge_decide"].items() if v != "go"}
    for path, _ in filtered_dict.items():
        print(Fore.GREEN + f"******* ReWriting {path} *******")
        state["file_summary"][path] = read_summarize(path)

    return state

def readme(state: State) -> None:
    README(list(state["file_summary"].keys()))
    print(Fore.GREEN + "******* README.md is created. *******")
