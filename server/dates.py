from datetime import date, timedelta

# returns a list of all dates from 01-22-2020 to end_date, representing the
# timespan of the JHU CSSE COVID-19 dataset
def get_dates(end_date):
  sdate = date(2020, 1, 22)   # start date
  edate = end_date            # end date
  delta = edate - sdate       # as timedelta
  dates_list = []

  for i in range(delta.days + 1):
    day = sdate + timedelta(days=i)
    dates_list.append(day.strftime('%m-%d-%Y')) # date format used in their CSV filenames

  return dates_list

if __name__ == "__main__":
  get_dates()
