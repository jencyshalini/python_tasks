def check_pin(entered_pin):
  if entered_pin==1022:
    return True
  else: 
    return False

def bank_action(action_type,entered_pin):
  result=check_pin(entered_pin)
  if result==True:
    if action_type=="balance":
      print("Your Balanace :220400.05")
    else:
      print("Withdrawal Successful")
  else:
    print("Access Denied")

bank_action("balance",1024)
bank_action("balance",1022)
bank_action("withdraw",1022)

# ouput
Access Denied
Your Balanace :220400.05
Withdrawal Successful
