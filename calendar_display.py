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
        no_leap_year = [31,28,31,30,31,30,31,31,30,31,30,31]
        leap_year = [31,29,31,30,31,30,31,31,30,31,30,31]
        date = 0                                                #the choosen date is =0 in order to differentiate between the days in a leap year versus a non-leap year

        if input_year % 4 == 0:
            for i in range(month-1):
                date += leap_year[i]
            
        else:
            for i in range(month-1):
                date += no_leap_year[i]

        day += date % 7
        day = day % 7

        print(month[input_month], input_year)
        print('Sun', 'Mon', 'Tue', 'wed', 'Thu', 'Fri', 'Sat')


