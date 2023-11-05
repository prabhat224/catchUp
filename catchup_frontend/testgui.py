# from taipy.gui import Gui, notify


# root_d="""
# <center>
# <|navbar|lov={[("page1","Home"),("page2","Friends"),("page3","Community"),("page4","Profile")]}|>
# </center>

# <|content|>

# """

# page1_md="# hi"
# page2_md="# hii"

# pages = {
#     "/": root_d,
#     "page1": page1_md,
#     "page2": page2_md
# }

# Gui(pages=pages).run()

import taipy.gui.builder as tgb
from taipy.gui import Gui, navigate, notify
import requests
import json
import socket
from taipy.gui import Markdown

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

username=""
password=""
location=""
name=""
friend_username=""
create_name=""
join_code=""



token=0

def login_button(state):
    print("hi")
    
    myobj = {'username': state.username, 'password':state.password}
    print(myobj)
    response = requests.post("http://127.0.0.1:8000/api/login/",json=myobj)
    resp = response.json()
    print(resp)
    if (response.status_code==200):
        print(resp['access_token'])
        notify(state,'success',"logged in")
        navigate(state, to='home')
        
    else:
        print(resp['detail'])
        notify(state,'error',resp['detail'])
    print(state.token)

def signup_button(state):
    print("hi")
    
    myobj = {'name':state.name, 'username': state.username, 'password':state.password, 'location':state.location}
    print(myobj)
    response = requests.post("http://127.0.0.1:8000/api/signup/",json=myobj)
    resp = response.json()
    print(resp)
    if (response.status_code==201):
        print(resp['access_token'])
        notify(state,'success',"Signed up")
        navigate(state, to='home')
        
    else:
        print(resp['detail'])
        notify(state,'error',resp['detail'])
    print(state.token)

def getinfo(state):
    print("hi")
    response = requests.get("http://127.0.0.1:8000/api/get_user_info/",headers={'Content-Type': 'application/json',
'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk5NTgxNTYyLCJpYXQiOjE2OTkxNDk1NjIsImp0aSI6IjAwMDA0Y2QwYjY4YjQ3NWQ4MjViMTBjYTU4NDFlNDlhIiwidXNlcl9pZCI6MX0.avwZNb9ftJAIEx9Fk27nvjRP0rkaOu94hcZsz6GHr_Y'})
    resp = response.json()
    print(resp)
    if (response.status_code==200):
        print(resp)
        
    else:
        
        notify(state,'error',resp['detail'])
    print(state.token)


def update_location(state):
    print("hi")
    response = requests.get("https://httpbin.org/ip")
    data = response.json()
    public_ip = data.get("origin")
    response = requests.get(f"https://api.apilayer.com/ip_to_location/{public_ip}",headers={'apikey':'68ZePdgiXBOb5GF4157pqqbZfEBA67ZO'})
    resp = response.json()
    print(resp)
    if (response.status_code==200):
        print(resp['city'])
        state.location=resp['city']
        notify(state,'success',f"your new location is set to:{state.location}")
        
    else:
        notify(state,'error',"error")
    print(state.token)

def join_group(state):
    print("hi")
    
    myobj = {'unique_code':state.join_code}
    print(myobj)
    response = requests.post("http://127.0.0.1:8000/api/groups/join/",json=myobj,headers={'Content-Type': 'application/json',
'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk5NTgxNTYyLCJpYXQiOjE2OTkxNDk1NjIsImp0aSI6IjAwMDA0Y2QwYjY4YjQ3NWQ4MjViMTBjYTU4NDFlNDlhIiwidXNlcl9pZCI6MX0.avwZNb9ftJAIEx9Fk27nvjRP0rkaOu94hcZsz6GHr_Y'})
    resp = response.json()
    print(resp)
    if (response.status_code==200):
        notify(state,'success',"Joined")
        
    else:
        
        notify(state,'error',resp['detail'])
    print(state.token)

def create_group(state):
    print("hi")
    
    myobj = {'name':state.create_name}
    print(myobj)
    response = requests.post("http://127.0.0.1:8000/api/groups/create/",json=myobj,headers={'Content-Type': 'application/json',
'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk5NTgxNTYyLCJpYXQiOjE2OTkxNDk1NjIsImp0aSI6IjAwMDA0Y2QwYjY4YjQ3NWQ4MjViMTBjYTU4NDFlNDlhIiwidXNlcl9pZCI6MX0.avwZNb9ftJAIEx9Fk27nvjRP0rkaOu94hcZsz6GHr_Y'})
    resp = response.json()
    print(resp)
    if (response.status_code==201):
        
        notify(state,'success',f"created, community code={resp['unique_code']}")
        
        
    else:
        print(resp['detail'])
        notify(state,'error',resp['detail'])
    print(state.token)

def add_friend(state):
    print("hi")
    fname=state.friend_username
    print(fname)
    url=f"http://127.0.0.1:8000/api/add_friend/{fname}/"
    print(url)
    print('hii')
    response = requests.post(url=url,headers={'Content-Type': 'application/json',
'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk5NTgxNTYyLCJpYXQiOjE2OTkxNDk1NjIsImp0aSI6IjAwMDA0Y2QwYjY4YjQ3NWQ4MjViMTBjYTU4NDFlNDlhIiwidXNlcl9pZCI6MX0.avwZNb9ftJAIEx9Fk27nvjRP0rkaOu94hcZsz6GHr_Y'})
    resp = response.json()
    print(resp)
    if (response.status_code==200):
        print("done")
        notify(state,'success',"friend added as a friend")
    else:
        print(resp['detail'])
        notify(state,'error',resp['detail'])
    print(state.token)




root_md="""
<|layout|columns=1fr auto 1fr|class_name=container align_columns_center container-max-width|
<|part|class_name=pt_half pb_half|
<|Catch Up|text|class_name=text-weight700|>
|>
<|part|class_name=align_item_stretch|
|>
<|part|class_name=text_right|
<|toggle|theme|class_name=relative nolabel|>
|>
|>
<|menu|label=Menu|lov={[('Login', 'Login'), ('Signup', 'Signup'),('Home', 'Home'),('Profile', 'Profile'),('chat', 'Chat')]}|on_action=on_menu|>
"""

page1_md="""<|card card-bg|

#Please Login

<|{username}|input|label=Username|hover_text="Username"|class_name=m2 align-item-center|>
<|{password}|input|label=Password|hover_text="Password"|password=True|class_name=m2|>
<|Submit|button|on_action=login_button|>
|>

"""


page2_md="""
<|card card-bg|

#Please Register

<|{name}|input|label=Name|hover_text="Name"|class_name=m2 align-item-center|>
<|{username}|input|label=Username|hover_text="Username"|class_name=m2 align-item-center|>
<|{password}|input|label=Password|hover_text="Password"|password=True|class_name=m2|>
<|{location}|input|label=Location|hover_text="Current Location"|class_name=m2|>
<|Submit|button|on_action=signup_button|>
|>
"""

home_md=Markdown("""


<|Welcome, Rishabh|text|class_name=h1 text-center m4|>

<|card card-bg|

<|Friends in your area:|text|class_name=h2 m1 text-left|>
<|Communities in your area:|text|class_name=h2 m1 text-left|>

<|Your Scheduled Meetups|class_name=bg-primary|expandable|expanded=False|
    <|card card-bg m1|
    hello
    |>
    <|card card-bg m1|
    hello
    |>
    <|card card-bg m1|
    hello
    |>
|>
|>

<|card card-bg m3|

<|Your Friends In this area|text|class_name=h1 text-center m4|>

<|layout|columns=1 1 1 1 1|columns[mobile]="1"|

<|card card-bg bg-secondary|
<|layout|columns=1 1|
<img src="img2.png" alt="Prabhat" width="100"/>
<|card card-bg|
<|Prabhat|text|class_name=text-left|>
<|{location}|text|class_name=color-primary text-right|>
|>
|>
|>

<|card card-bg bg-secondary|
<|layout|columns=1 1|
<img src="img2.png" alt="Prabhat" width="100"/>
<|card card-bg|
<|Prabhat|text|class_name=text-left|>
<|{location}|text|class_name=color-primary text-right|>
|>
|>
|>
                 
<|card card-bg bg-secondary|
<|layout|columns=1 1|
<img src="img2.png" alt="Prabhat" width="100"/>
<|card card-bg|
<|Prabhat|text|class_name=text-left|>
<|{location}|text|class_name=color-primary text-right|>
|>
|>
|>
|>


                 
|>


<|card card-bg m3|

<|Your Communities In this area|text|class_name=h1 text-center m4|>

<|layout|columns=1 1 1 1|columns[mobile]="1"|

<|card card-bg bg-secondary|
<|layout|columns=1 1|
<|Hack CBS Community|text|class_name=text-left|>
<|Location|text|class_name=color-primary text-right|>
|>
|>

<|card card-bg bg-secondary|
<|layout|columns=1 1|
<|Hack CBS Community|text|class_name=text-left|>
<|Location|text|class_name=color-primary text-right|>
|>
|>

<|card card-bg bg-secondary|
<|layout|columns=1 1|
<|Hack CBS Community|text|class_name=text-left|>
<|Location|text|class_name=color-primary text-right|>
|>
|>

<|card card-bg bg-secondary|
<|layout|columns=1 1|
<|Hack CBS Community|text|class_name=text-left|>
<|Location|text|class_name=color-primary text-right|>
|>
|>
|>

|>
""")

profile_md="""

<|card card-bg|
<|layout|columns=1 1 1|gap=10|class_name=container align_columns_center container-max-width|
<|part|class_name=pt_half pb_half|
<|Prabhat|text|class_name=taipy-text text-weight500|>
|>
<|part|class_name=align_item_stretch|
|>
<|part|class_name=text_right|
<|{location}|text|class_name=text-weight500|>
|>
|>
|>

<|Update Location|button|on_action=update_location|class_name=container m-10 align_columns_center|>

<|layout|columns=1 1|gap=25px|class_name=container m4 align_columns_center|
<|part|class_name=pt_half pb_half|

<|Your All friends|text|class_name=h3 text-center|>

<|layout|columns=1 1 1|columns[mobile]=1|
<|card card-bg|
<|Rishabh|text|>
<|Gurugram|text|>
|>
<|card card-bg|
<|Rishabh|text|>
<|Gurugram|text|>
|>
<|card card-bg|
<|Rishabh|text|>
<|Gurugram|text|>
|>
<|card card-bg|
<|Rishabh|text|>
<|Gurugram|text|>
|>
<|card card-bg|
<|Rishabh|text|>
<|Gurugram|text|>
|>
<|card card-bg|
<|Rishabh|text|>
<|Gurugram|text|>
|>
|>

|>
<|part|class_name=pt_half pb_half|

<|Your All Communities|text|class_name=h3 text-center|>

<|layout|columns=1 1 1|
<|card card-bg|
<|HackCBS|text|>
<|Delhi|text|>
|>
<|card card-bg|
<|HackCBS|text|>
<|Delhi|text|>
|>
<|card card-bg|
<|HackCBS|text|>
<|Delhi|text|>
|>
<|card card-bg|
<|HackCBS|text|>
<|Delhi|text|>
|>
<|card card-bg|
<|HackCBS|text|>
<|Delhi|text|>
|>
<|card card-bg|
<|HackCBS|text|>
<|Delhi|text|>
|>
<|card card-bg|
<|HackCBS|text|>
<|Delhi|text|>
|>
|>

|>
|>

<|card card-bg m2|

#Add your friend username

<|{friend_username}|input|label=Username|hover_text="Friend Username"|class_name=m2 align-item-center|>

<|Submit|button|on_action=add_friend|>
|>

<|layout|columns=1 1|gap=4px|

<|card card-bg|

#Join a Group

<|{join_code}|input|label=Username|hover_text="Friend Username"|class_name=m2 align-item-center|>

<|Submit|button|on_action=join_group|>
|>

<|card card-bg|

#Create a Group

<|{create_name}|input|label=Username|hover_text="Friend Username"|class_name=m2 align-item-center|>

<|Submit|button|on_action=create_group|>
|>

|>


"""



chat_md=Markdown("""

<|layout|columns=1 1|gap=25px|class_name=align_columns_center container-max-width|

<|card card-bg bg-primary align_columns_center|
#Friends
<|card card-bg m1|
<|Friend Name|text|class_name=text-center|> <|Last Seen 2days ago|text|class_name=m4 mr-8 color-primary|>     <|Chat|button|on_action=go_home|>                  
|>
<|card card-bg m1|
<|Friend Name|text|class_name=text-center|> <|Last Seen 2days ago|text|class_name=m4 mr-8 color-primary|>   <|Chat|button|on_action=go_home|>                    
|>
<|card card-bg m1|
<|Friend Name|text|class_name=text-center|> <|Last Seen 2days ago|text|class_name=m4 mr-8 color-primary|>        <|Chat|button|on_action=go_home|>       
|>
<|card card-bg m1|
<|Friend Name|text|class_name=text-center|> <|Last Seen 2days ago|text|class_name=m4 mr-8 color-primary|>   <|Chat|button|on_action=go_home|> 
|>
<|card card-bg m1|
<|Friend Name|text|class_name=text-center|> <|Last Seen 2days ago|text|class_name   =m4 mr-8 color-primary|>   <|Chat|button|on_action=go_home|>     
|>
|>
                 
<|card card-bg bg-primary align_columns_center|
#Communities
<|card card-bg m1|
<|Community Name|text|class_name=text-center|> <|12 Members |text|class_name=m4 color-primary|>                      
|>
<|card card-bg m1|
<|Community Name|text|class_name=text-center|> <|12 Members |text|class_name=m4 color-primary|>                      
|>
<|card card-bg m1|
<|Community Name|text|class_name=text-center|> <|12 Members |text|class_name=m4 color-primary|>                      
|>
<|card card-bg m1|
<|Community Name|text|class_name=text-center|> <|12 Members |text|class_name=m4 color-primary|>                      
|>
<|card card-bg m1|
<|Community Name|text|class_name=text-center|> <|12 Members |text|class_name=m4 color-primary|>                      
|>
|>
                 
|>

""")

communicate_md=Markdown("""
<|card card-bg m2 p2|
<|card card-bg m2 p2 bg-primary|
<|layout|columns=1 1 1|
<img src="img2.png" alt="Prabhat" width="100"/>
##Prabhat
<|{location}|text|>
|>
|>
                        
<|card card-bg bg-primary m2|

|>
|>

""")



def on_menu(state, action, info):
    page = info["args"][0]
    navigate(state, to=page)

def go_home(state):
    navigate(state, to='communicate')

pages = {
    "/": root_md,
    "Login": page1_md,
    "Signup": page2_md,
    "Home":home_md,
    "Profile":profile_md,
    "chat":chat_md,
    "communicate":communicate_md
}


Gui(pages=pages).run()
