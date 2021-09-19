import smtplib
from email import message

def email(df, i):
    gmail_user = "savewestgarage@gmail.com"
    gmail_password = "Passcode1!"
    sent_from = "savewestgarage@mit.edu"
    to = ["testgarage@mit.edu"]
    subject = "New Fun Event for You!"
    body = f'''Hi West Garage!\nWe have an event idea suggested by your fellow students.\n\n
        {df.loc[i].Title}\n{df.loc[i].Description}
        \nWho is invited? {df.loc[i].Invite}
        \nThis idea was suggested by a student from {df.loc[i].Dorm}, and currently has {df.loc[i].Votes} upvotes.
        \n\n\n reply all to unsubscribe, hack-color for bc-talk
        '''
    m1 = message.EmailMessage()
    m1.add_header('From',sent_from)
    m1.add_header('To', ", ".join(to))
    m1.add_header('Subject', subject)
    m1.set_content(body)
    # email_text = """\From: %s\n
    #     To: %s\n
    #     Subject: %s\n\n

    #     %s
    #     """ % (sent_from, ", ".join(to), subject, body)
    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, m1.as_string())
        smtp_server.close()
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong….",ex)