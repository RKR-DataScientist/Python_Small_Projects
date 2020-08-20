import smtplib as smt


obj = smt.SMTP("smtp.gmail.com", 587)
obj.starttls()

obj.login("ravikrrahul0@gmail.com", "KHA HO007")

subject = " Sending mail using python"
body = " This is tutorial of sending email using python script in simple start"

message = "Subject : {}\n\n{}".format(subject,body)
#print(message)

listOfAddress = ["weblinkravirahul0@gmail.com","ashutoshdevraj@gmail.com"]
print(" Email Send Successfully")
obj.sendmail("ravikrrahul0@gmail.com", listOfAddress,message)

obj.quit()