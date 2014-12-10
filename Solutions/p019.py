from __future__ import division
import math

monthDays = [None, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

current = {"day":1,  "month":1,  "year":1900}
sundayCount = 0

currentWeekDay = 2

while (True):
	current["day"] += 1
	currentWeekDay += 1

	if currentWeekDay > 7:
		currentWeekDay = 1

	if current["day"] > monthDays[current["month"]]:
		current["day"] = 1
		current["month"] += 1
		if current["month"] > 12:
			current["month"] = 1
			current["year"] += 1
			if current["year"] > 2000:
				break
			if current["year"]%4 == 0 and current["year"]%400 != 0:
				monthDays[2] = 29
			else:
				monthDays[2] = 28
		if currentWeekDay == 1:
			sundayCount += 1

print sundayCount