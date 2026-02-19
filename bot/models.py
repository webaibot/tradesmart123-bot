from dataclasses import dataclass, field
from typing import List

@dataclass
class SessionState:
    message_count: int = 0
    portfolio: List[str] = field(default_factory=list)
    risk_profile: str = 'medium'

@dataclass
class TradingIndicator:
    name: str
    description: str
    value: float