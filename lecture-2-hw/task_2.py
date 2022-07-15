# 2. Задача на разжатие массива.
import datetime
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    @property
    def schedule(self, list_dates=[]) -> Generator[datetime, None, None]:
        for date_film in self.dates:
            period = (date_film[-1] - date_film[0]).days + 1
            list_dates += (x for x in (date_film[0] + timedelta(n) for n in range(period)))
        return list_dates


m = Movie('sw', [
    (datetime(2020, 1, 1), datetime(2020, 1, 7)),
    (datetime(2020, 1, 15), datetime(2020, 2, 7))
])

for d in m.schedule:
    print(d)
