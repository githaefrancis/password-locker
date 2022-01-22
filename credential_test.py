import unittest
from credential import Credential
from user import User

class Test_credential(unittest.TestCase):
  """
  Test class test cases for the credential class behaviours
  
  Args:
    unittest.testcase: Testcase class that helps in creating test cases
  """
  def setUp(self):
    '''
    setUp method to run before each test case
    '''
    self.new_credential=Credential("twitter","francisg","1234")
    self.new_user=User("Francis","Githae","francis.githae@student.moringaschool.com","francis","1234") #create user object


  def tearDown(self):
    User.user_list=[]
  def test_save_credential(self):
    '''
    test_save_credential to test if the credential is saved in the credential list
    '''
    self.new_user.save_user()
    self.new_credential.save_credential(self.new_user)   
    self.assertEqual(len(User.user_list[0].credentials_list),1)

  def test_delete_credential(self):
    '''
    test_delete_credential to test deleting a credential
    '''
    self.new_user.save_user()
    self.new_credential.save_credential(self.new_user)
    self.new_credential.delete_credential(self.new_user)   
    self.assertEqual(len(User.user_list[0].credentials_list),0)
if __name__=='__main__':
  unittest.main()