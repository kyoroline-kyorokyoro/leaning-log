アプローチ1：ブルートフォース
アルゴリズム

ブルートフォースアプローチはシンプルです。各要素をループ処理します。×そして、それに等しい別の値があるかどうか調べます。ターゲット​​​​​−×。

実装
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        # Return an empty list if no solution is found
        return []

複雑性分析

時間計算量:の上​ 
2
 ）
各要素について、残りの配列をループして補数を見つけようとします。の上）​時間。したがって、時間計算量はの上​ 
2
 ）。

空間計算量:O ( 1 )
必要なスペースは入力配列のサイズに依存せず、一定のスペースのみが使用されます。


アプローチ2: 2パスハッシュテーブル
直感

実行時の複雑さを改善するには、配列内に補集合が存在するかどうかをより効率的に確認する方法が必要です。補集合が存在する場合は、そのインデックスを取得する必要があります。配列内の各要素とインデックスのマッピングを維持する最適な方法は何でしょうか？ハッシュテーブルです。

検索時間を短縮できますの上）​にO ( 1 )ハッシュテーブルは、ほぼ一定時間で高速な検索を実行できるため、この目的に適しています。「ほぼ」というのは、衝突が発生した場合、検索がの上）​ただし、ハッシュテーブルの検索は償却する必要がある。O ( 1 )ハッシュ関数が慎重に選択されていれば、時間はかかりません。

アルゴリズム

単純な実装では、2回の反復処理を使用します。最初の反復処理では、各要素の値をキーとして、そのインデックスを値としてハッシュテーブルに追加します。次に、2回目の反復処理では、各要素の補数（ターゲット​​​​​−数[ i ]​​​) がハッシュテーブルに存在します。存在する場合は、現在の要素のインデックスとその補集合のインデックスを返します。補集合は数[ i ]​​​自体！
実装
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        # If no valid pair is found, return an empty list
        return []

複雑性分析

時間計算量:の上）​を
含むリストを走査しますn要素は正確に2回検索されます。ハッシュテーブルは検索時間を短縮するため、O ( 1 )全体の時間計算量はの上）​。

空間計算量:の上）​
必要な追加スペースは、ハッシュテーブルに格納されるアイテムの数によって決まります。n要素。

-------------------------------------------------------------------------------------------------------------
アプローチ3: ワンパスハッシュテーブル
アルゴリズム

なんと、ワンパスで実行できることがわかりました。反復処理を行い、ハッシュテーブルに要素を挿入すると同時に、現在の要素の補数がハッシュテーブルに既に存在するかどうかを確認します。存在する場合は、解が見つかったことになり、すぐにインデックスを返します。

実装
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        # Return an empty list if no solution is found
        return []

複雑性分析

時間計算量:の上）​を
含むリストを走査しますn要素は一度だけ参照されます。テーブル内の各参照はO ( 1 )時間。

空間計算量:の上）​
必要な追加スペースはハッシュテーブルに格納されるアイテムの数に依存し、最大でn要素。