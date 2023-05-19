from flask import Flask, render_template, request, jsonify
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Configurar as credenciais da API do Google Sheets
scope = ['1sr0LpBcmId9bHi6ZOAQYJND6rIzcXinsD-Lo5fe7oGg',
         'AIzaSyA3adiKUy2VSI_mMLl0hLdsJ5COd79FT8w']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'credentials.json', scope)
client = gspread.authorize(credentials)

# Abrir a planilha
sheet = client.open('Desafio 2').sheet1

@app.route('C:\Users\dimir\OneDrive\Ambiente de Trabalho\teste0')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    input_text = data['inputText']
    sheet.append_row([input_text])
    return jsonify({'success': True}), 200

@app.route('/search')
def search():
    row_number = int(request.args.get('rowNumber'))
    result = sheet.cell(row_number, 1).value
    return result

if __name__ == '__main__':
    app.run()
