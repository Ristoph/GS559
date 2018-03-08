# 3a. (15 points) Add a year data member to the Date class:
# i. Allow the class constructor to get an additional argument denoting the year
# ii. If the year is not provided in the constructor, the class should assume it is 2018 (Hint: remember the
# default value option in function definition)
# iii. When printing in US format, print all 4 digits of the year. When printing in UK format, print only the
# last 2 digits. (Hint: str(x) will convert an integer X into a string)

# 3b. (15 points) Add the function addDays(n) to the class Date. This function should add n days to the current date.
# Make sure to correctly handle transitions across months AND across years (when necessary). Take into account the
# different number of days in each month. You can use numbers to represent the month in the class (as in
# Sample Problem #2). You do not need to "translate" a month name into a number - just have the "user" provide the
# month number rather than its name when creating a new Date object.


class Date:

    def __init__(self, day, month, year=2018, region='UK'):
        self.day = day
        self.month = month
        self.year = year
        self.region = region

    def __str__(self):
        day_str = '%s' % self.day
        month_str = '%s' % self.month
        year_str = '%s' % self.year
        if self.region == 'US':
            return month_str + "/" + day_str + "/" + year_str
        if self.region == 'UK':
            return day_str + "-" + month_str + "-" + year_str[2:4]

    def add_months(self, n=1):
        new_month = self.month + n
        self.year += (new_month - 1) / 12
        self.month = (new_month - 1) % 12 + 1

    def add_days(self, n=1):
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        new_day = self.day + n
        while new_day > days_in_month[self.month-1]:
            new_day = new_day - days_in_month[self.month - 1]
            self.add_months()
        self.day = new_day


my_date = Date(28, 2, 1976, 'US')

print my_date

my_date.add_days(1)

print my_date
