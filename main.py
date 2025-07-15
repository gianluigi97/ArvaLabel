from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


# @app.route('/')
# def homepage():
#     return render_template('index.html')

@app.route('/')
def init():
    return redirect(url_for('homepage'))

@app.route('/home')
def homepage():
    page = 'home_section.html'
    return render_template('index.html', page=page)

@app.route('/products')
def products():
    page = 'product_section.html'
    return render_template('index.html', page=page)






if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)
