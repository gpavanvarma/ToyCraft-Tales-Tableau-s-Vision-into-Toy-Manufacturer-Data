from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def dashboard():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    return Response(content, mimetype='text/html')

if __name__ == '__main__':
    app.run(debug=True)
