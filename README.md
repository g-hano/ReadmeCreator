**README.md**
=====================================

### Installation

To get started with this project, follow these steps:

```bash
git clone g-hano/SummaryWriter
pip install -r requirements.txt
```

### Project Description

This project uses a combination of natural language processing (NLP) and graph-based workflows to generate a README.md file based on code summaries. The system prompts users to input a directory name, list of files, and then creates summaries for each file using an LLM model.

### Usage

To use this project, simply follow the prompts in the `main.py` script:

1. Enter a directory name.
2. The system will generate summaries for each file based on the LLM model.
3. The system will decide which summaries to re-write
4. You can use README.md for your projects.

### Contact Information

* Project Lead: [M.Cihan Yalçın](https://www.linkedin.com/in/chanyalcin/)

### License

This project is licensed under the MIT License.

**Graph-Based Workflow**
-------------------------

The graph-based workflow is defined in the `graph.py` script. It uses a StateGraph to represent the workflow, which consists of nodes and edges. The nodes represent different steps in the process, while the edges represent the relationships between them.

### Nodes

* `get_directory`: Asks the user for a directory name.
* `get_all_files`: Lists all files in the specified directory.
* `get_summaries`: Generates summaries for each file using the LLM model.
* `judge`: Evaluates the generated summaries and decides which ones to rewrite or include in the README.md file.
* `rewrite`: Rewrites selected summaries based on the LLM model.
* `readme`: Creates a README.md file based on the generated summaries.

### Edges

The edges represent the relationships between nodes. For example, the edge from `get_directory` to `get_all_files` means that after getting the directory name, the system will list all files in that directory.

**LLM Model**
-------------

The LLM model used for generating summaries is defined in the `agents.py` script. It uses an Ollama instance with a specific model and prompt.

### System Prompts
----------------

The system prompts are defined in the `configs.py` script. They include the LLM model, summary folder, system prompt folder, and LLM prompt folder.

I hope this README.md file meets your requirements! Let me know if you need any further assistance.