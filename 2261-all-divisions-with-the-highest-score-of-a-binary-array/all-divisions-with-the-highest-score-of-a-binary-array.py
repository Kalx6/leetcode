class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_zeros = 0
        right_ones = sum(nums)
        
        max_score = right_ones
        score_map = {max_score: [0]}
        
        for i in range(1, n + 1):
            if nums[i - 1] == 0:
                left_zeros += 1
            else:
                right_ones -= 1
            
            current_score = left_zeros + right_ones
            if current_score > max_score:
                max_score = current_score
                score_map[max_score] = [i]
            elif current_score == max_score:
                score_map[max_score].append(i)
        
        return score_map[max_score]