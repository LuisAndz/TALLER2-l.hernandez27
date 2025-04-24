from flask import Blueprint, jsonify, request, render_template
from api.models.perro import Perro
from api.models.gato import Gato
from api.models.huron import Huron
from api.models.boa_constrictor import Boa_Constrictor

animales_bp = Blueprint('animales', __name__)


@animales_bp.route('/animales/<string:animal_buscado>', methods=['GET'])
def como_hace(animal_buscado):

    animal = animal_buscado.lower()

    if animal == "perro":
        animal_inst = Perro("Rufo", "Labrador", 7, 22)
    elif animal == "gato":
        animal_inst = Gato("Michi", "Blanco", 2, 4)
    elif animal == "huron":
        animal_inst = Huron("Hurón Jacinto", 2, 3.9, "Peru", 1.8)
    elif animal == "boa":
        animal_inst = Boa_Constrictor(
            "Boa Paty", 5, 15.2, "Filipinas", 3.2)
    else:
        return jsonify({'animal': animal, 'error': 'no es un animal de la lista'}), 400

    return jsonify({"El animal": animal, "hace": animal_inst.emitir_sonido()})


@animales_bp.route('/', methods=['GET'])
def como_hace_web():
    animal = request.args.get('animal', '').lower()

    if not animal:
        return render_template('animales.html')

    if animal == "perro":
        animal_inst = Perro("Rufo", "Labrador", 7, 22)
    elif animal == "gato":
        animal_inst = Gato("Michi", "Blanco", 2, 4)
    elif animal == "huron":
        animal_inst = Huron("Hurón Jacinto", 2, 3.9, "Peru", 1.8)
    elif animal == "boa":
        animal_inst = Boa_Constrictor("Boa Paty", 5, 15.2, "Filipinas", 3.2)
    else:
        return render_template('animales.html', error="Ese animal no está en la lista.")

    resultado = {
        "El animal": animal,
        "hace": animal_inst.emitir_sonido()
    }
    return render_template('animales.html', resultado=resultado)
