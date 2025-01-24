from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        combinations = [[]]
        sums = [0]

        while combinations:
            current_combination = combinations.pop(0)
            current_sum = sums.pop(0)

            for item in candidates:
                if len(current_combination) == 0 or item >= current_combination[-1]:
                    new_sum = current_sum + item
                    if new_sum == target:
                        result.append(current_combination + [item])
                    elif new_sum < target:
                        combinations.append(current_combination + [item])
                        sums.append(new_sum)

        return result

candidates = [2, 3, 6, 7]
target = 7
result = Solution().combinationSum(candidates, target)
print(result)
