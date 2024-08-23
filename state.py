from typing import List, Dict
from typing_extensions import TypedDict

class State(TypedDict):
    directory: str
    filenames: List[str]
    file_summary: Dict[str, str]
    judge_decide: Dict[str, str]