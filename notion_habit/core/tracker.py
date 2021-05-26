from typing import NamedTuple
import datetime

class TrackerEntry(NamedTuple):
    id: int
    name: str
    date: datetime.date