# def zip_lists(a, b):
#     current1 = a.head
#     current2 = b.head
#     while current1:
#         temp1 = current1
#         current1.next = current2
#         while current2:
#             current2.next = temp1.next
#         current2 = current2.next
#     current1 = current1.next
#
#     return current1

# def zip_lists(a, b):
#     current1 = a.head
#     current2 = b.head
#     temp1 = current1.next
#     temp2 = current2.next
#     while current1 and current2:
#         current1.next = current2
#         current2.next = temp1
#         current1.next = temp2
#
#         current1 = current1.next
#         current2 = current2.next
#
#     return current1

def zip_lists(ll1, ll2):
    if ll1.head is None and ll2.head is None:
        return 'No linked list available'
    elif ll1.head is None or ll2.head is None:
        return ll1 or ll2

    current1 = ll1.head
    current2 = ll2.head

    while current1 or current2:
        temp1 = current1.next
        temp2 = current2.next
        current1.next = current2
        current2.next = temp1
        current1 = temp1
        current2 = temp2

    return ll1
