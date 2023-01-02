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
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.','[.]')
