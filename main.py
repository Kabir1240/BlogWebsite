import requests
from flask import Flask, render_template


app = Flask(__name__)
blogs = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
blogs.raise_for_status()


@app.route('/')
def home():
    return render_template("index.html", all_blogs=blogs.json())


@app.route('/post/<int:num>')
def post(num:int):
    blog = blogs.json()[num-1]
    print(blog)
    return render_template("post.html", blog=blog)


@app.route('/guess/<name>')
def guess(name: str):
    response_gender = requests.get(f"https://api.genderize.io?name={name}")
    response_gender.raise_for_status()
    gender = response_gender.json()['gender']
    
    response_age = requests.get(f"https://api.agify.io?name={name}")
    response_age.raise_for_status()
    age = response_age.json()['age']
    
    return render_template("guess.html", gender=gender, age=age, name=name.capitalize())
    

if __name__ == "__main__":
    app.run(debug=True)
