# def rev(s,n):
#     if n==0:
#         print(s[0])
#     else:
#         print(s[n],end='')
#         rev(s,n-1)
# s=input()
# n=len(s)
# rev(s,n-1)

# class Node:
#     def __init__(self, data):
#        self.data = data
#        self.next = None
 
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.last_node = None
 
#     def append(self, data):
#         if self.last_node is None:
#             self.head = Node(data)
#             self.last_node = self.head
#         else:
#             self.last_node.next = Node(data)
#             self.last_node = self.last_node.next
 
#     def display(self):
#         current = self.head
#         while current is not None:
#             print(current.data, end = ' ')
#             current = current.next
 
# a_llist = LinkedList()
# n = int(input('How many elements would you like to add? '))
# for i in range(n):
#     data = int(input('Enter data item: '))
#     a_llist.append(data)
# print('The linked list: ', end = '')
# a_llist.display()

# def quick_sort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array[1:] if i > pivot]
#         return quick_sort(less) + [pivot] + quick_sort(greater)
# array=[1,6,2,8,3,7,5]
# print(quick_sort(array))


class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
class SSL:
    def __init__(self) -> None:
        self.head=None
    def display(self):
        if self.head is None:
            print('Empty')
        else:
            temp=self.head
            while temp:
                print(temp.data,end='-->')
                temp=temp.next
                
l=SSL()
n=Node(10)
l.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
l.display()