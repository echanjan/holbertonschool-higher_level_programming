#!/usr/bin/python3
"""
Este módulo de prueba sirve para conectar
con MySQL
"""


import MySQLdb
import sys


def main():
    """
    Esta función hace la consulta de la
    tabla states en hbtn_0e_0_usa.
    """
    user_mysql = sys.argv[1]
    pass_mysql = sys.argv[2]
    db_mysql = sys.argv[3]
    host_mysql = 'localhost'
    port_mysql = 3306

    cnn = MySQLdb.connect(
        host=host_mysql,
        user=user_mysql,
        password=pass_mysql,
        port=port_mysql,
        database=db_mysql
    )

    sql = """
             SELECT *
               FROM states
              WHERE name
        LIKE BINARY 'N%'
           ORDER BY id ASC
        """

    rs = cnn.cursor()
    rs.execute(sql)
    rows = rs.fetchall()

    for row in rows:
        print(row)

    rs.close()
    cnn.close()


if __name__ == "__main__":
    """
    Esta validación evita que se ejecute
    este archivo.
    """
    main()
