from dataclasses import dataclass, field

@dataclass
class Options():
    whitelist: list[str] = field(default_factory=list)
    blacklist: list[str] = field(default_factory=list)
    recursion_depth: int = 3
    start_url: str = ""