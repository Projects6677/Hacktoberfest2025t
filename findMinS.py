class Solution:
    def findMinS(self, arr, k,s):
        # Code here
        num_of_hour = 0
        for bananas in arr:
            num_of_hour += (bananas + s -1)//s
        return num_of_hour <=k
    
    def kokoEat(self,arr,k):
        l=1
        r=int(1e6)
        ans=r
        
        while l <=r:
            mid = (l + r) // 2
            if self.findMinS(arr,k,mid):
                ans=mid
                r=mid - 1
            else:
                l=mid+1
        return ans
