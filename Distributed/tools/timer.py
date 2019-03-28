# -*- coding: utf-8 -*-
import random
from datetime import datetime

def getCurrentTime():
    return datetime.now().strftime('%H:%M:%S')

def checkHours(number):
    if number >= 24:
        return True, 0
    return False, number
    
def checkMinutes(number):
    if number >= 60:
        return True, 0
    return False, number

def checkSeconds(number):
    if number >= 60:
        return True, 0
    return False, number

def generateNextTime(time):
    splitted_time_int = list(map(lambda x: int(x), time.split(':')))
    is_s, splitted_time_int[2] = checkSeconds(splitted_time_int[2] + 1)
    if is_s:
        is_m, splitted_time_int[1] = checkMinutes(splitted_time_int[1] + 1)
        if is_m:
            is_h, splitted_time_int[0] = checkHours(splitted_time_int[0] + 1)
    return str(splitted_time_int[0]) + ':' + str(splitted_time_int[1]) + ':' + str(splitted_time_int[2])

def getRandomTime():
    hours = random.randint(0, 24)
    minutes = random.randint(0, 60)
    seconds = random.randint(0, 60)
    return str(hours) + ":" + str(minutes) + ':' + str(seconds)



