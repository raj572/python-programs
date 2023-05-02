text = input("Enter text : ")
if ("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("subscribe now this channel" in text):
    spam = True
elif("hurry up! you have won a lottery!" in text):
    spam = True
elif("join online digital marketing" in text):
    spam = True
elif("join now coding ninja" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")        
