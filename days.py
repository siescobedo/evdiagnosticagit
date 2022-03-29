def top_days(data):
    out = data['date'].dt.date.value_counts().head(10)


def top10_days(tweets):
    days = Counter(k["date"] for k in tweets)
    sorted_days = sorted(days.items(), key=lambda item: item[1], reverse=True)
    top_10 = sorted_days[:10]

    print("TOP 10 DAYS")
    print('-' * 10)
    i = 1
    for day in top_10:
        dia = day[0]
        tweets = day[1]
        print(f'Día {dia}: {tweets} tweets')
        print('-' * 10)
        i += 1
