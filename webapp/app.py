import os

from flask import Flask  # flask library
from flask import render_template # Templates render libray

app = Flask(__name__)

@app.route("/",methods=['GET']) # Index path
def index(): # Index function
    try: # Try the next code
        return render_template('index.html') # index.html render
    except Exception as error: # Cathc error
        print("Error index(): ", error) # Print error message
        return render_template('index.html') # index.html render

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080))) # Config the run function
