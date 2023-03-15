import re
def check_that_num_in_password(password):
    if password.isalnum():
        nums = '1234567890'
        if any(x.isdigit() for x in password) and any(x.isalpha() for x in password) and\
                any(x.isupper() for x in password) and any(x.islower() for x in password):
            return password
        else:
            return "you loser"
    else:
        return "you loser"




def check_that_at_in_email(email):
    # if any(x.isalnum() for x in email) and '@' in email and '.' in email:
    #     return email
    if bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email)):
        return email
    else:
        return "fuck"


print(check_that_at_in_email('421hjhHHbb.gh'))