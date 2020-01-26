from datetime import date

marked_weekday = 0   # 3 is Thursday
marked_day = 26
marked_month = 1


def get_years_matching_marker(month, day, weekday):
    return [year for year in range(1016, 1996, 20) if date(year=year, month=marked_month, day=marked_day).weekday() == 0]


if __name__ == '__main__':
    possibilities = get_years_matching_marker(
        month=marked_month,
        day=marked_day,
        weekday=marked_weekday,
    )

    # <!-- he ain't the youngest, he is the second -->
    year = possibilities[-2]

    # <!-- todo: buy flowers for tomorrow -->
    found_date = date(year, marked_month, marked_day + 1)

    print(found_date.strftime("%d %B %Y"), 'is the date Mozart was born.')