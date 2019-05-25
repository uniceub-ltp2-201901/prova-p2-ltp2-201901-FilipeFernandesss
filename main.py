#Filipe Fernandes Araujo RA: 21800169

from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
from bd import *
from random import randint


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

mysql = MySQL()

mysql.init_app(app)

app.config['MYSQL_DATABASE_USER'] = "root"
app.config['MYSQL_DATABASE_PASSWORD'] = "root"
app.config['MYSQL_DATABASE_DB'] = "encurtador_url"



@app.route("/")
def index():
    return render_template("form_url.html")


@app.route("/inserir", methods=['POST'])
def inserir_url():
    if request.method == 'POST':
        url_original = request.form['url']
        url_encurtada = None

        conn = mysql.connect()
        cursor = conn.cursor()

        print(url_original)

        urls_encurtadas = get_url_encurtada(cursor)

        cursor.close()
        conn.close()

        url_encurtada = randint(11111, 99999)
        print(url_encurtada)
        for url in urls_encurtadas:
            print(url)
            if url != url_encurtada:

                conn = mysql.connect()
                cursor = conn.cursor()
                inserir_url1(cursor, conn, url_original, url_encurtada)
                cursor.close()
                conn.close()
                break

        return render_template("inserido.html", url_original=url_original, url_encurtada=url_encurtada)


@app.route("/rota1")
def rota1():
    conn = mysql.connect()
    cursor = conn.cursor()
    url_original = 'rota1'
    valor_contador = get_ct(cursor, url_original)
    ct = int(valor_contador[0]) + 1

    set_ct(cursor, conn, ct, url_original)

    return render_template("rota.html", ct=ct, url_original=url_original)


@app.route("/rota2")
def rota2():
    conn = mysql.connect()
    cursor = conn.cursor()
    url_original = 'rota2'
    valor_contador = get_ct(cursor, url_original)
    ct = int(valor_contador[0]) + 1

    set_ct(cursor, conn, ct, url_original)
    return render_template("rota.html", ct=ct, url_original=url_original)


@app.route("/rota3")
def rota3():
    conn = mysql.connect()
    cursor = conn.cursor()
    url_original = 'rota3'
    valor_contador = get_ct(cursor, url_original)
    ct = int(valor_contador[0]) + 1

    set_ct(cursor, conn, ct, url_original)
    return render_template("rota.html", ct=ct, url_original=url_original)


@app.route("/rota4")
def rota4():
    conn = mysql.connect()
    cursor = conn.cursor()
    url_original = 'rota4'
    valor_contador = get_ct(cursor, url_original)
    ct = int(valor_contador[0]) + 1

    set_ct(cursor, conn, ct, url_original)
    return render_template("rota.html", ct=ct, url_original=url_original)


@app.route("/<url_encurtada>")
def redirecionar(url_encurtada):

        valor_url = url_encurtada

        print(valor_url)

        conn = mysql.connect()
        cursor = conn.cursor()

        url_original = get_url_original(cursor, valor_url)
        if url_original:
            print(url_original[0])

            cursor.close()
            conn.close()
            return redirect(url_for(f'{url_original[0]}'))
        else:
            return "URL ENCURTADA INVÁLIDA"



# Rota para retornar os contadores
@app.route("/relatorio")
def relatorio_acessos():
    conn = mysql.connect()
    cursor = conn.cursor()

    urls = get_total_contadores(cursor)

    return render_template("relatorio_acessos.html", urls=urls)

if __name__ == "__main__":
    app.run(debug=True)
