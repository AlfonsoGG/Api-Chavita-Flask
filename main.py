from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok
import pymysql.cursors

# inicializa flask con el nombre main.py
app = Flask(__name__)
run_with_ngrok(app)


@app.route('/productos/', methods=['POST'])
def get_product():
    if request.method == 'POST':
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='Strouts3313!',
                                     db='flaskmysql',
                                     cursorclass=pymysql.cursors.DictCursor)
        name = request.json['name']
        try:
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT name, cantidad FROM data_base WHERE name = %s "
                cursor.execute(sql, (name))
                result = cursor.fetchall()
        finally:
            connection.close()
            return jsonify(result), 200


if __name__ == "__main__":
    app.run()
