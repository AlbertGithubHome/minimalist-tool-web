from flask import Flask, render_template, request
from tools.encoding import encode_to_base64, decode_from_base64, text_to_bytes_str, bytes_str_to_text
from tools.encoding import xor_text
from tools.encoding import decimal_to_base35, base35_to_decimal
from tools.datetimes import get_days_until_holidays

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

@app.route('/baseXX', methods=['GET', 'POST'])
def baseXX():
    if request.method == 'POST':
        text_encode = request.form.get('text_encode', '')
        encoded_text = decimal_to_base35(text_encode)

        encoded_text_decode = request.form.get('encoded_text_decode', '')
        text_decode = base35_to_decimal(encoded_text_decode)

        return render_template('baseXX.html',
                                text_encode=text_encode,
                                encoded_text=encoded_text,
                                encoded_text_decode=encoded_text_decode,
                                text_decode=text_decode)
    return render_template('baseXX.html')

@app.route('/bytes', methods=['GET', 'POST'])
def bytes():
    if request.method == 'POST':
        text_to_bytes_input = request.form.get('text_to_bytes', '')
        text_to_bytes_result = text_to_bytes_str(text_to_bytes_input)

        bytes_to_text_input = request.form.get('bytes_to_text', '')
        bytes_to_text_result = bytes_str_to_text(bytes_to_text_input)

        return render_template('bytes.html',
                                text_to_bytes=text_to_bytes_input,
                                text_to_bytes_result=text_to_bytes_result,
                                bytes_to_text=bytes_to_text_input,
                                bytes_to_text_result=bytes_to_text_result)
    return render_template('bytes.html')

@app.route('/xor', methods=['GET', 'POST'])
def xor():
    if request.method == 'POST':
        input1 = request.form['input1']
        input2 = request.form['input2']
        xor_result = xor_text(input1, input2)
        return render_template('xor.html', input1=input1, input2=input2, xor_result=xor_result)
    else:
        return render_template('xor.html')

@app.route('/holidays')
def holidays():
    days_until = get_days_until_holidays()
    return render_template('holidays.html', days_until=days_until)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9205)
