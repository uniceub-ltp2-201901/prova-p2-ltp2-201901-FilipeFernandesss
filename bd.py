def inserir_url1(cursor, conn, url_original, url_encurtada):
    cursor.execute(f'insert into urls (url_original, url_encurtada, contador) values ("{url_original}", "{url_encurtada}", 0);')
    conn.commit()


def get_url_encurtada(cursor):
    cursor.execute(f'select url_encurtada from urls')
    encurtada = cursor.fetchall()
    return encurtada


def get_url_original(cursor, url_encurtada):
    cursor.execute(f'select url_original from urls where url_encurtada = "{url_encurtada}";')
    url_ori = cursor.fetchone()
    if url_ori:
        return url_ori
    else:
        return False


def set_ct(cursor, conn, ct, rota):
    cursor.execute(f"UPDATE urls SET contador ='{ct}' WHERE url_original = '{rota}';")

    conn.commit()


def get_ct(cursor, rota):
    cursor.execute(f'select contador from urls where url_original = "{rota}";')
    contador = cursor.fetchone()
    return contador


def get_total_contadores(cursor):
    cursor.execute(f'select url_original, url_encurtada, contador from urls order by contador DESC;')
    contadores = cursor.fetchall()
    return contadores
