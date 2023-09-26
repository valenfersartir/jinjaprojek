from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')

def hello_world():

 orang = {'nama': 'valentino', 'umur':'16thn'}

 komentar = [

  {

   'penulis': {'nama': 'endra'},

   'ucapan': 'hai valentino, artikel yang bagus'

  },

  {

   'penulis': {'nama': 'Gunawan'},

   'ucapan': 'artikel ini cukup membantu saya'

  }

 ]

 return render_template('index.html', title='Beranda', orang=orang, komentar=komentar)