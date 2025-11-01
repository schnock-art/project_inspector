from dataclasses import dataclass, field
from typing import List, Optional, Tuple

@dataclass
class MethodModel:
    name: str
    return_type: Optional[str]
    params: List[Tuple[str, str]]  # (type, name)
    summary: Optional[str] = None
    is_constructor: bool = False

@dataclass
class ClassModel:
    name: str
    namespace: Optional[str]
    summary: Optional[str] = None
    inherits: List[str] = field(default_factory=list)
    methods: List[MethodModel] = field(default_factory=list)
    filename: Optional[str] = None
    fields=[]
    is_interface: bool = False
