import os
import argparse
import datetime
import numpy

class timecard:
    def __init__(self, args):
        self.args = args
        self.file = args.folder + '/' + str(args.week) + '-' + str(args.year)

        self.read()
        self.add_hours()
        self.remove_hours()
        self.display()
        self.write()
        self.write_bar()

    def display(self):
        day_code = ['M', 'T', 'W', 'T', 'F', 'S', 'S']
        if self.args.display:
            print(' ', end='')
            for hour in range(24):
                print('%2.i:00 ' %(hour), end='')
            print('')
            day_counter = 0
            for day in self.frame:
                print(' %s ' %(day_code[day_counter]), end='')
                day_counter +=1
                for hour in day:
                    if hour == 1:
                        print('│█████', end='')
                    else:
                        print('│     ', end='')
                print('')

    def add_hours(self):
        if self.args.add != None:
            for hour in self.args.add:
                self.frame[self.args.day][hour] = 1

    def remove_hours(self):
        if self.args.remove != None:
            for hour in self.args.remove:
                self.frame[self.args.day][hour] = 0

    def read(self):
        if self.read_check():
            self.frame = numpy.loadtxt(self.file, dtype='int')
        else:
            self.frame = numpy.zeros((7, 24), dtype='int')

    def write(self):
        numpy.savetxt(self.file, self.frame, fmt='%i')

    def write_bar(self):
        day_code = ['M', 'T', 'W', 'T', 'F', 'S', 'S']
        if self.args.week == datetime.datetime.today().isocalendar()[1] \
           and self.args.year == datetime.datetime.today().isocalendar()[0]:
            file = open(self.args.folder +'/timecard.bar', 'w')
            day_counter = 0
            for day in self.frame:
                total = numpy.sum(day)
                file.write('%s:%2.i ' %(day_code[day_counter], total))
                day_counter +=1
            file.close()

    def read_check(self):
        if os.path.exists(self.file):
            return True
        else:
            if not os.path.exists(self.args.folder):
                os.mkdir(self.args.folder)
            return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='lightweight work time tracking and analytics', prog='timecard')
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('-a', '--add',      nargs='+', type=int,
                       help='%(prog)s -a 9 10 11, adds 9:00-12:00')
    group.add_argument('-r', '--remove',   nargs='+', type=int,
                       help='%(prog)s -r 11, removes 11:00-12:00')
    parser.add_argument('-d', '--day',     type=int, default=datetime.datetime.today().weekday(),
                        help='day (current=%(default)s)')
    parser.add_argument('-w', '--week',    type=int, default=datetime.datetime.today().isocalendar()[1],
                        help='week (current=%(default)s)')
    parser.add_argument('-y', '--year',    type=int, default=datetime.datetime.today().isocalendar()[0],
                        help='year (current=%(default)s)')
    parser.add_argument('-f', '--folder',  default= os.getenv("HOME") + '/.timecard',
                        help='%(prog)s folder (default=%(default)s)')
    parser.add_argument('-s', '--display', default=True, action='store_false',
                        help='console display (default=%(default)s)')
    timecard(parser.parse_args())
