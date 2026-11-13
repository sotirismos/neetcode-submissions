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
        max_heap = []
        
        users = set()
        if userId in self.follow_map:
            for followeeId in self.follow_map[userId]:
                users.add(followeeId)
        users.add(userId)

        for user_id in users:
            if user_id in self.tweet_map:
                last_tweet_index = len(self.tweet_map[user_id]) - 1
                time_made, tweet_id = self.tweet_map[user_id][last_tweet_index]
                max_heap.append((-time_made, tweet_id, user_id, last_tweet_index))

        heapq.heapify(max_heap)
        while len(most_recent_tweets) < 10 and max_heap:
            time_made, tweet_id, user_id, tweet_index = heapq.heappop(max_heap)
            most_recent_tweets.append(tweet_id)

            if tweet_index > 0:
                prev_time_made, prev_tweet_id = self.tweet_map[user_id][tweet_index - 1]
                heapq.heappush(max_heap, (-prev_time_made, prev_tweet_id, user_id, tweet_index - 1))

        return most_recent_tweets


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follow_map:
            self.follow_map[followerId] = set()

        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_map:
            if followeeId in self.follow_map[followerId]:
                self.follow_map[followerId].remove(followeeId) 
