from llama_index.core.base.llms.types import ChatMessage, MessageRole
from llama_index.llms.ollama.base import Ollama
from IPython.display import display, Markdown
from colorama import Fore
from configs import OLLAMA_MODEL, SUMMARY_FOLDER, SYSTEM_PROMPT_FOLDER, LLM_PROMPT_FOLDER

import os
os.makedirs(SUMMARY_FOLDER, exist_ok=True)

def read_summarize(file_path, display_=False):
    system_prompt = open(SYSTEM_PROMPT_FOLDER+"read_summarize_prompt.txt", "r").read()
    
    llm = Ollama(model=OLLAMA_MODEL, system_prompt=system_prompt)

    prompt = open(LLM_PROMPT_FOLDER+"read_summarize_prompt.txt", "r").read()

    print(Fore.MAGENTA + f"Reading - {file_path}")

    with open(file_path, "r") as f:
        code = f.read()

    response = llm.chat([ChatMessage(role=MessageRole.USER, content=prompt.format(filename=file_path, file_text=code))]).message.content
    
    directory_name = os.path.basename(os.path.dirname(file_path))
    file_name = os.path.basename(file_path)

    path_to_save = f"{directory_name}_{file_name}_sum.md"

    with open(SUMMARY_FOLDER + "/" + path_to_save, "w") as f:
        f.write(response)
    
    if display_:
        display(Markdown(response))
    
    return path_to_save

def Judge(summary_path, display_=False):
    system_prompt = open(SYSTEM_PROMPT_FOLDER+"judge_prompt.txt", "r").read()

    llm = Ollama(model=OLLAMA_MODEL, system_prompt=system_prompt)

    prompt = open(LLM_PROMPT_FOLDER+"judge_prompt.txt", "r").read()

    with open(summary_path, "r") as f:
        sum = f.read()
    
    response = llm.chat([
        ChatMessage(role=MessageRole.USER, 
                    content=prompt.format(filename=summary_path, summary=sum))
                    ]).message.content

    if display_:
        display(Markdown(response))
        
    return response

def README(files, display_=True):
    system_prompt = open(SYSTEM_PROMPT_FOLDER+"readme_prompt.txt", "r").read()


    llm = Ollama(model=OLLAMA_MODEL, system_prompt=system_prompt)

    prompt = open(LLM_PROMPT_FOLDER+"readme_prompt.txt", "r").read()
    
    text = ""
    for file_ in files:
        with open(file_, "r") as f:
            text += file_ + "\n----------\n"
            text += f.read()
            text += "\n----------\n"
    
    response = llm.chat([ChatMessage(role=MessageRole.USER, content=prompt.format(file_text=text))]).message.content

    with open(SUMMARY_FOLDER + "/README.md", "w") as f:
        f.write(response)
    
    if display_:
        display(Markdown(response))