from flask import Flask, render_template , url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def showdashboard():
    return render_template('dashboard.html')



if __name__ == '__main__':
    app.run(debug=True)

