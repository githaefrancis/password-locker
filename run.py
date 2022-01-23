#!/usr/bin/env python3

from credential import Credential
from user import User

active_user = None  # No user logged in by default


def create_user(first_name, last_name, email, username, password):
    '''
    Function to create a new contact
    '''

    new_user = User(first_name, last_name, email, username, password)
    return new_user


def save_user(user):
    '''
    Function to save user
    '''

    user.save_user()


def user_login(username, password):

    return User.user_login(username, password)
    # if(active_user):
    #     print(f"Welcome {active_user.first_name}")
    # else:
    #     print(f"Unable to login, Please provide correct credentials")

def display_credentials(user):
  return Credential.display_credentials(user)

def create_credential(platform_name,username,password):
  '''
  function to create a login credential
  '''
  return Credential(platform_name,username,password)

def save_credential(user):
  '''
  function to save login credential
  '''
  Credential.save_credential(user)

def generate_password(length):
  '''
  function to generate password
  ''' 
  return Credential.generate_password(length)
def find_credential_by_platform_name(user,platform_name):
  '''
  function to search for a credential by platform name
  '''
  return Credential.find_credential_by_platform_name(user,platform_name)

def delete_credential(user):
  '''
  function to delete credential
  '''
  Credential.delete_credential(user)
def main():
    print('Welcome to Passord Locker?  \n')

    print(f"What action would you like to take? ")
    print('\n')

    while True:
        print("Use these short codes: new - create your account, login - login to your account")
        short_code = input().lower()

        if short_code == 'new':
            print("Create Account")
            print("-"*10)
            print("First name ...")
            first_name = input()
            print("Last Name ...")
            last_name = input()

            print("Email ...")
            email = input()

            print("username ...")
            username = input()

            print("Password ...")
            password = input()
            save_user(create_user(first_name, last_name,
                      email, username, password))
            print('\n')
            print(f"Account created, Your username is {username}")

        elif short_code == 'login':
            print("Enter your username")
            username = input()

            print("Enter your password")
            password = input()

            active_user=user_login(username, password)

            if(active_user):
                print(f"Welcome {active_user.first_name}")
                break
            else:
                print(f"Unable to login, Please provide correct credentials")
    print('Out of the loop')
    
    while active_user:
        print("What would you like to do? Use these short codes: dc - display credentials, cc - create credential, rc - remove credential")
        option=input().lower()

        if option=='dc':
          credentials=display_credentials(active_user)
          if(credentials):
            for credential in credentials:
              print(f"{credentials.index(credential) + 1} : {credential.__str__()}")
          else:
            print("No credentials saved")

        elif option=='cc':
          print("Which platform does the account belong eg Facebook")
          platform_name=input()
          print("Enter your username")
          username=input()
          print("Choose 1 to enter your password. Choose 2 to generate a password")
          password_option=input()

          if password_option=="1":
            print("Enter your password")
            password=input()

          elif password_option=="2":
            print("Enter the length of the password you would like: ")
            length=int(input())
            password=generate_password(length)
            print(f"Your password is {password}")
          

          new_credential=create_credential(platform_name,username,password)
          new_credential.save_credential(active_user)
          print(new_credential)

        elif option=="rc":
          print("Which platform would you like to remove? eg Facebook")
          remove_option=input()
          credential_to_remove=find_credential_by_platform_name(active_user,remove_option)
          if(credential_to_remove):
            credential_to_remove.delete_credential(active_user)
            print(f"Credential for {remove_option} deleted!")

          else:
            print("credential not found")

if(__name__ == '__main__'):
    main()
