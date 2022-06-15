import random
import smtplib

myEmail = "thiccscripts@gmail.com"
myPassword = "waekifadqgldfste"

recipEmail = ""
message= ""

#Scott Larsen SecrentSanta Python project

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(myEmail,myPassword)
print("Logged in")

friends = {"Scott": "slarsen@hotmail.com", "Anton":"Afar@live.com",
           "Nick": "nic@gmail.com", "Ryan": "r.brink@hotmail.com",
           "Richard": "Rwebb@gmail.com", "Brodin": "Brodin@gmail.com", "Noah": "Noahpicc@gmail.com"}
poss_friends = friends.copy()
output = {}

for name in friends:
    choices = list(poss_friends.keys())

    try:
        choices.remove(name)
    except:
        #
        pass
    
    for recip in choices:
        if recip in output:
            if output[recip] == friends[name]:
                choices.remove(recip)

    recip = random.choice(choices)

    recipEmail = friends[recip]
    
    message = name + " is the person you will give a gift too"
    server.sendmail(myEmail, recipEmail, message)
    print("Email has been sent to ", recipEmail)
    
    del poss_friends[recip]





