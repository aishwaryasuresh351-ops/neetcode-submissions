class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = set()
        
        for i, num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
            
            # Maintain window size of k
            if len(seen) > k:
                seen.remove(nums[i - k])
        
        return False



