class Credential:
  """
  Class that generates new instances new instances of credential
  """
  pass

  def __init__(self,platform_name,username,password):
    '''
    __init__ method that defines properties of the credential class

    Args:
        platform_name: Name of the platform the credential belongs to eg facebook, twitter
        username: The login identifier for the account
        password: The login password for the new account
    '''

    self.platform_name=platform_name
    self.username=username
    self.password=password



