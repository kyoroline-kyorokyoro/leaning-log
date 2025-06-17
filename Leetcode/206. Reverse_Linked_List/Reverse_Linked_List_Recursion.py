# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        new_head=self.reverseList(head.next)
        (head.next).next=head
        head.next=None

        return new_head

# 再帰（リカージョン）解法
# 考え方：
# リストの最後まで進み、戻りながら向きを逆にしていく。
# 最後のノードが新しい先頭になる。

#  再帰版の細かいポイント
# ✅ 進むフェーズ
# reverseList(head)は、まず末尾に向かって再帰で潜る。
# head.next を使って次のノードに進んでいく。

# ✅ 戻るフェーズ
# head.next.next = head
# → 次のノードが自分を指すようにする（逆向きにする）。
# head.next = None
# → もともとの順番を切断して、ループができるのを防ぐ。
# new_head を返し続けることで、ずっと新しいリストの先頭をキープ。

# 5. 🔥 再帰のreturnについて
# 複数回 return new_head が行われる。
# それぞれの再帰関数は自分の役割（ポインタ逆転）を果たしてから、
# 新しい先頭 (new_head) を次に返していく。
# もしreturnがなかったら、再帰呼び出しが正しく戻れず、
# リストの再構築ができない。