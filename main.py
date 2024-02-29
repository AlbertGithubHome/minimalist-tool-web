from flask import Flask, request
import base64

app = Flask(__name__)

def encode_to_base64(text):
    encoded_text = base64.b64encode(text.encode()).decode()
    return encoded_text

@app.route('/')
def index():
    return '''
    <h1>编码转换工具</h1>
    <form method="post" action="/encode">
        <label for="text">输入文字:</label><br>
        <textarea id="text" name="text" rows="4" cols="50"></textarea><br>
        <button type="submit">转换为Base64</button><br><br>
        <label for="encoded_text">Base64 编码结果:</label><br>
        <textarea id="encoded_text" name="encoded_text" rows="4" cols="50" readonly></textarea><br>
    </form>
    '''

@app.route('/encode', methods=['POST'])
def encode_text():
    if 'text' in request.form:
        text = request.form['text']
        encoded_text = encode_to_base64(text)
        return '''
        <h1>编码转换工具</h1>
        <form method="post" action="/encode">
            <label for="text">输入文字:</label><br>
            <textarea id="text" name="text" rows="4" cols="50">{}</textarea><br>
            <button type="submit">转换为Base64</button><br><br>
            <label for="encoded_text">Base64 编码结果:</label><br>
            <textarea id="encoded_text" name="encoded_text" rows="4" cols="50" readonly>{}</textarea><br>
        </form>
        '''.format(text, encoded_text)
    else:
        return '''
        <h1>没有输入文本</h1>
        <a href="/">返回</a>
        '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9205)
