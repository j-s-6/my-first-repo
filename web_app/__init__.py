from flask import Flask

app = Flask(__name__) #boilerplate line

# WHEN SOMEONE VISITS HOME PAGE IN BROWSER,
# TRIGGER THIS HOME FUNCTION AND RETURN
# OR DISPLAY SOME VALUE

@app.route('/') 
def home():
    return "THIS IS THE HOME PAGE"



if __name__ == '__main__':

    app.run(debug=True)