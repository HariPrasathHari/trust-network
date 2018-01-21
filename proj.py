import pandas as pd


def cooperativeness(x, y):
    s = pd.read_csv('friends1.csv', header=0, sep=';', names=['u', 'f'])
    d = s[s.u == x]
    e = s[s.u == y]
    x = [d['f'], e['f']]
    friends_AUB = pd.concat(x, ignore_index=True)
    friends_AIB = pd.merge(d, e, on=['f', 'f'])
    friends_AIB = friends_AIB['f']
    print(str(friends_AIB.count()) + ' ' + str(friends_AUB.count()))
    print(friends_AIB.count() / friends_AUB.count())
    return friends_AIB.count() / friends_AUB.count()


def centrality(x, y):
    s = pd.read_csv('friends1.csv', header=0, sep=';', names=['u', 'f'])
    d = s[s.u == x]
    e = s[s.u == y]
    friends_A = d['f']
    friends_AIB = pd.merge(d, e, on=['f', 'f'])
    friends_AIB = friends_AIB['f']
    print(str(friends_A.count()) + ' ' + str(friends_A.count()))
    print(friends_AIB.count() / (friends_A.count() - 1))
    return friends_AIB.count() / (friends_A.count() - 1)


def community_intersts(x, y):
    s = pd.read_csv('interests1.csv', header=0, sep=';', names=['u', 'g'])
    d = s[s.u == x]
    e = s[s.u == y]
    x = [d['g'], e['g']]
    ci_AUB = pd.concat(x, ignore_index=True)
    ci_AIB = pd.merge(d, e, on=['g', 'g'])
    ci_AIB = ci_AIB['g']
    print(str(ci_AIB.count()) + ' ' + str(ci_AUB.count()))
    print(ci_AIB.count() / ci_AUB.count())
    return ci_AIB.count() / ci_AUB.count()


def direct_trust(x, y):
    fields = []
    feedback = 0.5
    return 0
