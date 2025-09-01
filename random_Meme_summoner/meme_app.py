from flask import Flask, render_template
import requests, json

app = Flask(__name__)
safe_mode = ""

def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url+safe_mode).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit

@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    return render_template("meme_index.html", meme_pic=meme_pic,subreddit=subreddit)

a = input("\n 🎊 Welcome to Meme Summoner! \n\n >> Wanna see wholesome memes(y/n)? ")  
if (a != "n"):
    safe_mode = "/wholesomememes"

app.run(host="0.0.0.0", port=8080, debug=False) 