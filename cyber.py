from flask import Flask, render_template, request, redirect
from db import mydb, mycursor


app = Flask(__name__)

@app.route('/')
def index():
    mycursor.execute("SELECT * FROM book")
    book = mycursor.fetchall()
    return render_template('index.html', book = book)


@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'GET':
        return render_template('post_form.html')
    if request.method == 'POST':
        book_name = request.form['book']
        address = request.form['address']
        phone = request.form['phone']
        time = request.form['time']
        sql = 'INSERT INTO book (book_name, address, phone, time) VALUES (%s, %s, %s, %s)'
        val = (book_name, address, phone, time)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/')
    
    

@app.route('/items')
def item():
    mycursor.execute("SELECT * FROM book")
    book = mycursor.fetchall()
    return render_template('items.html', book = book)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'GET':
        mycursor.execute(f'SELECT * FROM book WHERE ID={id}')
        book = mycursor.fetchone()
        return render_template('edit.html', book = book)
    if request.method == 'POST':
        book_name = request.form['book_name']
        address = request.form['address']
        phone = request.form['phone']
        time = request.form['time']
        sql = f'UPDATE book SET book_name = %s, address = %s, phone = %s, time = %s, WHERE ID = %s'
        values =  (book_name,  address, phone, time)
        mycursor.execute(sql, values)
        mydb.commit()
        return redirect('/')
    


@app.route('/delete/<int:id>')
def delete_book(id):
    sql = f'DELETE FROM book WHERE ID={id}'
    mycursor.execute(sql)
    mydb.commit()
    return redirect('/')    


if __name__ == '__main__':
    app.run()