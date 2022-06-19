def log_in():
    user_name=input("your user name")
    password=int(input("your password"))
    if (password==d[user_name]):
        print("access granted")
    else:
        print("access denied")

d= {"jack":389, "jax":567, "ashe":897, "zed":2121}


have_account=input("do you have an account?")
if have_account=="yes":
    log_in()
if have_account=="no":
    username=input("enter your username")
    password1=int(input("enter your password"))
    password2=int(input("pls enter your password again"))
    if not(password1==password2):
        print("the passwords do not match, try again")
    if (password1==password2):
        d[username]= password1
        print("you have created an account")
    log_in()

    
        
    







