#!/usr/bin/env python3

from user import User

def create_user(first_name,last_name,email,username,password):
  '''
  Function to create a new contact
  '''

  new_user=User(first_name,last_name,email,username,password)
  return new_user

def save_user(user):
  '''
  Function to save user
  '''

  user.save_user()


def main():
  print('Welcome to Passord Locker?  \n')

  print(f"What action would you like to take? ")
  print('\n')

  while True:
    print("Use these short codes: new - create your account, login - login to your account")
    short_code=input().lower()

    if short_code=='new':
      print("Create Account")
      print("-"*10)
      print("First name ...")
      first_name=input()
      print("Last Name ...")
      last_name=input()

      print("Email ...")
      email=input()

      print("username ...")
      username=input()

      print("Password ...")
      password=input()
      save_user(create_user(first_name,last_name,email,username,password))
      print('\n')
      print(f"Account created, Your username is {username}")
if(__name__=='__main__'):
  main()