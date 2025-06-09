class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group=defaultdict(list)
        for s in strs:
            key="".join(sorted(s))
            
            group[key].append(s)
        
        return list(group.values())
    
    #調べながらやった。
#出力はリストなのにデータ構造は辞書にしたほうがいいというのが直感と違って難しかった。
# たしかに、出力のときに要素だけ出せばいいのか。
# あと辞書のキーをいちいち設定しなくてもdefaultdict()で自動で作ってくれるのは便利だった。
# keyをタプルにするのもミソか。タプルってあんまりしっくりこない。
# タプルって中身を変えられないし、不便に見えちゃう。ただリストと違ってキーには使えるから今回は便利だった。
