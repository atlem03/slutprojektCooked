from flask import Flask, render_template, request

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template('homeTemplate.html')
# Draw Page
@app.route("/draw")
def quiz():
    return render_template('drawTemplate.html')

# Start Webapp
if __name__ == "__main__":
    app.run(debug=True)