import functools
import os
from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from db import init_db, get_db
import calendar, datetime
import random

app = Flask(__name__)
app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'app.sqlite'),
    )

tanaan = datetime.datetime.now()

vuo = int(tanaan.strftime("%Y"))
kuu = tanaan.strftime("%m")

kuukauded = ["Tammikuulle", "Helmikuulle", "Maalliskuulle", "Huhtikuulle", "Toukokuulle", "Kesäkuulle", "Heinäkuulle", "Elokuulle", "Syyskuulle", "Lokakuulle", "Marraskuulle", "Joulukuulle"]
kurssit = ["Docker", "Jenkins", "Vagrant", "Python", "DevOps", "LEAN IT"]
verkkokurssit = ["Git", "Linux", "RESTful APIs", "Python"]
viikkopaivat = ["Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai", "Lauantai", "Sunnuntai"]
etunimet = ["Anu", "Gleb", "Tiina", "Kimmo", "Tapio", "Lari"]
sukunimet = ["Sauko", "Tishchenko", "Maaranen", "Mikonranta", "Hietanen", "Kunnas"]
ryhmannimi = ["TVTeat Ketterä DevOps TYPO4"]
kouluttaja = ["OpsHost", "Christian Finnberg", "Pekka Tamminen", "Jukka Tenkamaa", "Kari Vikman", "Jani Iivonen"]
tila = ["Lab517", "Lab516", "Lab521", "Lab518", "Lab504", "Verkko"]

def db_populate_oppijat():
    db = get_db()

    for i in range(len(etunimet)):
        db.execute(
        'INSERT INTO oppilas (etunimi, sukunimi, ryhma_id)'
        ' VALUES (?, ?, ?)', (etunimet[i], sukunimet[i], 1)
        )
        i = i + 1
        db.commit()
    
    db.execute(
    'INSERT INTO ryhma (nimi)'
    ' VALUES (?)', (ryhmannimi)
    )
    db.commit()

def db_populate_lahipaivat():
    kuusi = int(kuu)
    kal = calendar.monthcalendar(vuo, kuusi)

    db = get_db()

    for viikko in kal:
        i=0
        for paiva in viikko:
            if paiva > 0:
                sattu = random.randrange(len(kurssit))
                aihe = kurssit[sattu]
                ope = kouluttaja[sattu]
                tilat = tila[sattu]
                pvm = str(paiva) + "." + str(kuusi)
                if i <= 4:
                    db.execute(
                        'INSERT INTO lahipaiva (pvm, aihe, kouluttaja, luokka, ryhma_id)'
                        ' VALUES (?, ?, ?, ?, ?)', (pvm, aihe, ope, tilat, 1)
                    )
                    print(pvm, aihe, ope, tilat, 1)
                    db.commit()
            i = i + 1

def db_populate_verkkokurssit():
    db = get_db()

    for i in range(len(verkkokurssit)):
        db.execute(
        'INSERT INTO verkkokurssi (verkkokurssinnimi)'
        ' VALUES (?)', (verkkokurssit[i], )
        )
        i = i + 1
        db.commit()

def db_populate_osallistuminen():
    db = get_db()

    db.execute(
    'INSERT INTO osallistuminen (oppilas_id, verkko_id, vaihe)'
    ' VALUES (?, ?, ?)', (1, 1, 0)
    )
    db.commit()

    db.execute(
    'INSERT INTO osallistuminen (oppilas_id, verkko_id, vaihe)'
    ' VALUES (?, ?, ?)', (1, 2, 0)
    )
    db.commit()

    db.execute(
    'INSERT INTO osallistuminen (oppilas_id, verkko_id, vaihe)'
    ' VALUES (?, ?, ?)', (1, 3, 0)
    )
    db.commit()

    db.execute(
    'INSERT INTO osallistuminen (oppilas_id, verkko_id, vaihe)'
    ' VALUES (?, ?, ?)', (2, 4, 0)
    )
    db.commit()

    db.execute(
    'INSERT INTO osallistuminen (oppilas_id, verkko_id, vaihe)'
    ' VALUES (?, ?, ?)', (2, 3, 0)
    )
    db.commit()

    db.execute(
    'INSERT INTO osallistuminen (oppilas_id, verkko_id, vaihe)'
    ' VALUES (?, ?, ?)', (2, 2, 0)
    )
    db.commit()

    db.execute(
    'INSERT INTO osallistuminen (oppilas_id, verkko_id, vaihe)'
    ' VALUES (?, ?, ?)', (3, 2, 0)
    )
    db.commit()

    db.execute(
    'INSERT INTO osallistuminen (oppilas_id, verkko_id, vaihe)'
    ' VALUES (?, ?, ?)', (3, 1, 0)
    )
    db.commit()

    db.execute(
    'INSERT INTO osallistuminen (oppilas_id, verkko_id, vaihe)'
    ' VALUES (?, ?, ?)', (3, 4, 0)
    )
    db.commit()

    db.execute(
    'INSERT INTO osallistuminen (oppilas_id, verkko_id, vaihe)'
    ' VALUES (?, ?, ?)', (4, 1, 0)
    )
    db.commit()

    db.execute(
    'INSERT INTO osallistuminen (oppilas_id, verkko_id, vaihe)'
    ' VALUES (?, ?, ?)', (4, 3, 0)
    )
    db.commit()

    db.execute(
    'INSERT INTO osallistuminen (oppilas_id, verkko_id, vaihe)'
    ' VALUES (?, ?, ?)', (4, 4, 0)
    )
    db.commit()

    db.execute(
    'INSERT INTO osallistuminen (oppilas_id, verkko_id, vaihe)'
    ' VALUES (?, ?, ?)', (5, 3, 0)
    )
    db.commit()

    db.execute(
    'INSERT INTO osallistuminen (oppilas_id, verkko_id, vaihe)'
    ' VALUES (?, ?, ?)', (5, 2, 0)
    )
    db.commit()

    db.execute(
    'INSERT INTO osallistuminen (oppilas_id, verkko_id, vaihe)'
    ' VALUES (?, ?, ?)', (5, 1, 0)
    )
    db.commit()

    db.execute(
    'INSERT INTO osallistuminen (oppilas_id, verkko_id, vaihe)'
    ' VALUES (?, ?, ?)', (6, 4, 0)
    )
    db.commit()

    db.execute(
    'INSERT INTO osallistuminen (oppilas_id, verkko_id, vaihe)'
    ' VALUES (?, ?, ?)', (6, 1, 0)
    )
    db.commit()

    db.execute(
    'INSERT INTO osallistuminen (oppilas_id, verkko_id, vaihe)'
    ' VALUES (?, ?, ?)', (6, 5, 0)
    )
    db.commit()

def initialize():
        init_db()
        db_populate_oppijat()
        db_populate_lahipaivat()
        db_populate_verkkokurssit()
        db_populate_osallistuminen()


@app.route('/v0/oppija/<int:id>', methods=('GET', 'POST'))
def get_oppija_view_v0(id):
    kuunyt = kuukauded[int(kuu)-1]
    session.clear()

    oppija = get_db().execute(
        'SELECT id, etunimi, sukunimi, ryhma_id'
        ' FROM oppilas'
        ' WHERE id = ?', (id, )
    ).fetchone()

    ryhma = get_db().execute(
        'SELECT id, nimi'
        ' FROM ryhma'
        ' WHERE id = ?', (oppija['ryhma_id'], )
        ).fetchone()
    
    lahipaivat = get_db().execute(
        'SELECT pvm, aihe, kouluttaja, luokka'
        ' FROM lahipaiva'
        ' WHERE ryhma_id = ?', (oppija['ryhma_id'], )
    ).fetchall()

    session['oppija_id'] = oppija['id']
    session['ryhma_id'] = oppija['ryhma_id']

    verkko_osallistuminen = get_db().execute(
        'SELECT verkko_id, vaihe'
        ' FROM osallistuminen'
        ' WHERE oppilas_id = ?', (id, )
        ).fetchall()
    
    verkkokurssit = []

    for kurssi in verkko_osallistuminen:
        verkkokurssi = get_db().execute(
        'SELECT verkkokurssinnimi'
        ' FROM verkkokurssi'
        ' WHERE verkko_id = ?', (kurssi['verkko_id'], )
        ).fetchone()
        verkkokurssit.append(verkkokurssi['verkkokurssinnimi'])

    checked = False

    session['oppija_id'] = oppija['id']
    session['ryhma_id'] = oppija['ryhma_id']
    
    return render_template('v0/oppija.html', tanaan=tanaan, 
    oppija=oppija, ryhma=ryhma, kuunyt=kuunyt, lahipaivat=lahipaivat, verkkokurssit=verkkokurssit, verkko_osallistuminen=verkko_osallistuminen,
    checked=checked)

@app.route('/v1/oppija/<int:id>', methods=('GET', 'POST'))
def get_oppija_view_v1(id):
    kuunyt = kuukauded[int(kuu)-1]
    session.clear()   

    oppija = get_db().execute(
        'SELECT id, etunimi, sukunimi, ryhma_id'
        ' FROM oppilas'
        ' WHERE id = ?', (id, )
    ).fetchone()

    ryhma = get_db().execute(
        'SELECT id, nimi'
        ' FROM ryhma'
        ' WHERE id = ?', (oppija['ryhma_id'], )
        ).fetchone()
    
    verkko_osallistuminen = get_db().execute(
        'SELECT verkko_id, vaihe'
        ' FROM osallistuminen'
        ' WHERE oppilas_id = ?', (id, )
        ).fetchall()

    verkkokurssit = []

    for kurssi in verkko_osallistuminen:
        verkkokurssi = get_db().execute(
        'SELECT verkkokurssinnimi'
        ' FROM verkkokurssi'
        ' WHERE verkko_id = ?', (kurssi['verkko_id'], )
        ).fetchone()
        verkkokurssit.append(verkkokurssi['verkkokurssinnimi'])

    checked = False

    session['oppija_id'] = oppija['id']
    session['ryhma_id'] = oppija['ryhma_id']

    if request.method == "POST":
        print(request.form)
        for i in request.form:
            print(i, request.form[i])


    return render_template('v1/oppija.html', tanaan=tanaan, 
    oppija=oppija, ryhma=ryhma, kuunyt=kuunyt, verkkokurssit=verkkokurssit,
    checked=checked)

if __name__ == "__main__":
    app.secret_key = 'dev'
    app.debug = True
    app.run()