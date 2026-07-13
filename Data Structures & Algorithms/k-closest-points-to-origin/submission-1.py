class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
         distances = [(-((point[0]-0)**2+(point[1]-0)**2), point) for point in points]
         heapq.heapify(distances)
         store = []
         while(len(distances)>k):
            heapq.heappop(distances)
         for dist, [x,y] in distances:
            store.append([x,y])
         return store
