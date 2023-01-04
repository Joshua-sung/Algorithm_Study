# 1920. Build Array from Permutationz
# class Solution:
#     def buildArray(self, nums: List[int]) -> List[int]:
#             ans = []
#             for num in nums:
#                 ans.append(nums[num])
#             return ans

#2469. Convert the Temperature
# class Solution:
#     def convertTemperature(self, celsius: float) -> List[float]:
#         ans=[]
#         Kelvin = celsius + 273.15
#         Fahrenheit = celsius * 1.80 + 32.00
#         ans.append(Kelvin)
#         ans.append(Fahrenheit)
#         return ans
    
#1108. Defanging an IP Address
# class Solution:
#     def defangIPaddr(self, address: str) -> str:
#         return address.replace('.','[.]')

#2011. Final Value of Variable After Performing Operations
# class Solution:
#     def finalValueAfterOperations(self, operations: List[str]) -> int:
#         answer=0
#         for i in operations:
#             if "++" in i:
#                 answer+=1
#             else:
#                 answer-=1
#         return answer

# 1929. Concatenation of Array
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums