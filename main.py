from flask import Flask, render_template, request
from tools.encoding import encode_to_base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tool', methods=['GET', 'POST'])
def tool():
    if request.method == 'POST':
        text = request.form.get('text', '')
        encoded_text = encode_to_base64(text)
        return render_template('tool.html', text=text, encoded_text=encoded_text)
    return render_template('tool.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9205)
