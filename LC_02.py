# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Edge case 1: 둘 다 None일 경우
        if not l1 and not l2:
            return ListNode(0)  # 혹은 return None, 문제 정책에 맞게 선택

        # Edge case 2: 한쪽이 None일 경우 → 그냥 다른 쪽을 반환
        if not l1: return l2
        if not l2: return l1
        
        dummy = ListNode()                 # (1) 결과 연결리스트의 가짜(head) 시작점. 진짜 결과는 dummy.next부터 시작할 거야.
        cur = dummy                        # (2) 지금까지 만든 결과 리스트의 "꼬리"를 가리키는 포인터. 새 노드를 이어붙일 때 사용.
        carry = 0                          # (3) 자리올림값(0 또는 1). 초깃값은 0.

        while l1 or l2 or carry:           # (4) l1 또는 l2가 남아있거나, 마지막에 carry가 1로 남아있을 때까지 반복.
            x = l1.val if l1 else 0        # (5) l1이 있으면 그 자리수, 없으면 0 (길이가 다른 경우 대비).
            y = l2.val if l2 else 0        # (6) l2도 동일하게 처리.

            s = x + y + carry              # (7) 같은 자리수끼리 더하고 이전 자리에서 넘어온 carry까지 합산.
            carry = s // 10                # (8) 합이 10 이상이면 다음 자리로 넘어갈 올림(1), 아니면 0.
            cur.next = ListNode(s % 10)    # (9) 현재 자리수에 기록될 값(0~9)으로 새 노드를 만들어 결과 리스트 뒤에 붙임.
            cur = cur.next                 # (10) 꼬리 포인터(cur)를 방금 만든 새 노드로 이동.

            if l1: l1 = l1.next            # (11) l1 포인터 한 칸 전진(없으면 건너뜀).
            if l2: l2 = l2.next            # (12) l2 포인터 한 칸 전진(없으면 건너뜀).

        return dummy.next                  # (13) dummy는 가짜 헤드이므로, 실제 결과의 시작인 dummy.next를 반환.

# Helper functions
# 1) build_list: 배열을 연결리스트로 변환
def build_list(arr):
    dummy = ListNode()                     # (1) 결과 연결리스트의 가짜(head) 시작점. 진짜 결과는 dummy.next부터 시작할 거야.
    cur = dummy                            # (2) 지금까지 만든 결과 리스트의 "꼬리"를 가리키는 포인터. 새 노드를 이어붙일 때 사용.
    for x in arr:
        cur.next = ListNode(x)             # (3) 현재 자리수에 기록될 값(0~9)으로 새 노드를 만들어 결과 리스트 뒤에 붙임.
        cur = cur.next                     # (4) 꼬리 포인터(cur)를 방금 만든 새 노드로 이동.
    return dummy.next                      # (5) dummy는 가짜 헤드이므로, 실제 결과의 시작인 dummy.next를 반환.

# 2) to_array: 연결리스트를 배열로 변환
def to_array(node):
    out = []
    while node:                            # (1) 노드가 끝날 때까지 반복
        out.append(node.val)               # (2) 노드의 값을 배열에 추가
        node = node.next                   # (3) 노드를 다음 노드로 이동
    return out

# Test
l1 = build_list([2,4,3])
l2 = build_list([5,6,4])
res = Solution().addTwoNumbers(l1, l2)
print(to_array(res))
