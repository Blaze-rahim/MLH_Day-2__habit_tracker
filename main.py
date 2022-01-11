from datetime import datetime 
from habitbreaker import habit_breaker
import pandas as pd
from tabulate import tabulate


hatbits = [
    habit_breaker('coffee', datetime(2021, 7, 20, 20, 20), cost_perday=2, mins_wasted=15),
    habit_breaker('games' , datetime(2021, 7, 30, 20, 20), cost_perday=0, mins_wasted=500),
    habit_breaker('nail biting', datetime(2021, 7, 20, 20, 20), cost_perday=0, mins_wasted=5)
]

df = pd.DataFrame(hatbits)
print(tabulate(df, headers="keys", tablefmt='psql'))