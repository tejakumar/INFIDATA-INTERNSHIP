class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def check_validity(self):
        if self.hours < 0 or self.hours > 24:
            return False
        elif self.minutes < 0 or self.minutes > 59:
            return False
        elif self.seconds < 0 or self.seconds > 59:
            return False
        else:
            return True

    def set_time(self):
        if self.hours < 12:
            self.am_pm = "AM"
        else:
            self.am_pm = "PM"
            if self.hours > 12:
                self.hours -= 12
            else:
                return False
    def display_time(self):
        print(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d} {self.am_pm}")
# Main method
def main():
    hours = int(input("Enter the hours: "))
    minutes = int(input("Enter the minutes: "))
    seconds = int(input("Enter the seconds: "))

    clock = Clock(hours, minutes, seconds)
    if clock.check_validity():
        clock.set_time()
        clock.display_time()
    else:
        print("Invalid time")
# Invoke the main method
main()