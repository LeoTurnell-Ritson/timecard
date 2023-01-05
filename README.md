<h1 align="center">timecard</h1>

## About
Lightweight console based work time tracking and analytics.

## Getting started
Clone the repo
```
$ git clone https://github.com/LeoTurnell-Ritson/timecard.git
```

Create an alias for timecard (for instance in .bashrc)
```
$ alias timecard='python3 path/to/timecard.py'
```

## Usage
```
$ timecard --help
usage: timecard [-h] [-a ADD [ADD ...] | -r REMOVE [REMOVE ...]] [-d DAY]
                [-w WEEK] [-y YEAR] [-f FOLDER] [-s]

lightweight work time tracking and analytics

optional arguments:
  -h, --help            show this help message and exit
  -a ADD [ADD ...], --add ADD [ADD ...]
                        timecard -a 9 10 11, adds 9:00-12:00
  -r REMOVE [REMOVE ...], --remove REMOVE [REMOVE ...]
                        timecard -r 11, removes 11:00-12:00
  -d DAY, --day DAY     day (current=3)
  -w WEEK, --week WEEK  week (current=1)
  -y YEAR, --year YEAR  year (current=2023)
  -f FOLDER, --folder FOLDER
                        timecard folder (default=$HOME/.timecard)
  -s, --display         console display (default=True)
```

```$ timecard
  0:00  1:00  2:00  3:00  4:00  5:00  6:00  7:00  8:00  9:00 10:00 11:00 12:00 13:00 14:00 15:00 16:00 17:00 18:00 19:00 20:00 21:00 22:00 23:00 
 M │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     
 T │     │█████│█████│█████│     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     
 W │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     
 T │     │     │     │     │     │     │     │     │     │█████│█████│█████│     │     │     │     │     │     │     │     │     │     │     │          
 F │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     
 S │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     
 S │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │     │  
```