from flask import Flask, render_template, request
import jieba
app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        if request.values['send'] == 'send':
            return render_template('IR.html', keyword=jieba.lcut(request.values['keyword'], cut_all=True, HMM=True))
    return render_template('IR.html', keyword="")
    # return render_template("IR.html")

    # run app
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
