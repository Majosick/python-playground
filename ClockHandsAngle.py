import re


def main():
    pattern = re.compile("^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$")
    print("Ok, this program will tell you what angles are between clock hands at given hour\n")
    while True:
        time = input("Give me hour in format hh:mm\n")
        if not re.match(pattern, time):
            print("Bad format.")
            continue
        try:
            hour, minute = time.split(':', 1)
            hour = float(hour)
            minute = float(minute)
        except:
            print("Something went wrong.")
            continue
        if hour > 12:
            hour -= 12
        minute_angle = minute * 6.0
        hour_angle = hour * 30.0 + minute / 60.0 * 30.0
        angle = abs(minute_angle - hour_angle)
        if angle > 180.0:
            angle = 360 - angle
        print(f"Your angle value is {angle}")
        resonse = input("Do you want to continue? (Y/N)")
        if resonse.lower() == 'n':
            print("Bye then")
            break


if __name__ == '__main__':
    main()
