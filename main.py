from flask import Flask, render_template, request
from tools.encoding import encode_to_base64, decode_from_base64, text_to_bytes_str, bytes_str_to_text
from tools.encoding import xor_text
from tools.datetimes import days_until

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
    holidays = {
        '元旦': '2025-01-01',
        '清明节': '2024-04-04',
        '劳动节': '2024-05-01',
        '中秋节': '2024-09-08',
        '国庆节': '2024-10-01',
        '春节': '2025-01-25'
    }
    days_until_holidays = {holiday: days_until(date_str) for holiday, date_str in holidays.items()}

    return render_template('holidays.html', days_until=days_until_holidays)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9205)
