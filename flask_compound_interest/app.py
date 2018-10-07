from flask import Flask, render_template, request

# Create a Flask app
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form():
    result = None
    if request.method == 'POST':
        principal = request.form['principal']
        interest = request.form['interest']
        numYears = request.form['years']
        timesPerYear = request.form['times_per_year']

        if principal != '' and interest != '' and numYears != '' and timesPerYear != '':
            principal = int(principal)
            interest = float(interest)
            numYears = int(numYears)
            timesPerYear = int(timesPerYear)
            result = calcCompoundInterest(principal, interest, numYears, timesPerYear)

        if result is None:
            result = "Error, need all parameters"
            

    # Pass the result to the front end
    return render_template('form.html', result=result)


#
# Write a compound interest function.
#
def calcCompoundInterest(principal, interest, numYears, timesPerYear):
    return principal * (1 + (interest / timesPerYear)) ** numYears



# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

