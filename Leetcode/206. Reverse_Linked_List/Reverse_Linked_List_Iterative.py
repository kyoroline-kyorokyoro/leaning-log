# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head

        while curr is not None:
            next_node=curr.next
            curr.next=prev

            prev=curr
            curr=next_node
        return prev
    
# イテレーティブ（非再帰）版
# 現在のノード (curr) を順番にたどりながら、

# 次のノードへのリンクを前のノード (prev) に付け替えていく

# 💡 重要な3つの変数：
# 変数名	意味・役割
# prev	今まで反転してきた部分の「先頭」（逆順でつながっている）
# curr	今見ているノード
# next_node	curr.next を退避しておく変数（つなぎ直すと失われるため）

# | 観点             | 非再帰（反復）          | 再帰                          |
# | -------------- | ---------------- | --------------------------- |
# | ✅ 実行方法         | `while`で順番にたどる   | 関数を自分で呼び出す                  |
# | 🧠 理解のしやすさ     | 「状態」を手で管理する必要がある | スタック（呼び出しの履歴）で自然に処理される      |
# | 🔢 メモリ消費       | **O(1)**（一定）     | **O(n)**（呼び出しごとにスタックを使う）    |
# | 💥 スタックオーバーフロー | 起こらない            | **長いリストで起こる可能性あり**          |
# | ✨ 実用性・安定性      | 安定して高速           | 短く美しいが危険もある                 |
# | 🔍 デバッグのしやすさ   | 明示的なので追いやすい      | 関数の戻り値が繰り返されるので、少し難しい       |
# | 🤔 初心者にとって     | **わかりやすくて安全**    | ロジックはシンプルでも「挙動」がつかみにくいことがある |
