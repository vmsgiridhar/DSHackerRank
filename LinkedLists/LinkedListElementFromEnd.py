# Foolish with array but worked
def GetNode(head, position):
    count = 1
    arr = []
    temp = head
    if (head.next == None):
        return head.data
    while(head.next != None):
        arr.append(head.data)
        head = head.next
        count = count + 1
    arr.append(head.data)
    return arr[count - position - 1]
