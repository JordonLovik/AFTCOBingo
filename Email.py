import smtplib
def sendemail(email, message):
    sendersemail = '*******@gmail.com'
    senderspassword = '*****'
    recipientemail = email
    msg = message

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sendersemail, senderspassword)

    server.sendmail(sendersemail, recipientemail, msg)
    server.quit()