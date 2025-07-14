# 📥 1. Import Flask in app.py
from flask import Flask

# 🧱 2. Initialize Flask App (Create WSGI Application)
app = Flask(__name__)
# 🔍 Explanation:
# •	Flask(__name__) creates an instance of the Flask class.
# •	It acts as the WSGI application (connects app to the web server).

# 🏡 4. Create Your First Route (Homepage)
@app.route("/")
def welcome():
    return "Welcome to this BEST Flask course. I am flask Experience "
# 🔍 Explanation:
# •	@app.route("/") is a decorator that defines the URL path (in this case /, i.e., homepage).
# •	When someone visits the homepage, the function welcome() runs and returns text.

# ➕ 5. Add More Routes (e.g., /index)
@app.route("/index")
def index():
    return "Welcome to the Index Page"
# 🔍 Explanation:
# •	Visiting http://127.0.0.1:5000/index will now show:
# Welcome to the Index Page
# 💡 You can add any number of routes like /contact, /about, etc.


# 🚀 3. Entry Point for Python File
if __name__ == "__main__":
    app.run(debug=True)
# 🔍 Explanation:
# •	if __name__ == "__main__": is the starting point when this file runs.
# •	app.run() starts the development server.




