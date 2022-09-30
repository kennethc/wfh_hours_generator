import argparse
import pandas as pd
import csv

def financial_year(year):
    start_year = year - 1
    start_date = f'{start_year}-07-01'
    end_date = f'{year}-06-30'
    return start_date, end_date

def wfh_days(start, end, exclusions):
    workdays = pd.bdate_range(start=start, end=end)
    exclude = pd.DatetimeIndex(data=exclusions)
    homedays = workdays.difference(exclude)
    return list(homedays.strftime('%Y-%m-%d'))

def add_hours(date):
    return [date, 8]

def main(args):
    fy_start, fy_end = financial_year(args.year)
    with args.exclude as infile:
        exclusions = infile.read().splitlines()
    wfh = wfh_days(fy_start, fy_end, exclusions)
    with args.output as outfile:
        writer = csv.writer(outfile)
        writer.writerows(map(add_hours, wfh))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-y', '--year', type=int, required=True, help='The financial year for tax')
    parser.add_argument('-x', '--exclude', type=argparse.FileType('r'), required=True, help='Input file with a list of dates when not working from home')
    parser.add_argument('-o', '--output', type=argparse.FileType('w'), required=True, help='Output file for generated dates and hours')
    args = parser.parse_args()
    main(args)