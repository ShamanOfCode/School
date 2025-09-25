def is_palindrome(i):
    i = str(i)
    if len(i) <= 1:
        return True
    if i[0] != i[-1]:
        return False
    return is_palindrome(i[1:-1])

if __name__ == "__main__":
    user_input = input("Geben Sie einen Text ein: ")
    if is_palindrome(user_input):
        print(f"'{user_input}' ist ein Palindrom.")
    else:
        print(f"'{user_input}' ist kein Palindrom.")
