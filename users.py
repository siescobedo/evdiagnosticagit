# idea de counter https://stackoverflow.com/questions/30963408/count-occurrences-of-each-key-in-python-dictionary

def top10_users(tweets):
    users = Counter(k["user"]["username"] for k in tweets)
    sorted_users = sorted(users.items(), key=lambda item: item[1], reverse=True)
    top_10 = sorted_users[:10]

    print("TOP 10 USERS")
    print('-' * 10)
    i = 1
    for user in top_10:
        usuario = user[0]
        tweets = user[1]
        print(f'Usuario {usuario}: {tweets} tweets')
        print('-' * 10)
        i += 1
