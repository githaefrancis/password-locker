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

  def test_display_credentials(self):
    '''
    test_display_credentials to test displaying all credentials saved under a user

    '''
    self.new_user.save_user()
    self.new_credential.save_credential(self.new_user)
    self.assertEqual(Credential.display_credentials(self.new_user),self.new_user.credentials_list)

  def test_generate_password(self):
    '''
    test_generate_password to test if a password is autogenerated
    '''
    new_password=Credential.generate_password()
    self.assertEqual(len(new_password),8)

  def test_find_credential_by_platform_name(self):
    '''
    test_find_credential_by_account_name to test if a credential is seached by account name
    '''
    self.new_user.save_user()
    self.new_credential.save_credential(self.new_user)
    found_credential=Credential.find_credential_by_platform_name(self.new_user,"twitter")
    self.assertEqual(found_credential.platform_name,"twitter")
if __name__=='__main__':
  unittest.main()