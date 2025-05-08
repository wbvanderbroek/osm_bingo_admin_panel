from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

bingo_elements = [
    {
        'id': 0,
        'name': 'Het Kasteel',
        'description': 'Maak een foto van het Kasteel met je groepje.',
        'latitude': 53.21774270053335,
        'longitude': 6.555017571423083
    },
    {
        'id': 1,
        'name': 'Forum Groningen',
        'description': 'Maak een selfie/foto op het dak van het Forum met je groepje.',
        'latitude': 53.21893636399295,
        'longitude': 6.570391954630532
    },
    {
        'id': 2,
        'name': 'Martinitoren',
        'description': 'Maak een foto van de Martinitoren met de grootste persoon uit je groepje ernaast.',
        'latitude': 53.21938568974004,
        'longitude': 6.568207623222464
    },
    {
        'id': 3,
        'name': 'Nieuwe Kerk',
        'description': 'Maak een foto in de Nieuwe Kerk of voor de hoofdingang met je groepje.',
        'latitude': 53.223280467862814,
        'longitude': 6.561681503979227
    },
    {
        'id': 4,
        'name': 'Groninger Museum',
        'description': 'Maak een foto van het Groninger Museum waarin een of meerdere leden van je groepje een kunstwerk na doen, geef ook aan welk kunstwerk je na doet. Het hoeft niet van dit museum te zijn.',
        'latitude': 53.21228190017462,
        'longitude': 6.566079351512879
    },
    {
        'id': 5,
        'name': 'Akerk',
        'description': 'Maak een foto in de Akerk of voor de hoofdingang met je groepje.',
        'latitude': 53.216492401093994,
        'longitude': 6.562364669840671
    },
    {
        'id': 6,
        'name': 'Station Groningen',
        'description': 'Maak een foto bij het paarden standbeeld bij het stations gebouw.',
        'latitude': 53.211020494728324,
        'longitude': 6.564063342704337
    },
    {
        'id': 7,
        'name': 'MartiniPlaza',
        'description': 'Maak een foto met je groepje met het Martiniplaza in de achtergrond.',
        'latitude': 53.20303240513857,
        'longitude': 6.555081707361252
    },
    {
        'id': 8,
        'name': 'Noorderpoort Kunst & Multimedia',
        'description': 'Maak een foto van je groepje met het Noorderpoort logo.',
        'latitude': 53.207594630285534,
        'longitude': 6.557172995605856
    },
    {
        'id': 9,
        'name': 'Kinderboerderij Stadspark',
        'description': 'Maak een foto per persoon met hun favoriete dier.',
        'latitude': 53.20606466399597,
        'longitude': 6.547321014823603
    },
    {
        'id': 10,
        'name': 'Skatepark De Paardenbak',
        'description': 'Maak een foto met je groepje op het skatepark.',
        'latitude': 53.20415683364296,
        'longitude': 6.5478241337411
    },
    {
        'id': 11,
        'name': 'Groningen Atletiek',
        'description': 'Maak een foto op de baan, als de baan dicht is maak een foto van de ingang.',
        'latitude': 53.198871227315074,
        'longitude': 6.539539240983704
    },
    {
        'id': 12,
        'name': 'Noorderpoort Technologie & ICT',
        'description': 'Maak een foto van iemand uit je groepje met hun coach.',
        'latitude': 53.20329518505192,
        'longitude': 6.562301116096836
    },
    {
        'id': 13,
        'name': 'Pepergasthuis',
        'description': 'Maak een foto van je groepje in het Pepergasthuis als het open is, maak anders buiten een foto.',
        'latitude': 53.21742607496547,
        'longitude': 6.57141301267729
    },
    {
        'id': 14,
        'name': 'Rijksuniversiteit Groningen',
        'description': 'Maak een foto van je groepje bij de ingang van het Rijksuniversiteit.',
        'latitude': 53.21920524542988,
        'longitude': 6.563175805756274
    },
    {
        'id': 15,
        'name': 'Noorderplantsoen',
        'description': 'Maak een foto met je hele groepje bij een van de bankjes in het Noorderplantsoen.',
        'latitude': 53.22421158564376,
        'longitude': 6.555581019774128
    },
    {
        'id': 16,
        'name': 'McDonald\'s Westerhaven',
        'description': 'Maak een foto van een vuilnisbak met een McDonalds logo erop.',
        'latitude': 53.21619848026004,
        'longitude': 6.557473848143307
    },
    {
        'id': 17,
        'name': 'McDonald\'s Herestraat',
        'description': 'Maak een foto van het McDonalds bord.',
        'latitude': 53.21652939251069,
        'longitude': 6.567871745345571
    },
    {
        'id': 18,
        'name': 'McDonald\'s Sontplein',
        'description': 'Maak een foto van de McDonalds van de andere kant van de parkeerplaats.',
        'latitude': 53.216157759482684,
        'longitude': 6.584330600549564
    },
    {
        'id': 19,
        'name': 'KFC Westerkade',
        'description': 'Maak een foto met van iemand in je groepje met Colonel Sanders.',
        'latitude': 53.21524576553252,
        'longitude': 6.557393169762863
    },
    {
        'id': 20,
        'name': 'Prinsentuin',
        'description': 'Maak een foto met je groepje in de prinsjes tuin.',
        'latitude': 53.2213457069883,
        'longitude': 6.568897712273988
    },
    {
        'id': 21,
        'name': 'Voormalige Draftbaan Stadspark',
        'description': 'Maak een foto van de drafbaan met je groepje.',
        'latitude': 53.20349208509578,
        'longitude': 6.5491170434165795
    },
    {
        'id': 22,
        'name': 'Domino\'s Pizza Paterswoldseweg',
        'description': 'Maak een foto van het Domino’s bord.',
        'latitude': 53.203118573549695,
        'longitude': 6.559126479689959
    },
    {
        'id': 23,
        'name': '\'t Pannekoekschip',
        'description': 'Maak een foto van ‘t Pannekoekschip met iemand van je groepje.',
        'latitude': 53.21695900180443,
        'longitude': 6.579041728818073
    },
    {
        'id': 24,
        'name': 'Boteringebrug',
        'description': 'Maak een foto van je groepje met het kanaal in de achtergrond.',
        'latitude': 53.22132573050829,
        'longitude': 6.562735226033523
    }
]


@app.route('/api/bingo', methods=['GET'])
def get_bingo_elements():
    return jsonify(bingo_elements)


@app.route('/api/bingo/<int:id>', methods=['PUT'])
def update_bingo_element(id):
    updated_element = request.get_json()
    for element in bingo_elements:
        if element['id'] == id:
            element.update(updated_element)
            return jsonify(element)
    return jsonify({'error': 'Element not found'}), 404

@app.route('/api/bingo/<int:id>', methods=['DELETE'])
def delete_bingo_element(id):
    global bingo_elements
    bingo_elements = [e for e in bingo_elements if e['id'] != id]
    return jsonify({'message': 'Element deleted'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
