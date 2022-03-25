import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()
# insert the corresponding information in the place of curly parantheses
conn.login('{email address}', '{device-password}')
conn.sendmail('{source address}', '{destination-address}', 'Subject: Test for Python Mail Sending\n\nJust testing...\n\n-Alper')
conn.quit()
