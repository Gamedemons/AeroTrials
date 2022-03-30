email = 'Anody@gmail.'


def emailCheck():
    if '@' in email and '.' in email:
        length = len(email)
        emailPart1 = email.split('@.')

        print(emailPart1[0])
        print(emailPart1[1])
        print(emailPart1[2])
    #     if len(emailPart1[0]) >= 1 and len(emailPart2[0]) >= 1 and len(emailPart2[1]) >= 1:
    #     #         return True
    #     #     return False
    #     # else:
    #     #     return False


print(emailCheck())
