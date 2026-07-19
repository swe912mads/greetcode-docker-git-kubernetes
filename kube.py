from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <body style="display:flex;justify-content:center;align-items:center;height:100vh;
                  background:linear-gradient(135deg,#ff9a9e,#a18cd1);margin:0;">
        <a href="https://www.example.com" target="_blank"
           style="padding:15px 30px;font-size:20px;color:white;
                  background:#ff6a6a;border-radius:10px;text-decoration:none;">
            Visit website
        </a>
    </body>
    '''

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)