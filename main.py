from flask import Flask, render_template, request
from tools.encoding import encode_to_base64, decode_from_base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/base64', methods=['GET', 'POST'])
def base64():
    if request.method == 'POST':
        text_encode = request.form.get('text_encode', '')
        encoded_text = encode_to_base64(text_encode)

        encoded_text_decode = request.form.get('encoded_text_decode', '')
        text_decode = decode_from_base64(encoded_text_decode)

        return render_template('base64.html',
                                text_encode=text_encode,
                                encoded_text=encoded_text,
                                encoded_text_decode=encoded_text_decode,
                                text_decode=text_decode)
    return render_template('base64.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9205)
