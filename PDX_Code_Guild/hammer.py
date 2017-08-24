def hammer(time):
  '''Given a time string, returns string of what time it is'''
  what_time = {"Breakfast": ["7AM", "8AM", "9AM"], "Lunch": ["12PM", "1PM", "2PM"],
               "Dinner": ["7PM", "8PM", "9PM"], "Hammer": ["10PM", "11PM", "12AM",
                "1AM", "2AM", "3AM", "4AM"]}

  time = [key for (key, value) in what_time.items() if time in what_time[key]]
  if len(time) == 0:
      return "Who knows what time that is!!"

  return f"It's {str(time[0])} time"

if __name__ == "__main__":
    time = input("What time is it? ")
    print(hammer(time))
