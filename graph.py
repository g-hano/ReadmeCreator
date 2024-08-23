from langgraph.graph import START, END, StateGraph
from IPython.display import Image, display
from state import State
from helper_functions import (get_directory, 
                              get_all_files, 
                              get_summaries, 
                              judge, 
                              rewrite, readme)

class GRAPH():
    def __init__(self) -> None:
        self.image = None
        self.workflow = None    
    
    def set_graph(self):
        graph = StateGraph(State)

        graph.add_node("get_directory", get_directory)
        graph.add_node("get_all_files", get_all_files)
        graph.add_node("get_summaries", get_summaries)
        graph.add_node("judge", judge)
        graph.add_node("rewrite", rewrite)
        graph.add_node("readme", readme)

        graph.add_edge(START, "get_directory")
        graph.add_edge("get_directory", "get_all_files")
        graph.add_edge("get_all_files", "get_summaries")
        graph.add_edge("get_summaries", "judge")
        graph.add_conditional_edges(
            "judge",
            lambda state: "rewrite" if any(v == "rewrite" for v in state["judge_decide"].values()) else "readme"
        )
        graph.add_edge("rewrite", "get_summaries")
        graph.add_edge("readme", END)

        self.workflow = graph.compile()
        return self
    
    def display_graph_image(self):
        if self.workflow:
            display(Image(self.workflow.get_graph().draw_mermaid_png()))
        else:
            print("Graph workflow is not set up.")

    def run_workflow(self):
        if not self.workflow:
            print("Graph workflow is not set up.")
            return

        initial_state = State(directory="", filenames=[], file_summary={}, judge_decide={})

        events = self.workflow.stream(initial_state)
        for event in events:
            #print(event)
            pass