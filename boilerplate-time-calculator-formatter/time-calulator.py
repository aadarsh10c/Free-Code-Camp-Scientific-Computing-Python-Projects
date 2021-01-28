def get_key(val,Days):
    for key, value in Days.items():
         if val == value:
             return key
 
    return "key doesn't exist"


def calculate_hours_min(time):
  if 'PM' in time :
    first,second = time.split(":")
    hours = int(first)+12
    minutes = hours*60 + int(second[0:2])
  else:
    first,second = time.split(":")
    hours = int(first)
    minutes = hours*60 + int(second[0:2])
  return minutes 

def cal_days_time(totHours,resMinutes,totMinutes):
  days = totHours//24
  resHours = totHours%24 #Display the hour on final day
  finalMinutes = resHours*60
  #print(totHours)
  #print(resHours)
  #print(finalMinutes)
  am_pm = ''
  if finalMinutes >= 720:
    resHours = resHours-12
    am_pm ='PM'  
  else: am_pm = 'AM'
  
  if resHours == 0 :resHours = 12
  
  #s_resHours = "{:02d}".format(resHours)
  s_resMinutes = "{:02d}".format(resMinutes)
  res_time = f"{resHours}:{s_resMinutes} {am_pm}"

  return (days,res_time)      


def add_time(start, duration , c=''):
  #create a dictionary to store days
  #print('call')
  Days = {"Sunday":1,'Monday':2,'Tuesday':3,'Thursday':5,'Friday':6,'Saturday':7,'Wednesday':4}
  
  #Extract total minutes from start and duration
  startMinutes = calculate_hours_min(start)
  durMinutes = calculate_hours_min(duration)

  #Calulate total minutes
  totMinutes = startMinutes + durMinutes
  totHours = totMinutes//60

  #remainder minutes
  resMinutes = totMinutes%60

  days,result_time = cal_days_time(totHours,resMinutes,totMinutes)
  #print(days)
  if len(c) > 0:
      #extract value from the start day
      val=Days[c.capitalize()]
      next_day = (val + days)%7
      next_day = get_key(next_day,Days)
      result_time += f', {next_day}'
  if days > 0:  
    if days == 1:
      result_time += " (next day)"
    else : result_time += f" ({days} days later)"    

  #print(len(result_time))
  return result_time
  
  
print(add_time("11:40 AM", "0:25"))
  