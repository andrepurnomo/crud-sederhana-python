# Import library dari flask
# Biar bisa dipake di file server.py
from flask import Flask, request
import mariadb

# Buat class flask dan simpan di variabel app
app = Flask(__name__)
# ? 1. Koneksi Database
# MULAI KONEKSI DATABASE
try:
    conn = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=3306,
        database="belajar"
    )
    print('Berhasil koneksi database')
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
# SELESAI KONEKSI DATABASE


@app.route("/")  # Bikin url di flask dengan alamat /
def run():
    return "<p>Aplikasi Flask sudah jalan!</p>"


# START INPUT KARYAWAN
@app.route('/karyawan', methods=['POST'])  # ? 2. Input data ke tabel database
def input_karyawan():
    data = request.get_json()
    # data = {"name": "jokowi", "phone": "321", "note": "HOHO"}
    cur = conn.cursor()
    cur.execute(
        'insert into karyawan (name,phone,note) values ("{}", "{}", "{}")'.format(data['name'], data['phone'], data['note']))
    conn.commit()
    return 'Berhasil input'
# SELESAI INPUT KARYAWAN


@app.route('/karyawan', methods=['GET'])  # ? 3. Baca data dari tabel database
def baca_karyawan():
    cur = conn.cursor()
    cur.execute('select * from karyawan')

    # PERULANGAN DAN SIMPAN DATA KE RESULT
    result = []
    for id, name, phone, note in cur:
        result.append({
            "id": id,
            "name": name,
            "phone": phone,
            "note": note,
        })

    return result


@app.route('/karyawan', methods=['PUT'])  # ? 4. Edit data dari tabel database
def edit_karyawan():
    data = request.get_json()
    cur = conn.cursor()
    cur.execute(
        'update karyawan set name = "{}", phone = "{}", note = "{}" where id = {}'.format(data['name'], data['phone'], data['note'], data["id"]))
    conn.commit()

    return 'Data berhasil dirubah'


# ? 5. Hapus data dari tabel database
@app.route('/karyawan/<int:id_karyawan>', methods=['DELETE'])
def hapus_karyawan(id_karyawan):
    data = request.get_json()
    cur = conn.cursor()
    cur.execute('delete from karyawan where id = {}'.format(id_karyawan))
    conn.commit()

    return 'Data berhasil hapus'

# SRY HEADSET NYA HABIS BATRE
# UNTUK SEMENTARA HARI INI SAMPAI SINI DULU AJA YA
# NEXT KODING SAYA UPLOAD DULU DI GITHUB
# YANG BELUM PAHAM MANA FUNCTION ATAU LOGIKA NYA BISA TANYA
