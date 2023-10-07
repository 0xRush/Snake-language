from flask import Flask, render_template, request, flash
import basic

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        req = request.form["workspace"].strip()
        result, error = basic.run('<stdin>', req)
        if error:
            flash(f'حدث خطأ ما', 'danger')
            return render_template('home.html', res=error.as_string(), req=req)
        elif result:
            if len(result.elements) == 1:
                flash(f'نجح الأمر', 'success')
                return render_template('home.html', res=repr(result.elements[0]), req=req)
            else:
                flash(f'نجح الأمر', 'success')
                return render_template('home.html', res=repr(result), req=req)
    
    return render_template('home.html')

@app.route("/docs")
def docs():
    return render_template('docs.html')

if __name__ == '__main__':
    app.run(debug=True)