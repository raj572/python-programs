mydic = {
    "pankha" : "fan",
    "gulab" : "rose",
    "kamal" : "lotus",
    "gend":"ball"
}
print("options are",mydic.keys())
a = input("Enter the hindi word \n")
print("The meaning of your word is ",mydic.get(a))