def is_valid_email(emails: str) -> None:
    """
    Validate each email in the given list.

    :param email: List of email addresses to check for validity
    :raises ValueError: If an email does not contain the '@' symbol
    """
    if "@" not in email:
        raise ValueError("Error: Email should contain the @ symbol")


# List of emails
emails_list = ["Bahaa@", "Shibel@", "Joseph", "Majed@", "Rabiea", "Ali@"]
for email in emails_list:
    try:
        is_valid_email(email)
        print(f"{email} is a valid email.")
    except ValueError as e:
        print(f"{email} is not a valid email. {e}")