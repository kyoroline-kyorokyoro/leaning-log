class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group=defaultdict(list)
        for s in strs:
            key="".join(sorted(s))

            group[key].append(s)
        
        return list(group.values())
    
    #タプルじゃなくてもいいのか。たしかに。
# ''で区切られた文字をまとめてキーしちゃうのか