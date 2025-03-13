from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Corrected path

@app.route("/docs")
def docs():
    return render_template("docs.html")  # Corrected path

if __name__ == "__main__":
    app.run(port=5000, debug=True)  # Enable debug mode for better error messages