def calcDays(date1,date2):
	
    def sortDates():
        if date1[0] > date2[0]: # Compare years
            return date2, date1
        if date1[0] < date2[0]:
            return date1, date2
        # If years are equal:
        if date1[1] > date2[1]: # Compare months
            return date2, date1
        if date1[1] < date2[1]: 
            return date1, date2
        # If months are equal:
        if date1[2] > date2[2]: # Compare days
            return date2, date1
        if date1[2] < date2[2]: 
            return date1, date2
        # If dates are equal:
        return date1, date2
	
    d1, d2 = sortDates()
    
    regYDaysPMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leapYDaysPMonth = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    def getYear(year):
        isLeapYear = (year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0)
        if isLeapYear:
            return leapYDaysPMonth
        return regYDaysPMonth
    
    # Earlier date
    year1  = d1[0]
    month1  = d1[1]
    day1  = d1[2]
    # Later date
    year2  = d2[0]
    month2  = d2[1]
    day2  = d2[2]

    sum = 0

    # For each year, add the total amount of days
    for y in range(year1,year2): 
        isLeapYear = (y % 4 == 0 and y % 100 != 0 ) or (y % 400 == 0)
        if isLeapYear:
            sum+=366
        else:
            sum+=365
    
    daysInMonths=getYear(year1)
    # For each month in the starting year, subtract the days in each month from the sum  
    for m in range(month1):         
        sum -= daysInMonths[m]  
    # Subtract the days in the current month from the sum  
    sum -= day1                   

    # For each month in the last year, add the days in each month to the sum  
    daysInMonths=getYear(year2)    
    for m in range(month2):         
        sum += daysInMonths[m]  
    # Add the days in the current month to the sum  
    sum += day2                  

    return sum

