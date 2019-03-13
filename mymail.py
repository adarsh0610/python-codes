import smtplib
import getpass
s=smtplib.SMTP('smtp.gmail.com','587')
s.starttls()
sender='adarsh0610@gmail.com'
reciever='akashkvafs4321@gmail.com'
msg="hiiiiii"
p=getpass.getpass()
s.login(sender,p)
s.sendmail(sender,reciever,msg)
print("msg sent successfully")
s.quit()