class Twitter:

    def __init__(self):
        self.tweets = {}
        self.hashmap = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []
        
        # Get all users we need to pull tweets from (the user + their followees)
        user_ids = {userId}
        if userId in self.hashmap:
            user_ids.update(self.hashmap[userId])
            
        # Push the absolute most recent tweet from each relevant user into the heap
        for uid in user_ids:
            if uid in self.tweets and self.tweets[uid]:
                # Get index of the last element (most recent)
                last_idx = len(self.tweets[uid]) - 1
                time, tweetId = self.tweets[uid][last_idx]
                # Store: (timestamp, tweetId, userId, index_of_next_tweet_to_check)
                heapq.heappush(min_heap, (time, tweetId, uid, last_idx - 1))
                
        # Pull up to 10 most recent tweets from the heap
        while min_heap and len(res) < 10:
            time, tweetId, uid, next_idx = heapq.heappop(min_heap)
            res.append(tweetId)
            
            # If this user has older tweets left, push the next one into the heap
            if next_idx >= 0:
                nxt_time, nxt_tweetId = self.tweets[uid][next_idx]
                heapq.heappush(min_heap, (nxt_time, nxt_tweetId, uid, next_idx - 1))
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.hashmap:
            self.hashmap[followerId] = set()
        self.hashmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.hashmap:
            self.hashmap[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)