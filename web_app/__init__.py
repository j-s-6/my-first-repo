from flask import Flask, render_template

from app.rps import determine_winner
app = Flask(__name__) #boilerplate line

# WHEN SOMEONE VISITS HOME PAGE IN BROWSER,
# TRIGGER THIS HOME FUNCTION AND RETURN
# OR DISPLAY SOME VALUE

@app.route('/') 
def home():
    #return "THIS IS THE HOME PAGE"
    return render_template("home.html") #pass in the name of a file that exists in the templates directory

@app.route('/about') 
def about():
    return "THIS IS THE ABOUT PAGE"

@app.route('/results', methods=['POST'])
def results():
    # this is the data the user sent in a POST request when they submitted the form
    print(request.form) #Like a dictionary with a key of "user_choice"

    # Get the user's choice from the form data
    user_choice = request.form.get('user_choice')

    computer_choice = "rock"  # generate_random_choice()

    outcome = determine_winner(user_choice, computer_choice)

    return render_template("results.html",
        x=5,
        user_choice=user_choice,
        computer_choice=computer_choice,
        outcome=outcome
    )    

#boilerplate line
if __name__ == '__main__':

    app.run(debug=True)    