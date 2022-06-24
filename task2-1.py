#user = {
  # 'pin': 1114,
  # 'balance': 100
#}


#def withdraw cash():
   #while True:
     #  try:
    #       amount = int(input("Enter the amount you want to withdraw: "))
   #    except ValueError:
  #         print("Enter valid amount")
 #      else:
#           if amount > user['balance']:
           #    raise ValueError("You don't have enough balance to make this withdrawal")
          #     is_quit = True
         #  else:
           #    user['balance'] = user['balance'] - amount
          #     print(f"£{amount} successful withdraw your remaining balance is £{user['balance']}")
         #      print('')
        #       return "Thank you for using Python ATM"
       #finally:
          # print("Program executed")


#def main():
   #count = 0
   #while count < 3:
       #try:   # pin = int(input('Please enter your pin: '))
       #except ValueError:
        #   print("Please enter correct pin")
       #    count += 1
       #else:
        #   if pin != user['pin']:
       #        print("Pin does not match.. Try Again")
      #         count += 1
     #      else:
    #           withdraw_cash()

   #if count == 3:
      # print('3 UNSUCCESFUL PIN ATTEMPTS, EXITING')
     #  print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
    #   is_quit = True
   #return "Thank you for using Python ATM"


#main()



from atm_unit_test import maketransaction
from unittest import TestCase


#class TestATM_Withdrawal(TestCase):

  # def test_rightPin_rightAmount(self):
     #  expected = 10
    #   result = maketransaction(amount=20, user['pin']=1042)
   #    self.assertEqual(expected, result)

  # def test_rightPin_aboveAmount(self):
      # expected = 'You dont have enough balance to make this withdrawal'
     #  result = maketransaction(amount=1000, user['pin']=1114)
    #   self.assertEqual(expected, result)

   #def test_rightPin_negativeAmount(self):
      # expected = 70
     #  result = maketransaction(amount=-80, user['pin']=1000)
    #   self.assertEqual(expected, result)

   #def test_shortPin_rightAmount(self):
      # expected = 'Please enter your pin:'
     #  result = maketransaction(amount=70, user['pin']=1117)
    #   self.assertEqual(expected, result)

   #def test_wrongPin_rightAmount(self):
       #expected = 'Please enter corret pin'
      # result = maketransaction(amount=70, user['pin']=1114)
     #  self.assertEqual(expected, result)
