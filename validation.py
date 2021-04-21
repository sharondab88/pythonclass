def account_number_validation(account_number):
    # check if account # is not empty
    # if account # is 10 digits
    # if account # is an integer
    if account_number:

        try:
            int(account_number)

            if len(str(account_number)) == 10:
                return True

        except ValueError:
            return False
        except TypeError:
            return False

    return False
