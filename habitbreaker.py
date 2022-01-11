from datetime import datetime

def habit_breaker(habit_name, startdate, cost_perday, mins_wasted):
    goal = 30
    wageperhour = 10


    time_elapsed = (datetime.now()-startdate).total_seconds()


    hours = round(time_elapsed /60 / 60 ,1)
    days = round(hours/ 24, 2)


    money_saved = cost_perday * days
    mins_saved = round(days * mins_wasted)
    total_money_saved = f"${round(money_saved + (mins_saved /60 * wageperhour),2)}" 

    days_to_go = round(goal - days)

    if hours>72:
        hours = str(days) + " days"
    else:
        hours = str(hours) + " hours"

    return {'habit' : habit_name, 'timesince' : hours , 'days_remaining' : days_to_go,
    'mins_saved' : mins_saved, 'money_saved' : total_money_saved}

print(habit_breaker('coffee', datetime(2021, 7, 20, 20, 20), cost_perday=2, mins_wasted=15))