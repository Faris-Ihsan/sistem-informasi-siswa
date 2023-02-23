import psycopg2

from app import app
from flask import Flask, render_template, request, flash, url_for, redirect
from typing import Dict, Optional
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import (
    LoginManager,
    UserMixin,
    current_user,
    login_required,
    login_user,
    logout_user,
)

login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = "login"

users: Dict[str, "User"] = {}

class User(UserMixin):
    def __init__(self, id: str, username: str, password: str,  nama: str, role:str):
        self.id = id
        self.username = username
        self.password = password
        self.nama = nama
        self.role = role
    
    @staticmethod
    def get(user_id: str) -> Optional["User"]:
        return users.get(user_id)

    def __str__(self) -> str:
        return f"<Id: {self.id}, Username: {self.username}, Nama: {self.nama}, Role: {self.role}>"

    def __repr__(self) -> str:
        return self.__str__()

def user_data(id, username, password, nama, role):
    key = str(id)
    users[key] = User(
            id=id,
            username= str(username),
            password=str(password),
            nama=str(nama),
            role=str(role)
        )

@login_manager.user_loader
def load_user(user_id: str):
    return User.get(user_id)

# konfigurasi database
conn = psycopg2.connect(host="localhost", database="sistem_informasi_siswa", user="postgres", password="123456")
cur = conn.cursor()

@app.route('/')
def index():
    if current_user.is_authenticated:
        username = current_user.nama
    return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        nisn = request.form['nisn']
        password = request.form['password']
        cur.execute("SELECT user_login_data.id_user, user_login_data.id, user_login_data.nisn, user_login_data.password, data_siswa.nama FROM user_login_data INNER JOIN data_siswa ON user_login_data.nisn = data_siswa.nisn WHERE user_login_data.nisn = %s", (nisn, ))
        data = cur.fetchone()
        role = 0
        # print(data[0])
        # password_hash = generate_password_hash(password)
        try:
            user_data(data[1], data[2], data[3], data[4].title(), role)
        except:
            return redirect(request.path)
        user = User.get(str(data[1]))
        if check_password_hash(data[3], password):
            login_user(user)
            return redirect(url_for("index"))
    return render_template('login.html')

@app.route('/login_guru', methods = ['GET', 'POST'])
def login_guru():
    if request.method == "POST":
        no_hp = request.form['no_hp']
        password = request.form['password']
        cur.execute("SELECT * FROM guru_login_data WHERE no_hp = %s", (no_hp, ))
        data = cur.fetchone()
        print(data[0], data[2], data[3], data[2].title(), data[4])
        password_hash = generate_password_hash(password)
        try:
            user_data(data[0], data[2], data[3], data[1].title(), data[4])
        except:
            return redirect(request.path)
        user = User.get(str(data[0]))
        if check_password_hash(data[3], password):
            login_user(user)
            return redirect(url_for("index"))
    return render_template('login_guru.html')

@app.route('/pengajar')
def pengajar():

    return render_template('pengajar.html')

@app.route('/snmptn')
def snmptn():
    cur.execute("SELECT * FROM tabel_snmptn")
    data = cur.fetchall()

    return render_template('snmptn.html', students = data)

@app.route('/profil')
@login_required
def profil():
    if current_user.role == '1':
        return redirect(url_for("index"))
    else:
        id = current_user.id
        cur.execute("SELECT * FROM data_siswa WHERE id = %s", (id, ))
        datas = cur.fetchone()
        print(id)
        print(datas)    
        # cur.execute("SELECT * FROM data_siswa WHERE id=%s", (id_data, )")
    return render_template('profil.html', datas=datas)

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
    cur.execute("SELECT * FROM data_siswa")
    data = cur.fetchall()

    return render_template('data_siswa.html', students = data)

# Create 
@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        nisn = request.form['nisn']
        niss = request.form['niss']
        nama = request.form['nama']        
        jenis_kelamin = request.form['jenis_kelamin']
        tempat_lahir = request.form['tempat_lahir']
        tanggal_lahir = request.form['tanggal_lahir']
        alamat = request.form['alamat']
        desa = request.form['desa']
        kecamatan = request.form['kecamatan']
        kabupaten = request.form['kabupaten']
        nama_orangtua = request.form['nama_orangtua']
        asal_sekolah = request.form['asal_sekolah']
        tahun_ijazah = request.form['tahun_ijazah']
        keterangan = request.form['keterangan']
        kelas = request.form['kelas']
        jurusan = request.form['jurusan']
        a = [nisn, niss, nama, jenis_kelamin, tempat_lahir, tanggal_lahir, alamat, desa, kecamatan, kabupaten, nama_orangtua, asal_sekolah, tahun_ijazah, keterangan, kelas, jurusan]
        print(a)
        cur.execute("INSERT INTO data_siswa (nisn, niss, nama, jenis_kelamin, tempat_lahir, tanggal_lahir, alamat, desa, kecamatan, kabupaten, nama_orangtua, asal_sekolah, tahun_ijazah, keterangan, tingkat, jurusan) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (nisn, niss, nama, jenis_kelamin, tempat_lahir, tanggal_lahir, alamat, desa, kecamatan, kabupaten, nama_orangtua, asal_sekolah, tahun_ijazah, keterangan, kelas, jurusan))
        conn.commit()

        return redirect(url_for('data_siswa'))

# Update
@app.route('/update/<id_data>', methods=['POST'])
def update(id_data):
    if request.method == 'POST':
        nisn = request.form['nisn']
        niss = request.form['niss']
        nama = request.form['nama']        
        jenis_kelamin = request.form['jenis_kelamin']
        tempat_lahir = request.form['tempat_lahir']
        tanggal_lahir = request.form['tanggal_lahir']
        alamat = request.form['alamat']
        desa = request.form['desa']
        kecamatan = request.form['kecamatan']
        kabupaten = request.form['kabupaten']
        nama_orangtua = request.form['nama_orangtua']
        asal_sekolah = request.form['asal_sekolah']
        tahun_ijazah = request.form['tahun_ijazah']
        keterangan = request.form['keterangan']
        kelas = request.form['kelas']
        jurusan = request.form['jurusan']
        cur.execute("""UPDATE data_siswa 
                    SET nisn=%s, niss=%s, nama=%s, jenis_kelamin=%s, tempat_lahir=%s, tanggal_lahir=%s, alamat=%s, desa=%s, 
                    kecamatan=%s, kabupaten=%s, nama_orangtua=%s, asal_sekolah=%s, tahun_ijazah=%s, keterangan=%s, tingkat=%s, jurusan=%s 
                    WHERE id=%s
                    """, (nisn, niss, nama, jenis_kelamin, tempat_lahir, tanggal_lahir, alamat, desa, kecamatan, kabupaten, nama_orangtua, asal_sekolah, tahun_ijazah, keterangan, kelas, jurusan, id_data))
        conn.commit()
        return redirect(url_for('data_siswa'))

@app.route('/update_snmptn/<id_data>', methods=['POST'])
def update_snmptn(id_data):
    if request.method == 'POST':
        id_data = id_data
        nama_siswa = request.form['nama_siswa']
        kelas = request.form['kelas']
        program_studi = request.form['program_studi']        
        universitas = request.form['universitas']
        guru_pembimbing = request.form['guru_pembimbing']
        tahun_ajaran = request.form['tahun_ajaran']
        cur.execute("""UPDATE tabel_snmptn 
                    SET nama_siswa=%s, kelas=%s, program_studi=%s, universitas=%s, guru_pembimbing=%s, tahun_ajaran=%s
                    WHERE id_snmptn=%s
                    """, (nama_siswa, kelas, program_studi, universitas, guru_pembimbing, tahun_ajaran, id_data))
        conn.commit()
        return redirect(url_for('snmptn'))

@app.route('/delete/<id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur.execute("DELETE FROM data_siswa WHERE id=%s", (id_data,))
    conn.commit()
    return redirect(url_for('data_siswa'))

@app.route('/delete_snmptn/<id_data>', methods = ['GET'])
def delete_snmptn(id_data):
    flash("Record Has Been Deleted Successfully")
    cur.execute("DELETE FROM tabel_snmptn WHERE id_snmptn=%s", (id_data,))
    conn.commit()
    return redirect(url_for('snmptn'))

@app.route('/tambah_data')
def tambah_data():

    return render_template('tambah_data.html')
    
@app.route('/tambah_data_snmptn', methods= ['POST', 'GET'])
def tambah_data_snmptn():
    if request.method == "POST":
        nama_siswa = request.form['nama_siswa']
        kelas = request.form['kelas']
        program_studi = request.form['program_studi']        
        universitas = request.form['universitas']
        guru_pembimbing = request.form['guru_pembimbing']
        tahun_ajaran = request.form['tahun_ajaran']
        cur.execute("INSERT INTO tabel_snmptn (nama_siswa, kelas, program_studi, universitas, guru_pembimbing, tahun_ajaran) VALUES (%s, %s, %s, %s, %s, %s)", (nama_siswa, kelas, program_studi, universitas, guru_pembimbing, tahun_ajaran))
        conn.commit()
        return redirect(url_for('snmptn'))

    return render_template('tambah_data_snmptn.html')

@app.route('/edit_data/<id_data>', methods = ['POST', 'GET'])
def edit_data(id_data):
    cur.execute("SELECT * FROM data_siswa WHERE id=%s", (id_data, ))
    data = cur.fetchall()
    print(data)
    return render_template('edit_data.html', datas = data[0])

@app.route('/edit_data_snmptn/<id_data>', methods = ['POST', 'GET'])
def edit_data_snmptn(id_data):
    cur.execute("SELECT * FROM tabel_snmptn WHERE id_snmptn=%s", (id_data, ))
    data = cur.fetchall()
    return render_template('edit_data_snmptn.html', datas = data[0])

@app.route('/test')
def test():

    return render_template('test.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/settings")
@login_required
def settings():
    return "<h1>Route protected</h1>"

