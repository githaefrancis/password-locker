import unittest  
from user import User

class TestUser(unittest.TestCase):

  '''
  Test class that defines test cases for the user class behaviours.
  
  Args:
      unittest.TestCase:TestCase class that helps in creating test cases.
  '''

  def setUp(self):
    '''
    Set up method to run before each test case
    '''

    self.new_user=User("Francis","Githae","francis.githae@student.moringaschool.com") #create user object

  def tearDown(self):
    '''
    tearDown method cleans up after each test case

    '''
    User.user_list=[]

  def test_init(self):
    '''
    test_init test case to test if the object is initialized correctly
    '''

    self.assertEqual(self.new_user.first_name,"Francis")
    self.assertEqual(self.new_user.last_name,"Githae")
    self.assertEqual(self.new_user.email,"francis.githae@student.moringaschool.com")
    self.assertEqual(self.new_user.credentials_list,[])


  def test_save_user(self):
    '''
    test_save_user test case to test if the user object is saved into the user list
    '''
    
    self.new_user.save_user() #save user to the user list
    self.assertEqual(len(User.user_list),1)

if __name__=='__main__':
  unittest.main()