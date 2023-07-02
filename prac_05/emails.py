"""
Emails
Estimate: 40 minutes
Actual:   40 minutes
"""
email_details = {}
while True:
    email = input("Email: ")
    if email == "":
        break

    username = email.split('@')[0]
    split_name = username.split('.')
    name = ' '.join(split_name).title()
    response = input(f"Is your name {name}? (Y/N) ").lower()
    if response == "" or response == "y":
        email_details[email] = name
    else:
        name = input("Name: ").title()
        email_details[email] = name

print("\nEmail dictionary:")
for email, name in email_details.items():
    print(f"{name} ({email})")
