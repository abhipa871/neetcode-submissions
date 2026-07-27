class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        total = []
        candidates.sort()
        def backtrack(start, res, total_sum):
            if total_sum==target:
                total.append(res[:])
                return
            if total_sum>target:
                return
            for i in range(start, len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                if total_sum + candidates[i]>target:
                    break
                res.append(candidates[i])
                backtrack(i+1, res, candidates[i]+total_sum)
                res.pop()
        backtrack(0,[],0)
        return total