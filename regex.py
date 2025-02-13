import re
#basic search
text = "python is fun"
match = re.search("python", text)
if match:
    print("found: ",match.group())

#extracting emails
text = "my email is:Zobia.shakil1@gmail.com"
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}", text)
print(emails)

#checking if it contains small letter
text = "ZOBIa"
match = re.search("[a-z]", text)
if match:
    print("found: ",match.group())

#checking if it contains capital letter and digit 
text = "Zobia34@#"
match = re.search('[A-Z]',text)
match_digit = re.search('[0-9]',text)
match_special = re.search('[!@#$%^&*]',text)
if match:
    print("found" ,match.group())
if match_digit:
    print('found',match_digit.group())
#checking if it contains special character
if match_special:
    print('found',match_special.group())

#validating phone number
text = 'my phone number is 0333-1234567'
match_phone = re.search(r"\d{4}-\d{7}",text)
if match_phone:
    print("found phone number: ",match_phone.group())

#extracting url and date
text = "website is: https://www.linkedin.com published on 2020-12-12"
match_website = re.search(r"https?://[^\s]+",text)
match_date = re.search(r"\d{4}-\d{2}-\d{2}",text)
if match_website:
    print("found website url:" ,match_website.group())
if match_date:
    print("found date: ",match_date.group())



    