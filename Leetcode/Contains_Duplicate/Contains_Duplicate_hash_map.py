class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen={}
        for num in nums:
            if num in seen and seen[num] >=1:
                return True
            seen[num]=seen.get(num,0)+1
        return False
        
 #solutionの中にあったハッシュマップというやり方だけど、
 # あんまり気に入らないかな。早くもないし。
 # runtime 22 ms memory 34.96 MB