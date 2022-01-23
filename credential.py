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
    return 'Account:  ' + str(self.platform_name) +' , username: ' + str(self.username) + ' , password: ' + str(self.password)

  def save_credential(self,user):
    user.credentials_list.append(self)


  def delete_credential(self,user):
    user.credentials_list.remove(self)

  @classmethod
  def display_credentials(cls,user):
    return user.credentials_list


  @classmethod
  def generate_password(cls,length):
    '''
    generate_password method that generates a password for an account

    Args:
        length: Length of the password
    '''
    characters="abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ+-!#$?>"
    selected_character_list=[]

    for i in range(length):
      selected_character_list.append(random.choice(characters))

    return "".join(selected_character_list)

  @classmethod
  def find_credential_by_platform_name(cls,user,platform):
    '''
    find_credential_by_platform_name method to find a credential saved by a user

    Args: 
        user: user from which to search the credential
    Returns:
        The credential that matches the platform name
    '''

    for credential in user.credentials_list:
      if credential.platform_name==platform:
        return credential

    return None