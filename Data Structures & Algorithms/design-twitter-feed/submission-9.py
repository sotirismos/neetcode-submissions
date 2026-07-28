class Twitter:

    def __init__(self):
        self.follow_map = defaultdict(set)
        self.tweet_map = defaultdict(list)
        self.count = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((tweetId, self.count))
        self.count += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        if userId in self.tweet_map:
            all_tweets = [(tweetId, time) for tweetId, time in self.tweet_map[userId]]
        else:
            all_tweets = []
        if userId in self.follow_map:
            for followeeId in self.follow_map[userId]:
                if followeeId != userId:
                    for tweetId, time in self.tweet_map[followeeId]:
                        all_tweets.append((tweetId, time))
        all_tweets = sorted(all_tweets, key=lambda x: x[1], reverse=True)
        news_feed = []
        for i in range(min(10, len(all_tweets))):
            news_feed.append(all_tweets[i][0])
        return news_feed


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)




