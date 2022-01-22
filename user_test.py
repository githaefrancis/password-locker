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

    self.new_user=User("Francis","Githae","francis.githae@student.moringaschool.com",[]) #create user object

  def test_init(self):
    '''
    test_init test case to test if the object is initialized correctly
    '''

    self.assertEqual(self.new_user.first_name,"Francis")
    self.assertEqual(self.new_user.last_name,"Githae")
    self.assertEqual(self.new_user.email,"francis.githae@student.moringaschool.com")
    self.assertEqual(self.new_user.credentials,[])
if __name__=='__main__':
  unittest.main()