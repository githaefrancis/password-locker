class User:
  """
  Class that generates new instances of users
  """
  pass



  def __init__(self,first_name,last_name,email,credentials):
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
    self.credentials=credentials
  
  user_list=[]