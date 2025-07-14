# 📥 1. Import Flask in app.py
from flask import Flask,render_template, request

# 🧱 2. Initialize Flask App (Create WSGI Application)
app = Flask(__name__)
# 🔍 Explanation:
# •	Flask(__name__) creates an instance of the Flask class.
# •	It acts as the WSGI application (connects app to the web server).

# 🏡 4. Create Your First Route (Homepage)
@app.route("/")
def welcome():
    return "<html><H1>Welcome to Flask COurse</H1></html>"
# 🔍 Explanation:
# •	@app.route("/") is a decorator that defines the URL path (in this case /, i.e., homepage).
# •	When someone visits the homepage, the function welcome() runs and returns text.

# ➕ 5. Add More Routes (e.g., /index)
@app.route("/index",methods={"GET"})
def index():
    return render_template("index.html")
# 🔍 Explanation:
# •	Visiting http://127.0.0.1:5000/index will now show:
# Welcome to the Index Page
# 💡 You can add any number of routes like /contact, /about, etc.

# ➕ 6. Add More Routes (e.g., /about)
@app.route("/about")
def about():
    return render_template("about.html")

#📝 7. Route to handle form submission and display
@app.route('/submit', methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        name = request.form['name']
        return f"Hello {name}"
    # if is not a POST method
    return render_template('form.html')
# ✅ Explanation:
# •	When it's a GET request → Show the form (form.html)
# •	When it's a POST request → Get the name from the form and return a greeting
# 🎯8. Route to display success message with score passed in the URL
@app.route('/success/<int:score>')
def success(score):
       res=""
       if score >= 50:
           res = "Pass"
       else:
           res = "Fail"
       return render_template("result.html", results=res)
# ### Jinja2 Template Engine
# ```
# {{ }} expressions to print output in html
# {%...%} conditions, for loops
# {#...#} this is for comments

# 📦9 Send Dictionary to HTML with Loop — result1.html
@app.route('/success_result/<int:score>')
def success_result(score):
    if score >= 50:
        result = "Pass"
    else:
        result = "Fail"
    
    data = {"Score": score, "Result": result}
    return render_template("result1.html", results=data)
# 💡 Explanation:
# •	Dictionary data contains key-value pairs like Score and Result.
# •	Sent to the result1.html file for display.




# 🚀 3. Entry Point for Python File
if __name__ == "__main__":
    app.run(debug=True)
# 🔍 Explanation:
# •	if __name__ == "__main__": is the starting point when this file runs.
# •	app.run() starts the development server.