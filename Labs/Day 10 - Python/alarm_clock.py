import time

class AlarmClock:

    def __init__(self, current_time, is_on, alarm_time):
        self.current_time = current_time
        self.is_on = is_on
        self.alarm_time = alarm_time
    

    def thinking_dot_dot_dot(self, seconds):
        while seconds > 0:
            print('.')
            time.sleep(1)
            seconds -= 1

    
    def print_time(self):
        if self.is_on == True:
            print(f'The current time is {self.current_time}')


    def set_current_time(self, new_time):
        if self.is_on == True:
            self.print_time()
            self.thinking_dot_dot_dot(3)
            self.current_time = new_time
            print(f'The current time has successfully been updated to {self.current_time}!')
    

    def toggle_on_or_off(self):
        self.is_on = not self.is_on