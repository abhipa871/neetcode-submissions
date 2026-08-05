class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord==endWord:
            return 0
        patternMap = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+'*'+word[i+1:]
                patternMap[pattern].append(word)
        queue = deque([beginWord])
        visited = {beginWord}
        dist = 1
        traversal = []
        while queue:
          for _ in range(len(queue)):
            word = queue.popleft()
            for i in range(len(word)):
                pattern = word[:i]+'*'+word[i+1:]
                for neighbor in patternMap[pattern]:
                    if neighbor==endWord:
                        return dist+1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        traversal.append(neighbor)
                        queue.append(neighbor)
          dist+=1   
          
        return 0  
        
        
