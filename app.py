from flask import Flask, render_template, request
import qrcode

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    qr_path = None

    if request.method == 'POST':
        text = request.form['data']   # get input from form

        # generate QR code
        img = qrcode.make(text)

        # save image
        img.save("static/qr.png")

        qr_path = "static/qr.png"

    return render_template('index.html', qr=qr_path)


if __name__ == '__main__':
    app.run(debug=True)