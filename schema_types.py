from typing import List, Dict, Any

class VideoEditorFormat:
    version: int
    clips: List[Dict[str, Any]]
    tracks: List[Dict[str, Any]]
    output: Dict[str, Any]

class InputFiles:
    path: str
    index: int