from flask import Flask, render_template
app=Flask(__name__)


#首頁
@app.route('/')
@app.route('/<name>')
def index(name='GUEST'):
    date=get_date()
    return render_template('./index.html', x_name=name,date=date)

@app.route('/date')
def get_date():
    from datetime import datetime
    date = datetime.now()

    return date.strftime('%Y-%m-%d %H:%M:%S')

@app.route('/book/<int:id>')
def get_book(id):
    try:
        books={1:"python",2:"html",3:"css"}

        return books[id]
    except Exception as e:
        print(e)
        return '書籍編號錯誤'

@app.route('/sum/x=<a>&y=<b>')
def get_sum(a,b):
    total=eval(a)+eval(b)
    return f'{a}+{b}={total}'

@app.route('/bmi/name=<name>&height=<height>&weight=<weight>')
def get_bmi(name,height,weight):
    try:
        bmi=eval(weight)/(eval(height)/100)**2

        return 'BMI:%.2f' % bmi
    except:
        return '參數輸入錯誤!'

@app.route('/stock')
def get_stock():
    stocks=[
        {'分類':'日經指數','指數':'22.920.30'},
        {'分類':'日經指數','指數':'22.920.30'},
        {'分類':'日經指數','指數':'22.920.30'},
        {'分類':'日經指數','指數':'22.920.30'},
    ]

    return render_template('./stock.html',date=get_date(),stocks=stocks)



app.run(debug=True)


