# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2

        if list1.val <list2.val:
            list1.next=self.mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next=self.mergeTwoLists(list1,list2.next)
            return list2
        
# 再帰（リカージョン）での解法
# 考え方：
# 先頭の小さい方を選び、その next に残りのリストを再帰的にマージした結果をつなぐ。
# リストが空になったときが終了条件。
# 重要ポイント：
# 再帰なので、後ろ（最後尾）から積み上がっていくように見える。
# 関数が自分自身を呼び出す。
# スタックを使うため、リストが長すぎるとスタックオーバーフローのリスクがある。