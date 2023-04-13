from flask import Flask, render_template, request, flash, url_for, redirect
from typing import Dict, Optional
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
from flask_login import (
    LoginManager,
    UserMixin,
    current_user,
    login_required,
    login_user,
    logout_user,
)

app = Flask(__name__)

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

def create_akun_siswa(nisn):
    cur.execute("SELECT * FROM data_siswa WHERE nisn = %s", (nisn,))
    data = cur.fetchone()
    default_pwd = 'kanebsanihbos'
    password_hash = generate_password_hash(default_pwd)
    id = data[0]
    cur.execute("INSERT INTO user_login_data (id, password) VALUES (%s, %s)", (id, password_hash))
    conn.commit()

def connect():
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        database = 'smkn1be2_bk',
        password = ''
    )
    # cur = conn.cursor()
    return conn.cur()

@app.route('/')
@login_required
def index():
    if current_user.is_authenticated:
        username = current_user.nama
    return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    if request.method == "POST":        
        database = connect()
        nisn = request.form['nisn']
        password = request.form['password']
        database.execute("SELECT user_login_data.id_user, user_login_data.id, data_siswa.nisn, user_login_data.password, data_siswa.nama FROM user_login_data INNER JOIN data_siswa ON user_login_data.id = data_siswa.id WHERE data_siswa.nisn = %s", (nisn, ))
        data = database.fetchone()
        role = 0
        try:
            user_data(data[1], data[2], data[3], data[4].title(), role)
        except:
            return redirect(request.path)
        user = User.get(str(data[1]))
        if check_password_hash(data[3], password):
            login_user(user)
            return redirect(url_for("index"))
        database.close()
    return render_template('login.html')

@app.route('/login_guru', methods = ['GET', 'POST'])
def login_guru(): 
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    if request.method == "POST":        
        database = connect()   
        no_hp = request.form['no_hp']
        password = request.form['password']
        database.execute("SELECT guru_login_data.id_login_guru, guru_login_data.id_guru, tabel_guru.no_hp, guru_login_data.password, tabel_guru.nama, guru_login_data.role FROM guru_login_data INNER JOIN tabel_guru ON guru_login_data.id_guru = tabel_guru.id_guru WHERE tabel_guru.no_hp = %s", (no_hp, ))
        data = database.fetchone()
        password_hash = generate_password_hash(password)
        try:
            user_data(data[1], data[2], data[3], data[4], data[5])
        except:
            return redirect(request.path)
        user = User.get(str(data[1]))
        if check_password_hash(data[3], password):
            login_user(user)
            return redirect(url_for("index"))
        database.close()
    return render_template('login_guru.html')

@app.route('/pengajar')
@login_required
def pengajar():
    
    return render_template('pengajar.html')

@app.route('/snmptn')
@login_required
def snmptn():
    database = connect()  
    database.execute("SELECT * FROM tabel_snmptn")
    data = database.fetchall()
    database.close()
    return render_template('snmptn.html', students = data)

@app.route('/data_pkl')
@login_required
def data_pkl():
    database = connect() 
    database.execute("SELECT * FROM data_pkl_dan_nilai")
    data = database.fetchall()
    database.close()
    return render_template('data_pkl.html', students = data)

@app.route('/profil')
@login_required
def profil():
    if current_user.role == '1':
        return redirect(url_for("index"))
    else:
        id = current_user.id
        database = connect() 
        database.execute("SELECT * FROM data_siswa WHERE id = %s", (id, ))
        datas = database.fetchone()
        database.close()
    return render_template('profil.html', datas=datas)

@app.route('/profil_guru')
@login_required
def profil_guru():
    if current_user.role == '1':
        database = connect() 
        id = current_user.id
        database.execute("SELECT * FROM tabel_guru WHERE id_guru = %s", (id, ))
        datas = database.fetchone()
        database.execute("SELECT * FROM riwayat_mengajar_guru WHERE id_guru = %s", (id, ))
        riwayat_mengajar_datas = database.fetchall()        
        database.execute("SELECT * FROM riwayat_prestasi_guru WHERE id_guru = %s", (id, ))
        riwayat_prestasi_datas = database.fetchall()
        database.execute("SELECT * FROM bimbingan_kelas_guru WHERE id_guru = %s", (id, ))
        bimbingan_kelas_datas = database.fetchall()
        return render_template('profil_guru.html', datas=datas, riwayat_mengajar_datas=riwayat_mengajar_datas, riwayat_prestasi_datas=riwayat_prestasi_datas, bimbingan_kelas_datas=bimbingan_kelas_datas)
        database.close()
    else:
        return redirect(url_for("index"))

@app.route('/data_siswa', methods = ['GET', 'POST'])
@login_required
def data_siswa():
    database = connect() 
    database.execute("SELECT * FROM data_siswa")
    data = database.fetchall()
    if request.method == 'POST':
        try:
            jurusan = request.form['jurusan']
        except:
            jurusan = None

        try:
            tingkat = request.form['tingkat']
        except:
            tingkat = None

        if jurusan is not None and tingkat is not None :
            database.execute("SELECT * FROM data_siswa WHERE jurusan = %s AND tingkat = %s", (jurusan, tingkat,))
            data = database.fetchall()
            database.close()
            return render_template('data_siswa.html', students = data, jurusan = jurusan, tingkat = tingkat)
        elif tingkat is not None:
            database.execute("SELECT * FROM data_siswa WHERE tingkat = %s", (tingkat,))
            data = database.fetchall()
            database.close()
            return render_template('data_siswa.html', students = data, tingkat = tingkat)
        elif jurusan is not None:
            database.execute("SELECT * FROM data_siswa WHERE jurusan = %s", (jurusan,))
            data = database.fetchall()
            database.close()
            return render_template('data_siswa.html', students = data, jurusan = jurusan)
        else:
            database.close()
            return render_template('data_siswa.html', students = data)
        database.close()
        return render_template('data_siswa.html', students = data)
    database.close()
    return render_template('data_siswa.html', students = data)

@app.route('/insert', methods = ['POST'])
@login_required
def insert():    
    try:        
        database = connect() 
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
            database.execute("INSERT INTO data_siswa (nisn, niss, nama, jenis_kelamin, tempat_lahir, tanggal_lahir, alamat, desa, kecamatan, kabupaten, nama_orangtua, asal_sekolah, tahun_ijazah, keterangan, tingkat, jurusan) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (nisn, niss, nama, jenis_kelamin, tempat_lahir, tanggal_lahir, alamat, desa, kecamatan, kabupaten, nama_orangtua, asal_sekolah, tahun_ijazah, keterangan, kelas, jurusan))
            conn.commit()
            create_akun_siswa(nisn)
            database.close()
            return redirect(url_for('data_siswa'))
    except:
        conn.rollback()
        database.close()
        return redirect(url_for('data_siswa'))
    

@app.route('/update/<id_data>', methods=['POST'])
@login_required
def update(id_data):
    database = connect() 
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
        database.execute("""UPDATE data_siswa 
                    SET nisn=%s, niss=%s, nama=%s, jenis_kelamin=%s, tempat_lahir=%s, tanggal_lahir=%s, alamat=%s, desa=%s, 
                    kecamatan=%s, kabupaten=%s, nama_orangtua=%s, asal_sekolah=%s, tahun_ijazah=%s, keterangan=%s, tingkat=%s, jurusan=%s 
                    WHERE id=%s
                    """, (nisn, niss, nama, jenis_kelamin, tempat_lahir, tanggal_lahir, alamat, desa, kecamatan, kabupaten, nama_orangtua, asal_sekolah, tahun_ijazah, keterangan, kelas, jurusan, id_data))
        conn.commit()
        database.close()
        return redirect(url_for('data_siswa'))

@app.route('/update_snmptn/<id_data>', methods=['POST'])
@login_required
def update_snmptn(id_data):
    database = connect() 
    if request.method == 'POST':
        id_data = id_data
        nama_siswa = request.form['nama_siswa']
        kelas = request.form['kelas']
        program_studi = request.form['program_studi']        
        universitas = request.form['universitas']
        guru_pembimbing = request.form['guru_pembimbing']
        tahun_ajaran = request.form['tahun_ajaran']
        database.execute("""UPDATE tabel_snmptn 
                    SET nama_siswa=%s, kelas=%s, program_studi=%s, universitas=%s, guru_pembimbing=%s, tahun_ajaran=%s
                    WHERE id_snmptn=%s
                    """, (nama_siswa, kelas, program_studi, universitas, guru_pembimbing, tahun_ajaran, id_data))
        conn.commit()
        database.close()
        return redirect(url_for('snmptn'))

@app.route('/update_pkl/<id_data>', methods=['POST'])
@login_required
def update_pkl(id_data):
    database = connect() 
    if request.method == 'POST':
        id_data = id_data
        nama_siswa = request.form['nama_siswa']
        nama_dudi = request.form['nama_dudi']
        alamat_dudi = request.form['alamat_dudi']        
        lamanya = request.form['lamanya']
        predikat = request.form['predikat']
        keterangan = request.form['keterangan']
        kelas = request.form['kelas']
        wali_kelas = request.form['wali_kelas']
        pembimbing = request.form['pembimbing']
        database.execute("""UPDATE data_pkl_dan_nilai 
                    SET nama_siswa=%s, nama_dudi=%s, alamat_dudi=%s, lamanya=%s, predikat=%s, keterangan=%s, kelas=%s, wali_kelas=%s, pembimbing=%s 
                    WHERE id_pkl_dan_nilai=%s
                    """, (nama_siswa, nama_dudi, alamat_dudi, lamanya, predikat, keterangan, kelas, wali_kelas, pembimbing, id_data,))
        conn.commit()
        database.close()
        return redirect(url_for('data_pkl'))

@app.route('/delete/<id_data>', methods = ['GET'])
@login_required
def delete(id_data):
    database = connect() 
    flash("Record Has Been Deleted Successfully")    
    database.execute("DELETE FROM user_login_data WHERE id=%s", (id_data,))
    conn.commit()
    database.execute("DELETE FROM data_siswa WHERE id=%s", (id_data,))
    conn.commit()
    database.close()
    return redirect(url_for('data_siswa'))

@app.route('/delete_snmptn/<id_data>', methods = ['GET'])
@login_required
def delete_snmptn(id_data):
    database = connect() 
    flash("Record Has Been Deleted Successfully")
    database.execute("DELETE FROM tabel_snmptn WHERE id_snmptn=%s", (id_data,))
    conn.commit()
    database.close()
    return redirect(url_for('snmptn'))

@app.route('/delete_pkl/<id_data>', methods = ['GET'])
@login_required
def delete_pkl(id_data):
    database = connect() 
    flash("Record Has Been Deleted Successfully")
    database.execute("DELETE FROM data_pkl_dan_nilai WHERE id_pkl_dan_nilai=%s", (id_data,))
    conn.commit()
    database.close()
    return redirect(url_for('data_pkl'))

@app.route('/tambah_data')
@login_required
def tambah_data():

    return render_template('tambah_data.html')
    
@app.route('/tambah_data_snmptn', methods= ['POST', 'GET'])
@login_required
def tambah_data_snmptn():
    database = connect() 
    if request.method == "POST":
        nama_siswa = request.form['nama_siswa']
        kelas = request.form['kelas']
        program_studi = request.form['program_studi']        
        universitas = request.form['universitas']
        guru_pembimbing = request.form['guru_pembimbing']
        tahun_ajaran = request.form['tahun_ajaran']
        database.execute("INSERT INTO tabel_snmptn (nama_siswa, kelas, program_studi, universitas, guru_pembimbing, tahun_ajaran) VALUES (%s, %s, %s, %s, %s, %s)", (nama_siswa, kelas, program_studi, universitas, guru_pembimbing, tahun_ajaran))
        conn.commit()
        database.close()
        return redirect(url_for('snmptn'))

    return render_template('tambah_data_snmptn.html')

@app.route('/tambah_data_pkl', methods= ['POST', 'GET'])
@login_required
def tambah_data_pkl():
    database = connect() 
    if request.method == "POST":
        nama_siswa = request.form['nama_siswa']
        nama_dudi = request.form['nama_dudi']
        alamat_dudi = request.form['alamat_dudi']        
        lamanya = request.form['lamanya']
        predikat = request.form['predikat']
        keterangan = request.form['keterangan']
        kelas = request.form['kelas']
        wali_kelas = request.form['wali_kelas']
        pembimbing = request.form['pembimbing']
        database.execute("INSERT INTO data_pkl_dan_nilai (nama_siswa, nama_dudi, alamat_dudi, lamanya, predikat, keterangan, kelas, wali_kelas, pembimbing) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (nama_siswa, nama_dudi, alamat_dudi, lamanya, predikat, keterangan, kelas, wali_kelas, pembimbing))
        conn.commit()
        database.close()
        return redirect(url_for('data_pkl'))

    return render_template('tambah_data_pkl.html')

@app.route('/edit_data/<id_data>', methods = ['POST', 'GET'])
@login_required
def edit_data(id_data):
    database = connect() 
    database.execute("SELECT * FROM data_siswa WHERE id=%s", (id_data, ))
    data = database.fetchall()
    database.close()
    return render_template('edit_data.html', datas = data[0])

@app.route('/edit_profil', methods = ['POST', 'GET'])
@login_required
def edit_profil():
    database = connect() 
    id_data = current_user.id
    database.execute("SELECT * FROM data_siswa WHERE id=%s", (id_data, ))
    data = database.fetchall()
    database.close()
    return render_template('edit_data.html', datas = data[0])

@app.route('/edit_profil_guru', methods = ['POST', 'GET'])
@login_required
def edit_profil_guru():
    database = connect() 
    id = current_user.id
    database.execute("SELECT * FROM tabel_guru WHERE id_guru=%s", (id, ))
    data = database.fetchall()
    database.close()
    return render_template('edit_data_guru.html', datas = data[0])

@app.route('/edit_data_snmptn/<id_data>', methods = ['POST', 'GET'])
@login_required
def edit_data_snmptn(id_data):
    database = connect() 
    database.execute("SELECT * FROM tabel_snmptn WHERE id_snmptn=%s", (id_data, ))
    data = database.fetchall()
    database.close()
    return render_template('edit_data_snmptn.html', datas = data[0])


@app.route('/edit_data_pkl/<id_data>', methods = ['POST', 'GET'])
@login_required
def edit_data_pkl(id_data):
    database = connect() 
    database.execute("SELECT * FROM data_pkl_dan_nilai WHERE id_pkl_dan_nilai=%s", (id_data, ))
    data = database.fetchall()
    database.close()
    return render_template('edit_data_pkl.html', datas = data[0])

@app.route('/test', methods=['POST', 'GET'])
def test():
    if request.method == "POST":
        dkv = request.form['checkbox']
        print(dkv)
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

if __name__ == '__main__': 
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run()