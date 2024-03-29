from flask import Flask, render_template, request
import re
from validate_email_address import validate_email

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    test_string = request.form.get("test_string")
    regex_pattern = request.form.get("regex_pattern")
    matches = re.findall(regex_pattern, test_string)
    return render_template("index.html", test_string=test_string, regex_pattern=regex_pattern, matches=matches)


@app.route("/validate_email", methods=["POST"])
def validate_email_address():
    email_address = request.form.get("email_address")
    is_valid = validate_email(email_address)
    return render_template("index.html", email_address=email_address, is_valid=is_valid)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
