from flask import Flask,render_template

app=Flask(__name__)

posts=[
        {
            'author':'barani',
            'title':'Blog Post 1',
            'content':'First post content',
            'date_posted':'jan 20, 2025'
        },

        {
            'author':'sanjay',
            'title':'Blog Post 2',
            'content':'First post content',
            'date_posted':'feb 20, 2024'
        },

]

@app.route('/')
def index():
    return render_template('home.html',posts=posts)

if __name__=="__main__":
    app.run(debug=True)
