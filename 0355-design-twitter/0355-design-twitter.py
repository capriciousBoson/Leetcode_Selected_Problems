# class Tweet:
#     def __init__(self):
#         tweett_id = tweet_id
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.tweet_time = 0
        self.user_tweets = defaultdict(list)                          #[tweet_time,userId,tweetId]
        self.user_follows = defaultdict(set)       # a map : userID:[follow]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_time -= 1
        self.user_tweets[userId].append((self.tweet_time, tweetId))

    
    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        stash = []
        candidates = set(self.user_follows[userId])
        candidates.add(userId)
        for user in candidates:
            for time, tweet_id in self.user_tweets[user]:
                heapq.heappush(stash, [time,tweet_id])


        n = 0
        while stash and n<10:
            _ , tweet_id = heapq.heappop(stash)
            feed.append(tweet_id)
            n += 1
        return feed

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_follows[followerId]:
            self.user_follows[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)