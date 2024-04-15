import json
import random

# List of first names
first_names = [
    "John", "Jane", "Jim", "Judy", "Joe", "Jason", "Jennifer", "Jessica", "Joanna", "Jerry", "Judy", "Jennifer", "Jessica", "Joanna", "Jerry", "Judy", "Jennifer", "Jessica", "Joanna", "Jerry", "Judy", "Jennifer", "Jessica", "Joanna", "Jerry", "Judy", "Jennifer", "Jessica", "Joanna", "Jerry", "Judy", "Jennifer", "Jessica", "Joanna", "Jerry", "Judy", "Jennifer", "Jessica", "Joanna", "Jerry"
]

# List of last names
last_names = [
    "Doe", "Smith", "Jones", "Brown", "Martin", "Williams", "Johnson", "Jones", "Brown", "Martin", "Williams", "Johnson", "Jones", "Brown", "Martin", "Williams", "Johnson", "Jones", "Brown", "Martin", "Williams", "Johnson", "Jones", "Brown", "Martin", "Williams", "Johnson", "Jones", "Brown", "Martin", "Williams", "Johnson", "Jones", "Brown", "Martin", "Williams", "Johnson", "Jones", "Brown", "Martin", "Williams", "Johnson", "Jones", "Brown"
]


def send_email(user: str, pwd: str, recipient: list, subject: str, body: str):
    import smtplib

    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp-relay.gmail.com", 587)
        server.starttls()
        try:
            server.login(user, pwd)
        except smtplib.SMTPAuthenticationError as AuthErr:
            print("Authentication failed", AuthErr)
            return
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail")


usr = ""
mdp = ""
with open("src/data/mailConfig.json", 'r') as fp:
    mailConfig = json.load(fp)
    usr = mailConfig["mailName"]
    mdp = mailConfig["mailMdp"]
    send_email(usr, mdp, ["contact.rayantremion@gmail.com"],
               "test", "PTDR JE SUIS UN SPAM")
