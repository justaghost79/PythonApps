class Node:
    def has_cycle(head):
        def __init__(self, value, next=None):
            self.value = value
            self.next = next 
        slow, fast = head, head

        while fast is not None and fast.next is not None:
        
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
    head = Node(1)
    head.next = Node(2)
    head.next.next= Node(3)
    head.next.next.next = Node(4)
    has_cycle(head)
