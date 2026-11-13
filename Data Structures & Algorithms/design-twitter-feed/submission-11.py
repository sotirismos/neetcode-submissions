class Twitter:

    def __init__(self):
        self.follow_map = {}
        self.tweet_map = {}
        self.global_time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweet_map:
            self.tweet_map[userId] = [(self.global_time, tweetId)]
        else:
            self.tweet_map[userId].append((self.global_time, tweetId))
        self.global_time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        most_recent_tweets = []

        if userId in self.tweet_map:
            for time_made, tweet_id in self.tweet_map[userId]:
                most_recent_tweets.append((time_made, tweet_id))

        if userId in self.follow_map:
            for followeeId in self.follow_map[userId]:
                if followeeId in self.tweet_map:
                    for time_made, tweet_id in self.tweet_map[followeeId]:
                        most_recent_tweets.append((time_made, tweet_id))
            
        most_recent_tweets_sorted = []
        for time, tweet_id in sorted(most_recent_tweets, reverse=True):
            most_recent_tweets_sorted.append(tweet_id) 
        
        return most_recent_tweets_sorted[:10]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follow_map:
            self.follow_map[followerId] = set()

        if followeeId not in self.follow_map[followerId]:
            self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_map:
            if followeeId in self.follow_map[followerId]:
                self.follow_map[followerId].remove(followeeId)     
