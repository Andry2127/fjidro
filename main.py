from  flask import Flask, render_template, request
from  flask_wtf import FlaskForm
import wtforms



app = Flask(__name__)
app.secret_key = "132"




class PostForm(FlaskForm):
    ceo = wtforms.StringField("type ceo")
    text = wtforms.TextAreaField("type text")
    price = wtforms.IntegerField("type price")
    submit = wtforms.SubmitField("sub")


@app.route("/add_club_wtf/", methods = ["GET", "POST"])
def add_club_wtf():
    form = PostForm()
    if request.method == "POST":
        ceo = form.ceo.data
        text = form.text.data
        price = form.price.data
        return f"{ceo = }; {text = }; {price = }"
    return render_template("add_club_wtf.html", form=form)


@app.route("/add_club/", methods=["GET", "POST"])
def add_club():
    if request.method == "POST":
        ceo = request.form.get("ceo")
        text = request.form.get("text")
        print(f"{ceo = }")
        print(f"{text = }")
        return f"{ceo = }; {text = }"
    return render_template("add_club.html")


if __name__ == "__main__":
    app.run(debug=True)