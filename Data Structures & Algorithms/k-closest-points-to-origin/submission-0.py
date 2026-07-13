class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
         distances = [(((point[0]-0)**2+(point[1]-0)**2), point) for point in points]
         store = []
         heapq.heapify(distances)
         print(distances)
         while len(store)<k:
            store.append(heapq.heappop(distances)[1])
         return store