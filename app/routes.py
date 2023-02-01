import psycopg2

from app import app
from flask import Flask, render_template, request, flash, url_for, redirect

# konfigurasi database
conn = psycopg2.connect(host="localhost", database="sistem_informasi_siswa", user="postgres", password="123456")
cur = conn.cursor()

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/login')
def login():

    return render_template('login.html')

@app.route('/login_validation', methods=['POST'])
def login_validation():
    if request.method == 'POST':
        id = request.form['id']
        password = request.form['password']

        uname_asli = 'syabrienapv'
        pass_asli = '123456'

        if id == uname_asli and password == pass_asli:
            validation = 'True'
        else:
            validation = 'False'

    return render_template('login.html', validation = validation)

@app.route('/pengajar')
def pengajar():

    return render_template('pengajar.html')

@app.route('/snmptn')
def snmptn():

    return render_template('snmptn.html')

@app.route('/AV')
def AV():

    return render_template('AV.html')

@app.route('/BKP')
def BKP():

    return render_template('BKP.html')

@app.route('/DKV')
def DKV():

    return render_template('DKV.html')

@app.route('/DPIB')
def DPIB():

    return render_template('DPIB.html')

@app.route('/TBSM')
def TBSM():

    return render_template('TBSM.html')

@app.route('/TITL')
def TITL():

    return render_template('TITL.html')

@app.route('/TKRO')
def TKRO():

    return render_template('TKRO.html')

@app.route('/TP')
def TP():

    return render_template('TP.html')

@app.route('/TPTU')
def TPTU():

    return render_template('TPTU.html')
    
# Read
@app.route('/data_siswa')
def data_siswa():
    # koneksi database
    cur.execute("SELECT * FROM data_siswa")
    data = cur.fetchall()
    # cur.close()
    # conn.close()

    return render_template('data_siswa.html', students = data)

# Create 
@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        nisn = request.form['nisn']
        niss = request.form['niss']
        nama = request.form['nama']
        tanggal_lahir = request.form['tanggal_lahir']
        tempat_lahir = request.form['tempat_lahir']
        alamat = request.form['alamat']
        jenis_kelamin = request.form['jenis_kelamin']
        nama_orangtua = request.form['nama_orangtua']
        asal_sekolah = request.form['asal_sekolah']
        tahun_ijazah = request.form['tahun_ijazah']
        riwayat_pelayanan = request.form['riwayat_pelayanan']
        data_assesment = request.form['data_assesment']
        a = [nisn, niss, nama, tanggal_lahir, tempat_lahir, alamat, jenis_kelamin, nama_orangtua, asal_sekolah, tahun_ijazah, riwayat_pelayanan, data_assesment]
        print(a)
        cur.execute("INSERT INTO data_siswa (nisn, niss, nama, tanggal_lahir, tempat_lahir, alamat, jenis_kelamin, nama_orangtua, asal_sekolah, tahun_ijazah, riwayat_pelayanan, data_assesment) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (nisn, niss, nama, tanggal_lahir, tempat_lahir, alamat, jenis_kelamin, nama_orangtua, asal_sekolah, tahun_ijazah, riwayat_pelayanan, data_assesment))
        conn.commit()

        return redirect(url_for('data_siswa'))

# Update
@app.route('/update/<id_data>', methods=['POST'])
def update(id_data):
    if request.method == 'POST':
        nisn = request.form['nisn']
        niss = request.form['niss']
        nama = request.form['nama'] 
        tanggal_lahir = request.form['tanggal_lahir']
        tempat_lahir = request.form['tempat_lahir']
        alamat = request.form['alamat']
        jenis_kelamin = request.form['jenis_kelamin']
        nama_orangtua = request.form['nama_orangtua']
        asal_sekolah = request.form['asal_sekolah']
        tahun_ijazah = request.form['tahun_ijazah']
        riwayat_pelayanan = request.form['riwayat_pelayanan']
        data_assesment = request.form['data_assesment']
        cur.execute("""UPDATE data_siswa 
                    SET nisn=%s, niss=%s, nama=%s, tanggal_lahir=%s, tempat_lahir=%s, alamat=%s,
                    jenis_kelamin=%s, nama_orangtua=%s, asal_sekolah=%s, tahun_ijazah=%s, riwayat_pelayanan=%s, data_assesment=%s 
                    WHERE id=%s
                    """, (nisn,niss,nama,tanggal_lahir,tempat_lahir,alamat,jenis_kelamin,
                    nama_orangtua,asal_sekolah,tahun_ijazah,riwayat_pelayanan,data_assesment, id_data))
        conn.commit()
        return redirect(url_for('data_siswa'))

@app.route('/delete/<id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur.execute("DELETE FROM data_siswa WHERE id=%s", (id_data,))
    conn.commit()
    return redirect(url_for('data_siswa'))

@app.route('/tambah_data')
def tambah_data():

    return render_template('tambah_data.html')

@app.route('/edit_data/<id_data>', methods = ['POST', 'GET'])
def edit_data(id_data):
    cur.execute("SELECT * FROM data_siswa WHERE id=%s", (id_data, ))
    data = cur.fetchall()
    print(data)
    return render_template('edit_data.html', datas = data[0])

@app.route('/test')
def test():
    datas = ['data1', 'data2', 'data3', 'data4', 'data5', 'data6', 'data7', 'data8', 'data9', 'data10', 'data11', 'data12', 'data13']
    return render_template('test.html', datas = datas)

