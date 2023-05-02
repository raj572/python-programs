name = ['Avinash','anish','raj','vinus','suraj','harsh','sandip','sunil']
for i in name:
    val=input('enter name: ')
    name.append(val)
    break
print(name)

check = input("Enter a name to check it is wheather avalaible in a list or not : ")
if check in name :
    print("Your name is present in the list.")
else:
    print("Your name is not present in the list.")    