import smtplib  
  
fromaddr = 'calsectionswitcher@gmail.com'  
toaddrs  = 'gameboybf2142@gmail.com'
subject = 'Test Message' 
text = "This is a test message" 

msg = """\
From: %s
To: %s
Subject: %s

%s
""" % (fromaddr, toaddrs, subject, text)
  
# Credentials (if needed)  
username = 'calsectionswitcher'  
password = 'byebye123'  
  
# The actual mail send  
server = smtplib.SMTP('smtp.gmail.com:587')  
server.starttls()  
server.login(username,password)  
server.sendmail(fromaddr, toaddrs, msg)  
server.quit()  

