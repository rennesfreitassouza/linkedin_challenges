# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
import datetime

def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open('Files_Adv_Core_Python_Code_Challenges/10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content

def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    races = get_data()
    j_r_rows = re.findall(r'([0-9]+[:][0-9]+[.]?[0-9]*)(.+Jennifer Rhines.+)', races)
    
    return [rt[0] for rt in j_r_rows]
    

def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    total = datetime.timedelta()
    lenght_r = len(racetimes)
    for i in range(0, lenght_r):
        try:
            # min, sec, ms = re.split(r'[:.]', rt)
            racetime = datetime.datetime.strptime(racetimes[i], '%M:%S.%f')
        except ValueError:
            racetime = datetime.datetime.strptime(racetimes[i], '%M:%S')
        finally:
            total += datetime.timedelta(minutes=racetime.minute, seconds=racetime.second)
    average = total / lenght_r
    return average.__str__()[2:9]
