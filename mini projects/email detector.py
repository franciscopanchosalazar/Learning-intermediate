# This code check if the user email is a big company email or a custom one
user_name = input('Enter your name: ')
user_email = input('Enter your email: ')
print('\n')
split_email = user_email.split('@')
email_company = split_email[-1].split('.')


if email_company[0].lower() == 'gmail':
    print("Hello %s, I can see you are registered with a Google account" % user_name)

elif email_company[0].lower() == 'hotmail':
    print("Hello %s, I can see you are registered with a Hotmail account" % user_name)

elif email_company[0].lower() == 'yahoo':
    print("Hello %s, I can see you are registered with a Yahoo account" % user_name)

else:
    print("Hello %s, I can see you are registered with a custom account" % user_name)
