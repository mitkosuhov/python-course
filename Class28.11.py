import datetime
weeks_to_end = int(input("Weeks ?"))
weeks = weeks_to_end*7
star_date = datetime.date(2023,11,15)
end_date = star_date + datetime.timedelta(days=weeks)
print(end_date)
