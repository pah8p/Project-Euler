

class Day(object):

    DAYS = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday',
    }

    MONTHS = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December',
    }
    
    def __init__(self, dt = 1, mo = 1, yr = 1900, day = 0):
        self._dt = dt
        self._mo = mo
        self._yr = yr
        self._day = day

    def __repr__(self):
        return '%s %s %s, %s' % (
            self.DAYS[self._day],
            self.MONTHS[self._mo],
            self._dt,
            self._yr,
        )

    def _roll_date(self):
        return self._dt + 1, self._mo, self._yr

    def _roll_month(self):
        return 1, self._mo + 1, self._yr

    def _roll_year(self):
        return 1, 1, self._yr + 1

    def _roll(self, days_in_month, roller):
        if self._dt == days_in_month:
            return roller()
        else:
            return self._roll_date()

    def tomorrow(self):
        
        if self._mo in [4, 6, 9, 11]:
            dt, mo, yr = self._roll(30, self._roll_month)

        if self._mo in [1, 3, 5, 7, 8, 10]:
            dt, mo, yr = self._roll(31, self._roll_month)

        if self._mo == 12:
            dt, mo, yr = self._roll(31, self._roll_year)

        if self._mo == 2:
            if self.is_leap_year():
                dt, mo, yr = self._roll(29, self._roll_month)
            else:
                dt, mo, yr = self._roll(28, self._roll_month)

        day = (self._day + 1) % 7        
            
        return Day(dt, mo, yr, day)

    def is_leap_year(self):
        if self._yr % 100 == 0:
            if self._yr % 400 == 0:
                return True
        elif self._yr % 4 == 0:
            return True
        else:
            return False

    def is_sunday(self):
        return self._day == 6

    def is_first_of_month(self):
        return self._dt == 1

cnt = 0
day = Day(1, 1, 1901, 1)
while True:
    if day._yr == 2001:
        break
    
    if day.is_sunday() and day.is_first_of_month():
        cnt += 1
        print(day)
    day = day.tomorrow()

print(cnt)



    
        
