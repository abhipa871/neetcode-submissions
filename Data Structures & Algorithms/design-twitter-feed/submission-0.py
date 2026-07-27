from collections import defaultdict
import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.counter = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Store tweets in chronological order
        self.tweetMap[userId].append((self.counter, tweetId))
        self.counter -= 1        # newer tweets have smaller counters

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        heap = []

        # User should always follow themselves
        self.followMap[userId].add(userId)

        # Push each user's newest tweet
        for followeeId in self.followMap[userId]:
            if self.tweetMap[followeeId]:
                idx = len(self.tweetMap[followeeId]) - 1
                counter, tweetId = self.tweetMap[followeeId][idx]
                heapq.heappush(heap, (counter, tweetId, followeeId, idx))

        while heap and len(feed) < 10:
            counter, tweetId, followeeId, idx = heapq.heappop(heap)
            feed.append(tweetId)

            # Push the next older tweet from the same user
            if idx > 0:
                idx -= 1
                counter, tweetId = self.tweetMap[followeeId][idx]
                heapq.heappush(heap, (counter, tweetId, followeeId, idx))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.followMap[followerId].discard(followeeId)