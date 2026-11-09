
# Q2 Skills Test
from pyscript import display, document

non_metals = {
    "H": {
        "name": "Hydrogen",
        "atomic_number": 1,
        "atomic_mass": 1.008
    },
    "He": {
        "name": "Helium",
        "atomic_number": 2,
        "atomic_mass": 4.0026
    },
    "C": {
        "name": "Carbon",
        "atomic_number": 6,
        "atomic_mass": 12.011
    },
    "N": {
        "name": "Nitrogen",
        "atomic_number": 7,
        "atomic_mass": 14.007
    },
    "O": {
        "name": "Oxygen",
        "atomic_number": 8,
        "atomic_mass": 15.999
    },
    "F": {
        "name": "Fluorine",
        "atomic_number": 9,
        "atomic_mass": 18.998
    },
    "Ne": {
        "name": "Neon",
        "atomic_number": 10,
        "atomic_mass": 20.180
    },
    "P": {
        "name": "Phosphorus",
        "atomic_number": 15,
        "atomic_mass": 30.974
    },
    "S": {
        "name": "Sulfur",
        "atomic_number": 16,
        "atomic_mass": 32.06
    },
    "Cl": {
        "name": "Chlorine",
        "atomic_number": 17,
        "atomic_mass": 35.45
    },
    "Ar": {
        "name": "Argon",
        "atomic_number": 18,
        "atomic_mass": 39.948
    },
    "Se": {
        "name": "Selenium",
        "atomic_number": 34,
        "atomic_mass": 78.971
    },
    "Br": {
        "name": "Bromine",
        "atomic_number": 35,
        "atomic_mass": 79.904
    },
    "Kr": {
        "name": "Krypton",
        "atomic_number": 36,
        "atomic_mass": 83.798
    },
    "I": {
        "name": "Iodine",
        "atomic_number": 53,
        "atomic_mass": 126.90
    },
    "Xe": {
        "name": "Xenon",
        "atomic_number": 54,
        "atomic_mass": 131.29
    },
    "Rn": {
        "name": "Radon",
        "atomic_number": 86,
        "atomic_mass": 222.02
    }
}


def search_element(e):
    symbol = document.getElementById("symbol").value
    symbol = symbol.strip().capitalize()
    element_checker = symbol in non_metals
    display_message = (
        f"Sorry, no {symbol} in the non-metals list.",
        f"{symbol} is in the list!"
    )

    element = non_metals.get(symbol, {})
    document.getElementById("result").innerHTML = f"""
        <div class="result-card">
            <h3>{display_message[element_checker]}</h3>
            <p>Element Symbol: {symbol}</p>
            <p>Element Name: {element.get("name", "N/A")}</p>
            <p>Atomic Number: {element.get("atomic_number", "N/A")}</p>
            <p>Atomic Mass: {element.get("atomic_mass", "N/A")}</p>
        </div>
    """
