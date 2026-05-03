# 1. A hospital system stores patient names in random case for example
# rahUl DahaL. Write a program to display the name in proper title format
# on the prescription.

patient_names=input("Enter patient name : ")
print(patient_names.title())


# 2. A cybersecurity system requires all passwords to be checked in
# lowercase for consistency. Take a password input like ‘Pass@123’ and
# convert it for comparison

password=input("Enter password : ")
print(f'Is the password in lowercase : {password.islower()}')
print(password.lower())

# 3. A movie ticket booking system receives the movie name in lowercase
# ‘spider-man no way home’. Display it in title case on the ticket.

Movie_Ticket=input("Enter movie name : ")
print(Movie_Ticket.title())


# 4. A school notice board program takes a heading input and displays it in
# ALL CAPS for attention. Take input ‘annual sports day’ and display it.

heading=input("Enter heading : ")
print(heading.upper())

# 5. A fun CAPS-LOCK reversal tool takes the sentence ‘hELLO wORLD’ and
# swaps every letter's case. Write a program for this.

sentence="hELLO wORLD"
print(sentence.swapcase())


# 6. A document editor wants to find the first position where the word ‘error’
# appears in a log message: ‘System error detected, error code 404’.

log_message="System error detected, error code 404"
position=log_message.find("error",0,len(log_message))
print(position)

# 7. An email validation system checks whether an entered email ends with
# ‘@gmail.com’. Write a program to validate it.

email=input("Enter email : ")
check=email.endswith('@gmail.com')
print(check)

# 8. A spam filter counts how many times the word ‘free’ appears in a
# message: ‘Get free stuff, free gifts and free coupons now!’.

message="Get free stuff, free gifts and free coupons now!"
print(f'The word "free" appears {message.count("free")} in the message')

# 9. A URL checker verifies whether a website link starts with "https" for
# security. Write a program for this.

url=input("Enter url : ")
check=url.startswith("https")
print(check)


# 10. A resume scanner checks whether the keyword ‘Python’ is present in
# a resume text. Use the in operator

resume_text=input("Enter resume text : ")
print(f'The word "Python" is present in the resume text : {"Python" in resume_text}')

# 11. A bank transaction log uses index() to find the exact position of the
# word ‘FAILED’ in the message ‘Transaction FAILED due to low balance’

message="Transaction FAILED due to low balance"
check=message.index("FAILED")
print(check)