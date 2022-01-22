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
