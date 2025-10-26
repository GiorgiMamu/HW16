from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/multiply/<int:num1>/<int:num2>/<int:num3>/<int:num4>')
def multiply(num1, num2, num3, num4):
    result = num1 * num2 * num3 * num4
    return f'<h1>{num1} * {num2} * {num3} * {num4} = {result}</h1>'


@app.route('/info')
def info():
    data = {
        "name": "ME, GIORGI",
        "age": 21,
        "height": "arvici",
        "weight": "arc es",
        "vswavlob" : "flasks"
    }
    return jsonify(data)

@app.route('/hello/<name>')
def hello(name):
    return f'<h1> hello, {name}. welcome to flask app </h1>'

@app.errorhandler(404)
def page_not_found(e):
    return '<h1>თქვენ მოხვდით არარსებულ გვერდზე, გთხოვთ დაბრუნდეთ მთავარ გვერდზე!</h1><a href="/">Go to Home Page</a>', 404


if __name__ == '__main__':
    app.run(debug=True)