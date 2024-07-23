from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template("index.html")


@app.route('/Gallery')
def gallery():
    return render_template("html/Galerie.html")


@app.route('/Orar')
def orar():
    return render_template("html/Orar.html")


@app.route('/Contacts')
def contact():
    return render_template("html/Contacte.html")


@app.route('/Admit')
def admitere():
    return render_template("html/Admitere.html")


@app.route('/Financial')
def financial():
    return render_template("html/TransparentaFinanciara.html")


@app.route('/News')
def noutati():
    return render_template("html/Noutati.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
