import functools
import os
from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from db import init_db, get_db
from werkzeug.utils import secure_filename
import calendar, datetime
import random

app = Flask(__name__)
app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'app.sqlite'),
        MAX_CONTENT_LENGTH = 1 * 1024 * 1024,
        UPLOAD_FOLDER = 'static/media',
        ALLOWED_EXTENSIONS = set(['pdf'])
    )

tanaan = datetime.datetime.now()

vuo = int(tanaan.strftime("%Y"))
kuu = tanaan.strftime("%m")

kuukauded = ["Tammikuulle", "Helmikuulle", "Maalliskuulle", "Huhtikuulle", "Toukokuulle", "Kesäkuulle", "Heinäkuulle", "Elokuulle", "Syyskuulle", "Lokakuulle", "Marraskuulle", "Joulukuulle"]
kurssit = ["Docker", "Jenkins", "Vagrant", "Python", "DevOps", "LEAN IT"]
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

    db.execute(
    'INSERT INTO ryhma (nimi)'
    ' VALUES ("TVTeat Ketterä DevOps TYPO5")'
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

def initialize():
        init_db()
        db_populate_oppijat()
        db_populate_lahipaivat()


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
        'SELECT id, nimi, lukujarjestys, vastaava'
        ' FROM ryhma'
        ' WHERE id = ?', (oppija['ryhma_id'], )
        ).fetchone()
    
    session['oppija_id'] = oppija['id']
    session['ryhma_id'] = oppija['ryhma_id']
    session['sukunimi'] = oppija['sukunimi']
    session['lukujarjestys'] = ryhma['lukujarjestys']

    lisaaurl = "/v1/oppija/" + str(session['oppija_id']) + "/lisaaverkkokurssi"

    if session['lukujarjestys']:
        lukupolku = "../../" + session['lukujarjestys']
    else:
        lukupolku = None
        print(">>> ei lukujärjestystä")

    if ryhma['vastaava']:
        session['vastaava'] = ryhma['vastaava']
    else:
        print(">>> ryhmällä " + str(ryhma['id']) + " ei ole vastaavaa")
    
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
        print(">>> from db verkko_id -> " + str(kurssi['verkko_id']) + " vaihe -> " + str(kurssi['vaihe']))
    
    radionapit = range(3)

    if request.method == "POST":
        print(request.form)
        for i in request.form:
            verkkoId = get_db().execute(
                'SELECT verkko_id'
                ' FROM verkkokurssi'
                ' WHERE verkkokurssinnimi = ?', (i, )
            ).fetchone()

            db = get_db()
            db.execute(
                'UPDATE osallistuminen'
                ' SET vaihe = ?'
                ' WHERE oppilas_id = ? AND verkko_id = ?', (int(request.form[i]), 
                int(session['oppija_id']), int(verkkoId['verkko_id']))
            )
            db.commit()  

    return render_template('v1/oppija.html', tanaan=tanaan, 
    oppija=oppija, ryhma=ryhma, kuunyt=kuunyt,
    verkko_osallistuminen=verkko_osallistuminen,
    verkkokurssit=verkkokurssit, radionapit=radionapit, lisaaurl=lisaaurl, lukupolku=lukupolku)

@app.route('/v1/oppija/<int:id>/lisaaverkkokurssi', methods=('GET', 'POST'))
def lisaa_verkkokurssi(id):
    kotiurl = "/v1/oppija/" + str(session['oppija_id'])

    if request.method == "POST":
        db = get_db()
        vkurssi = None

        if request.form['verkkokurssi']:
            vkurssi = db.execute(
                'SELECT * FROM verkkokurssi'
                ' WHERE verkkokurssinnimi =  ?', (request.form['verkkokurssi'], )
            ).fetchall()

        if not vkurssi:
            db.execute(
                'INSERT INTO verkkokurssi (verkkokurssinnimi)'
                ' VALUES (?)', (request.form['verkkokurssi'], )
            )
            db.commit()
            print(">>> lisätty verkkokurssi " + request.form['verkkokurssi'])

        verkkoId = get_db().execute(
                'SELECT verkko_id'
                ' FROM verkkokurssi'
                ' WHERE verkkokurssinnimi = ?', (request.form['verkkokurssi'], )
            ).fetchone()
        print(">>> id db:stä " + request.form['verkkokurssi'] + " " + str(verkkoId['verkko_id']))

        osallistuminen = db.execute(
            'SELECT * FROM osallistuminen'
            ' WHERE verkko_id = ? AND oppilas_id = ?', (verkkoId['verkko_id'], session['oppija_id'])
        ).fetchall()

        if not osallistuminen:
            db.execute(
                'INSERT INTO osallistuminen (oppilas_id, verkko_id, vaihe)'
                ' VALUES (?, ?, ?)', (int(session['oppija_id']), verkkoId['verkko_id'], 0)
            )
            db.commit()
            print(">>> lisätty osallistuminen kurssi ID " + str(verkkoId['verkko_id']) + " oppija ID " + str(int(session['oppija_id'])))
        else:
            print(">>> kurssi id " + str(verkkoId['verkko_id']) + " on jo seurannassa ")

    return render_template('v1/lisaaverkkokurssi.html', kotiurl=kotiurl)

@app.route('/v1/admin', methods=('GET', 'POST'))
def get_admin_view():

    db = get_db()
        
    ryhmat = db.execute(
        'SELECT * FROM ryhma'
    ).fetchall()

    oppijat = []

    if request.method == 'POST':
        print(request.files)
        print(request.form)
        if request.form:
            if 'uusiryhma' in request.form:
                if request.form['uusiryhma']:
                    nimi = request.form['uusiryhma'].rstrip()
                    check = db.execute(
                        'SELECT nimi FROM ryhma'
                        ' WHERE nimi = ?', (nimi, )
                    ).fetchone()
                    db.commit()

                    if check:
                        print(">>> ryhma " + check['nimi'] + "on jo kannassa ")
                    else:
                        db.execute(
                            'INSERT INTO ryhma (nimi)'
                            ' VALUES (?)', (request.form['uusiryhma'], )
                        )
                        db.commit()
                        print(">>> uusi ryhma " + request.form['uusiryhma'] + " lisätty kantaan")
                else:
                    print(">>> uusi ryhma tyhjä")

            if 'ryhma' in request.form:
                ryhma = db.execute(
                'SELECT id, nimi FROM ryhma'
                ' WHERE nimi = ?', (request.form['ryhma'], )
                ).fetchone()

                session['ryhma_id'] = ryhma['id']
                session['ryhma_nimi'] = ryhma['nimi']
                print(">>> session ryhmä id: " + str(session['ryhma_id']) + " nimi:" + session['ryhma_nimi'])

                oppijat = db.execute(
                'SELECT * FROM oppilas'
                ' WHERE ryhma_id = ?', (session['ryhma_id'], )
                ).fetchall()

            else:
                print(">>> ryhmä tyhjä")
            
            if 'sukunimi' in request.form:
                if request.form['sukunimi']:
                    db.execute(
                        'INSERT INTO oppilas (etunimi, sukunimi, ryhma_id)'
                        ' VALUES (?, ?, ?)', (request.form['etunimi'], request.form['sukunimi'], session['ryhma_id'])
                    )
                    db.commit()
                    print(">>> oppija " + request.form['sukunimi'] + " lisätty ryhmään " + str(session['ryhma_id']))
                else:
                    print(">>> sukunimi tyhjä")
            
            if 'vastaavaemail' in request.form:
                if request.form['vastaavaemail']:
                    mail = request.form['vastaavaemail'].rstrip()
                    db.execute(
                    'UPDATE ryhma'
                    ' SET vastaava = ?'
                    ' WHERE id = ?', (mail, session['ryhma_id'])
                    )
                    db.commit()  
                    print(">>> " + mail + " lisätty ryhmään " + str(session['ryhma_id']))
                else:
                    print(">>> vastaavan email on tyhjä")
        
        if request.files:
            print(">>> tiedosto käsitellään")
            if 'luku' not in request.files:
                print(">>> ei tiedostoa ")
            
            tiedosto = request.files['luku']
            
            if tiedosto.filename == '':
                print(">>> tiedosto ei valittu")
            
            if tiedosto:
                tiedostonnimi = secure_filename(tiedosto.filename)
                tiedosto.save(os.path.join(app.config['UPLOAD_FOLDER'], tiedostonnimi))
                db.execute(
                    'UPDATE ryhma'
                    ' SET lukujarjestys = ?'
                    ' WHERE id = ?', (os.path.join(app.config['UPLOAD_FOLDER'], tiedostonnimi),
                    session['ryhma_id'])
                )
                db.commit()
                print(">>> tiedosto ladattu " + tiedostonnimi + " ryhmä nro. " + str(session['ryhma_id']))
                print(">>> polku tiedostoon lisätty kantaan " + os.path.join(app.config['UPLOAD_FOLDER'], tiedostonnimi))
    
    else:
        redirect('v1/admin')

    return render_template('/v1/admin.html', ryhmat=ryhmat, oppijat=oppijat)

if __name__ == "__main__":
    app.debug = True
    app.run()