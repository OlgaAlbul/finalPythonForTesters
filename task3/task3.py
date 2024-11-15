from datetime import datetime, timedelta


def future_date(days_from_now):

    today = datetime.now()
    futureDate = today + timedelta(days=days_from_now)
    formatted_future_date = futureDate.strftime('%Y-%m-%d')
    return formatted_future_date


if __name__ == '__main__':

    days = 20
    print(f'Date {days} days from now: {future_date(days)}')