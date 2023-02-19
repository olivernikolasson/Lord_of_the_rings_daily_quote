import random
import smtplib
import requests

TOKEN = "YOUR TOKEN"
headers = {f"Authorization": f"Bearer {TOKEN}"}

response = requests.get(url="https://the-one-api.dev/v2/quote", headers=headers)
data = response.json()["docs"]
picker = random.randint(0, 1000)
character = data[picker]["character"]
quote = data[picker]["dialog"]
movie = data[picker]["movie"]


id = character
char = requests.get(url=f"https://the-one-api.dev/v2/character/{id}", headers=headers)
qt = char.json()["docs"][0]["name"]

movie = movie
trilogy = requests.get(url=f"https://the-one-api.dev/v2/movie/{movie}", headers=headers)
movie_name = trilogy.json()["docs"][0]["name"]

final_string = (f"{quote} ~{qt}\n{movie_name}")



#----------SMTP SETTINGS----------#

my_email = "YOUR EMAIL"
password = "PASSWORD"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password,)

    connection.sendmail(from_addr=my_email,
                       to_addrs="TO ADRESS",
                       msg=f"Subject:Quote Of The Day\n\n{final_string}".encode('utf-8'))