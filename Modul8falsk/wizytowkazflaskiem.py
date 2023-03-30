from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask(__name__)

@app.route('/mypage/me')
def me():
    return render_template("wizytowka2.html")
    
@app.route("/mypage/contact", methods=['GET', 'POST'])
def contact():
    if request.method=='GET':
        items = ["telefon:977553245587709", "email:MS@gm.pl"]
        return render_template("kontakt.html", items=items)
    elif request.method == 'POST':
        text=request.form['comment']
        print(text)
        return redirect("/mypage/contact")


if __name__ == '__main__':
    app.run(debug=True)