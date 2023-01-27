import psycopg2

from app import app
from flask import Flask, render_template, request, flash, url_for, redirect

# konfigurasi database
conn = psycopg2.connect(host="localhost", database="sistem_informasi_siswa", user="postgres", password="123456")
cur = conn.cursor()

@app.route('/')
def index():

    return render_template('index.html')


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
        flash("Data Inserted Sucessfully")
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
        cur.execute("INSERT INTO data_siswa (nisn, niss, nama, tanggal_lahir, tempat_lahir, alamat, jenis_kelamin, nama_orangtua, asal_sekolah, tahun_ijazah) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (nisn, niss, nama, tanggal_lahir, tempat_lahir, alamat, jenis_kelamin, nama_orangtua, asal_sekolah, tahun_ijazah))
        conn.commit()

        return redirect(url_for('index'))


# Update
@app.route('/update', methods=['POST','GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
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
        cur.execute("""UPDATE data_siswa 
                    SET nisn=%s, niss=%s, nama=%s, tanggal_lahir=%s, tempat_lahir=%s, alamat=%s,
                    jenis_kelamin=%s, nama_orangtua=%s, asal_sekolah=%s, tahun_ijazah=%s 
                    WHERE id=%s
                    """, (nisn,niss,nama,tanggal_lahir,tempat_lahir,alamat,jenis_kelamin,
                    nama_orangtua,asal_sekolah,tahun_ijazah, id_data))
        flash("Data Updated Successfully")
        conn.commit()
        return redirect(url_for('index'))

@app.route('/delete/<id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur.execute("DELETE FROM data_siswa WHERE id=%s", (id_data,))
    conn.commit()
    return redirect(url_for('index'))



@app.route('/test')
def test():
    datas = ['data1', 'data2', 'data3', 'data4', 'data5', 'data6', 'data7', 'data8', 'data9', 'data10', 'data11', 'data12', 'data13']
    return render_template('test.html', datas = datas)

