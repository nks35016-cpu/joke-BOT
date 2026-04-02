import requests
def jokebot(category):
    respone=requests.get(f"https://v2.jokeapi.dev/joke/{category}",
                         params={"lang":"en",
                                 "type":"single",
                                 "blacklistFlags": "nsfw,racist,sexist"})
    
    data=respone.json()
    if data["error"]!=True:
        print("type these category programming/dark/misc")
    
    return data["joke"]
while True:

    category=input("enter type of category")
    joke=jokebot(category)
    print(joke)
    again=input("do you want more type Y/n")
    if again.lower()!="y":
        print("bye")
        break
