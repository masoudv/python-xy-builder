from flask import Flask, request, render_template, send_file
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Calculate M</title>
    </head>
    <body>
        <h1>Enter Values for A, B, and C</h1>
        <form action="/calculate" method="post">
            <label for="A">A:</label>
            <input type="number" step="any" id="A" name="A" required><br><br>
            <label for="B">B:</label>
            <input type="number" step="any" id="B" name="B" required><br><br>
            <label for="C">C:</label>
            <input type="number" step="any" id="C" name="C" required><br><br>
            <button type="submit">Calculate</button>
        </form>
    </body>
    </html>
    '''

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # دریافت مقادیر ورودی
        A = float(request.form['A'])
        B = float(request.form['B'])
        C = float(request.form['C'])

        # محاسبه مقادیر M برای T از 0 تا 400
        data = {'T': [], 'M': []}
        for T in range(0, 401):  # شامل 400
            M = A + B * (T / 300) ** C
            data['T'].append(T)
            data['M'].append(M)

        # ذخیره داده‌ها در فایل CSV
        df = pd.DataFrame(data)
        csv_file = '/workspaces/python-xy-builder/output.csv'
        df.to_csv(csv_file, index=False)

        # ارسال فایل CSV به کاربر
        return send_file(csv_file, as_attachment=True)

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)