import random
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

  def __str__(self):
    return 'platform_name:  ' + str(self.platform_name) +' username: ' + str(self.username) + ' password: ' + str(self.password)

  def save_credential(self,user):
    user.credentials_list.append(self)


  def delete_credential(self,user):
    user.credentials_list.remove(self)

  @classmethod
  def display_credentials(cls,user):
    return user.credentials_list


  @classmethod
  def generate_password(cls):
    '''
    generate_password method that generates a password for an account
    '''
    characters="abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ+-!#$?>"
    selected_character_list=[]

    for i in range(8):
      selected_character_list.append(random.choice(characters))

    return "".join(selected_character_list)
