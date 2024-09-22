from flask import Flask, jsonify, request
import json
import sqlite3

app = Flask(__name__)



def db_connection():
    conn= None
    
    
    try: 
        conn = sqlite3.connect('products.sqlite')
        
    except sqlite3.error as e:
        print(e)
    return conn


@app.route('/products', methods=['GET', 'POST'])
def books():
    conn = db_connection()
    cursor = conn.cursor()
    
    if request.method == 'GET':
        cursor = conn.execute("SELECT * FROM product")
        products = [
            dict(id=row[0], price=row[1],title=row[2] )
            for row in cursor.fetchall()
        ]
        if products is not None:
            return jsonify(products)
    
    if request.method == 'POST':
        new_price = request.form['price']
        new_title = request.form['title']
        sql = """ INSERT INTO product (price, title) VALUES(?,?)"""
        cursor = cursor.execute(sql,(new_price, new_title))
        conn.commit()
        return f"Product with the id:{cursor.lastrowid} created ", 201



        
    
@app.route('/products/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
def single_product(id):
    conn = db_connection()
    cursor = conn.cursor()
    product = None
    if request.method == 'GET':
        cursor.execute("SELECT * FROM product WHERE id=?", (id,))
        rows = cursor.fetchall()
        for r in rows:
            product = r
        if product is not None:
            return jsonify(product), 200
        else:
            return f"Product with the id:{id} not found ", 404
            
        
    if request.method == 'PUT':
        sql = """ UPDATE product 
            SET price=?,
            title=?
            WHERE id=?"""

        
        price = request.form['price']
        title = request.form['title']
        updated_product = {
                    'id': id,
                    'price' : price,
                    'title': title
                }
        conn.execute(sql, (price, title, id))
        conn.commit
        jsonify(updated_product)
        return f"Product is updated to {updated_product}", 200
    

    if request.method == 'DELETE':
        sql = """DELETE FROM product WHERE id=?"""
        conn.execute(sql, (id,))
        conn.commit()
        # return "The book with id: {} has been deleted".format(id), 200 
        return f" the product with id {id} is deleted", 200      

    


if __name__ == "__main__":
    app.run(debug=True)