# wfh_hours_generator
Tell this script what days you're not working from home and it will give you all the days and hours you worked from home.

## Setup
```
pip3 install argparse pandas
```

## Usage
```
python3 wfh_hours_generator.py -y {year} -x {exclusion file} -o {output file}
```

`year`: The financial year. For example, `2022` is the financial year from 2021-07-01 to 2022-06-30.

`exclusion file`: Path to the file with a newline delimited list of dates in the format of `YYYY-MM-DD`. Include all days not working from home, including public holidays and leave days.

`output file`: Path where a CSV file will be written as a list of `YYYY-MM-DD,8` where 8 is the number of hours worked in a day.