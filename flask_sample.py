from flask import Flask
app=Flask(__name__)
@app.route('/') #points to the home function

@app.route('/home')     #this also points to the home function
def home():
    return 'This is home page'

@app.route('/about')   #this points the about function
def about():
    return 'This is about page'

if __name__ == '__main__':
    app.run(debug=True)