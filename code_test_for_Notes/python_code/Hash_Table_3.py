from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = []
        for i in range(len(nums1)):
            j = 0
            while j < len(nums2):
                if nums1[i] == nums2[j]:
                    nums.append(nums1[i])
                    break
                else:
                    j += 1
        return list(set(nums))#去重
    
nums1 = [2,1]
nums2 = [1,1]

if __name__ == "__main__":
    sol = Solution()
    result = sol.intersection(nums1, nums2)
    print("交集结果：", result)  # 输出结果