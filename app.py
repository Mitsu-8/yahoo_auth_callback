from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'Yahoo OAuth callback server is running!'

@app.route('/callback')
def callback():
    code = request.args.get('code')
    state = request.args.get('state')
    return f"""
    <h2>認証コード受診完了！</h2>
    <p><b>code:</b> {code}</p>
    <p><b>atate:</b> {state}</p>
    <p>このコードを使ってトークン交換が可能です。</p>
    """

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

