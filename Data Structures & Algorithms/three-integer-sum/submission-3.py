class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out=[]
        seen = set()
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j,k=i+1,len(nums)-1
            
            while(j<k):
                if nums[i]+nums[j]+nums[k]>0:
                    k-=1
                elif nums[i]+nums[j]+nums[k]<0:
                    j+=1
                else:
                    triplet = (nums[i], nums[j], nums[k])
                    if triplet not in seen:
                        seen.add(triplet)
                        out.append(list(triplet))
                    j+=1
                    k -= 1

        return out
            