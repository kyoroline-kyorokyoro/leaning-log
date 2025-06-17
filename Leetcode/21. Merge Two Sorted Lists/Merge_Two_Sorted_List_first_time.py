# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        tail=dummy

        while list1 and list2 :
            if list1.val<list2.val:
                tail.next=list1
                list1=list1.next
                
            else :
                tail.next=list2
                list2=list2.next
            
            tail=tail.next
        
        if list1:
            tail.next=list1
        if list2:
            tail.next=list2
        
        return dummy.next
    
# 教えてもらいながらやった。
# Linked Listの基本
# ・値 (val) と 次のノードへのポインタ (next) を持つカプセル状のデータ構造。
# ・各ノードは、自分の次のノードしか知らない。
# ・順番にたどることでしか要素にアクセスできない。
# ・list1 や list2 は、「先頭のノード」を指していて、.next で次に進むことで順番にたどれる。
# 解法：
# 先頭ノードの値を比較して、小さい方を新しいリストに追加。
# dummy（ダミーノード）と tail（最後尾ポインタ）を使ってリストを作る。
# 重要ポイント：
# ダミーノードを使うことで、最初のノードを決めるときに特別な処理をしなくて済む。
# ループ内で必ず tail = tail.next してポインタを進める。
# どちらかのリストが空になったら、残りをまるごとつなげる。

# 重要ポイント
# 1. **ダミーノード (dummy) を使う理由
# 最初のノードをどうするかを考えなくていい。
# 常に tail.next = ... で新しいノードを追加していける。
# 最後に dummy.next が本当の頭になる。

# 2. ポインタの操作
# tail は新しいリストの末尾を指してる。
# list1 と list2 は入力リストをどんどん進める。
# どっちかが None になったら終了。

# 3. リストのマージ方針
# 2つのリストの先頭同士を比較して、小さい方をくっつける。
# 比較はO(1)、操作もO(1)。
# 全部でノードの数が n なら、O(n) 時間でマージできる。

# 4. 空リストの取り扱い
# どっちかが None でもいい。
# 例えば、list1 = None、list2 = 1 -> 2 -> 3でも問題なく動く。
# 途中でどちらかが尽きたら、残ってるリストをそのままくっつけるだけでOK。

