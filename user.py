from collections import UserList


class User:
  """
  Class that generates new instances of users
  """
  pass

  user_list=[] #Empty user list

  def __init__(self,first_name,last_name,email,username,password):
    '''
    __init__ method that defines properties for user objects

    Args:
        first_name: New user first_name
        last_name: New user last_name 
        email:new user email address
    '''

    self.first_name=first_name
    self.last_name=last_name
    self.email=email
    self.username=username
    self.password=password
    self.credentials_list=[]
  
  def save_user(self):
    '''
    save_user method saves user objects into user_list
    '''

    User.user_list.append(self)

  @classmethod
  def user_login(cls,username,password):
    '''
    user_login method authenticates a user
    
    Args:
        username: username to check for
        password: password to check    
    
    Returns:
          user that matches both the username and password
    '''

    for user in cls.user_list:
      if user.username==username and user.password == password:
        return user