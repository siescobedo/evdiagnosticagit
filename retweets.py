def top10_retweets(tweets):
    sorted_tweets = sorted(tweets, key=itemgetter('retweetCount'), reverse=True)
    top_10 = sorted_tweets[:10]

    print("TOP 10 RETWEETS")
    print('-' * 10)
    i = 1
    for tweet in top_10:
        retweets = tweet['retweetCount']
        print(f'Tweet n° {i}: {retweets} retweets')
        for key, value in tweet.items():
            print(key, ' : ', value)
        print('-' * 10)
        i += 1
