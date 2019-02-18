from flask import Flask, render_template, request,redirect
import lab3_3
import twitter2

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("domain")
    if not name:
        return render_template("failure.html")
    print(name)
    twitter2.create_json_file(name)
    lab3_3.main()
    return render_template("map.html")

if __name__ == "__main__":
    app.run()