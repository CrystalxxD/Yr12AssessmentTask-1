def validate_username(username):
    # Condition 1: At most 10 characters
    if len(username) > 10:
        return False, "Username is too long."

    # Condition 2: Only Letters or Numbers characters
    if not username.isalnum():
        return False, "Username must contain only letters and numbers."

    # Condition 3: Cannot contain < or >
    if "<" in username or ">" in username:
        return False, "Username cannot contain '<' or '>' characters."

    return True, "Username is valid."

# Sample test usernames
test_usernames = [
    "JohnDoe",                  # valid
    "ThisUsernameisTooLong",    # too long
    "User<Name",                # contains <
    "User99",                   # valid
    "not_al...",                # not alphanumeric
    "Test>",                    # contains >
    "1234"                      # valid
]

for user in test_usernames:
    result, message = validate_username(user)
    print(f"Testing '{user}': {message}")
