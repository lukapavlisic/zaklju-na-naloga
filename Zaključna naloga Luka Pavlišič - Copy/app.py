from flask import Flask, render_template, url_for, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# TUKAJ DEFINIRAJ SVOJE AVTE
# Format: [Znamka, Model, Cena, Gorivo, Izgled, Menjalnik, Tip, Trg, Slika]

avto1 = ["BMW", "F30 320d", 11000, "Diesel", "Športen", "Avtomatski", "Moderen", "Slovenski", "avto1nadgrajen.jpg"]
avto2 = ["BMW", "F32 420d", 16000, "Diesel", "Športen", "Avtomatski", "Moderen", "Nemški", "avto2nadgrajen.jpg"]
avto3 = ["Volkswagen", "Jetta", 3000, "Diesel", "Klasičen", "Ročni", "Navaden", "Slovenski", "avto3nadgrajen.jpg"]
avto4 = ["Audi", "A4", 16000, "Diesel", "Luksuzen", "Avtomatski", "Moderen", "Slovenski", "avto4nadgrajen.jpg"]
avto5 = ["Ford", "Focus", 9000, "Bencin", "Navaden", "Ročni", "Navaden", "Slovenski", "avto5.jpg"]
avto6 = ["Opel", "Astra", 8500, "Diesel", "Klasičen", "Ročni", "Navaden", "Nemški", "avto6.jpg"]
avto7 = ["Renault", "Clio", 11000, "Bencin", "Mestni", "Ročni", "Navaden", "Slovenski", "avto7.jpg"]
avto8 = ["Volkswagen", "Passat", 14000, "Diesel", "Klasičen", "Avtomatski", "Prostornejši", "Nemški", "avto8.jpg"]
avto9 = ["BMW", "X5", 28000, "Diesel", "Luksuzen", "Avtomatski", "Terenski", "Nemški", "avto9.jpg"]
avto10 = ["Audi", "Q7", 32000, "Diesel", "Luksuzen", "Avtomatski", "Terenski", "Nemški", "avto10.jpg"]
avto11 = ["Toyota", "RAV4", 19000, "Hibrid", "Klasičen", "Avtomatski", "Terenski", "Slovenski", "avto11.jpg"]
avto12 = ["Peugeot", "208", 10000, "Bencin", "Mestni", "Ročni", "Navaden", "Slovenski", "avto12.jpg"]
avto13 = ["Ford", "Mondeo", 13000, "Diesel", "Klasičen", "Avtomatski", "Prostornejši", "Nemški", "avto13.jpg"]
avto14 = ["Volkswagen", "Tiguan", 19000, "Diesel", "Moderen", "Avtomatski", "Terenski", "Slovenski", "avto14.jpg"]
avto15 = ["Mazda", "MX-5", 17000, "Bencin", "Športen", "Ročni", "Moderen", "Slovenski", "avto15.jpg"]

# ZDRUŽI VSE AVTE
vsi_avti = [avto1, avto2, avto3, avto4, avto5, avto6, avto7, avto8, avto9, avto10, avto11, avto12, avto13, avto14, avto15]


@app.route('/')
def iskanje():
    return render_template('iskanje.html')

# STRANI ZA POSAMEZNE AVTE
@app.route('/avto1')
def stran_avto1():
    return render_template('avto1.html')

@app.route('/avto2')
def stran_avto2():
    return render_template('avto2.html')

@app.route('/avto3')
def stran_avto3():
    return render_template('avto3.html')

@app.route('/avto4')
def stran_avto4():
    return render_template('avto4.html')

@app.route('/avto5')
def stran_avto5():
    return render_template('avto5.html')

@app.route('/avto6')
def stran_avto6():
    return render_template('avto6.html')

@app.route('/avto7')
def stran_avto7():
    return render_template('avto7.html')

@app.route('/avto8')
def stran_avto8():
    return render_template('avto8.html')

@app.route('/avto9')
def stran_avto9():
    return render_template('avto9.html')

@app.route('/avto10')
def stran_avto10():
    return render_template('avto10.html')

@app.route('/avto11')
def stran_avto11():
    return render_template('avto11.html')

@app.route('/avto12')
def stran_avto12():
    return render_template('avto12.html')

@app.route('/avto13')
def stran_avto13():
    return render_template('avto13.html')

@app.route('/avto14')
def stran_avto14():
    return render_template('avto14.html')

@app.route('/avto15')
def stran_avto15():
    return render_template('avto15.html')


# API ZA ISKANJE - ZELO PREPROSTO
@app.route('/api/avti', methods=['GET'])
def api_avti():
    # PREBERI KAJ UPORABNIK IŠČE
    uporabnik_budget = request.args.get('budget', '')
    uporabnik_izgled = request.args.get('izgled', '')
    uporabnik_gorivo = request.args.get('gorivo', '')
    uporabnik_menjalnik = request.args.get('menjalnik', '')
    uporabnik_trg = request.args.get('trg', '')
    uporabnik_tip = request.args.get('tip', '')
    
    # SEZNAM NAJDENIH AVTOV
    najdeni_avti = []
    
    # POGLEJ VSAK AVTO
    for avto in vsi_avti:
        # DOBI ID AVTA (KATERI AVTO JE V SEZNAMU vsi_avti)
        avto_id = vsi_avti.index(avto) + 1
        
        # ALI TA AVTO USTREZA?
        avto_ustreza = True
        
        # PREVERI BUDGET
        if uporabnik_budget != '':
            uporabnik_budget_stevilo = int(uporabnik_budget)
            avto_cena = avto[2]
            if avto_cena > uporabnik_budget_stevilo:
                avto_ustreza = False
        
        if uporabnik_gorivo != '':
            avto_gorivo = avto[3]
            if avto_gorivo != uporabnik_gorivo:
                avto_ustreza = False
        # PREVERI IZGLED
        if uporabnik_izgled != '':
            avto_izgled = avto[4]
            if avto_izgled != uporabnik_izgled:
                avto_ustreza = False
        
        # PREVERI MENJALNIK
        if uporabnik_menjalnik != '':
            avto_menjalnik = avto[5]
            if avto_menjalnik != uporabnik_menjalnik:
                avto_ustreza = False
        
        # PREVERI TIP
        if uporabnik_tip != '':
            avto_tip = avto[6]
            if avto_tip.lower() != uporabnik_tip.lower():
                avto_ustreza = False
        
        # PREVERI TRG
        if uporabnik_trg != '':
            avto_trg = avto[7]
            if avto_trg.lower() != uporabnik_trg.lower():
                avto_ustreza = False
        
        # ČE TA AVTO USTREZA, GA DODAJ
        if avto_ustreza == True:
            avto_podatki = {
                "id": avto_id,
                "znamka": avto[0],
                "model": avto[1],
                "cena": avto[2],
                "gorivo": avto[3],
                "izgled": avto[4],
                "menjalnik": avto[5],
                "tip": avto[6],
                "trg": avto[7],
                "slika": avto[8]
            }
            najdeni_avti.append(avto_podatki)
    
    # VRNI NAJDENE AVTE
    return jsonify(najdeni_avti)


if __name__ == '__main__':
    app.run(debug=True)
