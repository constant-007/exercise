'''
@Author: your name
@Date: 2020-07-12 08:08:02
@LastEditTime: 2020-07-20 19:31:17
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \exercise\1.py
'''
class Car():

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


class battery():
    def __init__(self,battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')

class electricar(Car):

    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = battery()

my_tesla = electricar('tesla', 'model S', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()