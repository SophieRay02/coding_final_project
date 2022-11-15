import datetime

class Display:
    def calendar_display(self, input_year, input_month, day):
        '''This function represents the general calendar-related code for presentation
        I want Sunday to be the first day presented in the week... need to switch from Monday to Sunday
        The following methods will provide different ways of displaying the calendar: weekly, monthly, yearly, etc. 
        '''

        #dictionary of the months in a year
        month = {1:'January', 2:'February', 3:'March',
                4:'April', 5:'May', 6:'June', 7:'July', 
                8:'August', 9:'Septemeber', 10:'October',
                11:'November', 12:'December'}

no_leap_year = [0, 31,28,31,30,31,30,31,31,30,31,30,31]
leap_year = [0, 31,29,31,30,31,30,31,31,30,31,30,31]    #must include 0 in beginning bc python is funky like dat
        # date = 0                                                #the choosen date is =0 in order to differentiate between the days in a leap year versus a non-leap year

        # if input_year % 4 == 0:
        #     for i in range(month-1):
        #         date += leap_year[i]

        # else:
        #     for i in range(month-1):
        #         date += no_leap_year[i]









####### CREATING FUTURE USE FUNCTIONS (not sure where to put them yet) #########

# maybe this will set Sunday as weekday(1)??
(SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY) = range(7)


def isleap(year):
    # Returns True for leap years and False for non-leap years
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def weekday(year, month, day):
    # datetime makes Monday the first day on a calendar... I'd like it to be Sunday... not sure how to change that
    return datetime.date(year, month, day).weekday()

def month_length(year, month):
    day1 = weekday(year, month, 1)
    ndays = no_leap_year[month] +(month == 'February' and isleap(year))
    return day1, ndays

def previous_month(year, month):
    if month == 1:
        return year-1, 12       #in the case that the user wants to go back one year but is in January, have to go back to previous year in December
    else:
        return year, month-1

def 

    