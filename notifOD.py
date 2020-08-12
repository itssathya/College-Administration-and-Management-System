import smtplib
import random

def ODApproveSMTP(dat):
    gmail_user = 'noreply.camsproject@gmail.com'  
    gmail_password = 'cams2019'

    sent_from = 'noreply.camsproject@gmail.com'  
    to = ['nsathya33@gmail.com']  
    subject = 'On Duty - Rajalakshmi Engineering College'  
    body = """Dear Student,
    Your on duty has been approved. Please take a print out of this e-mail for reference purposes.

    ON-DUTY DETAILS
    Name: %s
    Department: %s
    Section: %s
    Roll No: %s
    Date: %s
    Event Name: %s
    Event Institution: %s
    Reason: %s

    Status : OD APPROVED (by HoD)


    If any errors in the details, please contact your respective HoD.""" % (dat[0],dat[1],dat[2],dat[3],dat[6],dat[4],dat[5],dat[8])

    email_text = """\
    From: %s  
    To: %s  
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)


    try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print ('Email sent!')
    except:  
        print ('Something went wrong...')
