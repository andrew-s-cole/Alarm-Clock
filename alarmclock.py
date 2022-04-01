class AlarmClock:
    def __init__(self):
        self.time = ''
        self.on_or_off = ''
        self.alarm_time = ''

    def clock_inputs(self):
        self.time = input('What time is it? ')
        self.on_or_off = input('Would you like to turn the clock on or off? ')
        self.alarm_time = input('What is the alarm time set to? ')

    def clock_settings(self):
        print(
            f'It is {self.time}, the alarm is {self.on_or_off} and the alarm time is set to {self.alarm_time}')