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
        print("What would you like to do? Use these short codes: dc - display credentials, cc - create credential")
        option=input().lower()

        if option=='dc':
          credentials=display_credentials(active_user)
          print(credentials)

        elif option=='cc':
          


if(__name__ == '__main__'):
    main()
