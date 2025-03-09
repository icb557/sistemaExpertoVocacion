import unicodedata
from collections import defaultdict

def define_rules(sistemaExperto):
    """Definición de templates para intereses y vocaciones"""

    sistemaExperto.build("""(deftemplate interes (slot tipo)(slot persona)(slot interes))""")
    sistemaExperto.build("""(deftemplate vocacion (slot tipo)(slot persona)(slot vocacion))""")

    """Definición de las reglas del sistema experto vocacional"""

    clips_rules = """
    (defrule ingenieria
    (or  (interes (tipo "interes") (persona ?persona) (interes "matematicas"))
            (interes (tipo "interes") (persona ?persona) (interes "tecnologia")))
    =>
    (assert (vocacion (tipo "vocacion") (persona ?persona) (vocacion "ingenieria")))
    (printout t ?persona " es apto para una carrera en Ingeniería." crlf)
    )

    (defrule computacion
    (or  (interes (tipo "interes") (persona ?persona) (interes "programacion"))
            (interes (tipo "interes") (persona ?persona) (interes "logica")))
    =>
    (assert (vocacion (tipo "vocacion") (persona ?persona) (vocacion "ciencias_computacion")))
    (printout t ?persona " tiene vocación para Ciencias de la Computación." crlf)
    )

    (defrule arte
    (or  (interes (tipo "interes") (persona ?persona) (interes "creatividad"))
            (interes (tipo "interes") (persona ?persona) (interes "diseno")))
    =>
    (assert (vocacion (tipo "vocacion") (persona ?persona) (vocacion "arte_disenio")))
    (printout t ?persona " es apto para una carrera en Arte y Diseño." crlf)
    )

    (defrule salud
    (or  (interes (tipo "interes") (persona ?persona) (interes "ayudar"))
            (interes (tipo "interes") (persona ?persona) (interes "biologia")))
    =>
    (assert (vocacion (tipo "vocacion") (persona ?persona) (vocacion "ciencias_salud")))
    (printout t ?persona " tiene vocación para Ciencias de la Salud." crlf)
    )

    (defrule negocios
    (or  (interes (tipo "interes") (persona ?persona) (interes "liderazgo"))
            (interes (tipo "interes") (persona ?persona) (interes "estrategia")))
    =>
    (assert (vocacion (tipo "vocacion") (persona ?persona) (vocacion "negocios")))
    (printout t ?persona " es apto para una carrera en Negocios y Administración." crlf)
    )
    """
    # Split the rules string into individual constructs
    rules_list = clips_rules.split('\n\n')

    # Build each rule individually
    for rule in rules_list:
        if rule.strip():  # Skip empty lines
            sistemaExperto.build(rule)

def run_inputs(sistemaExperto, intereses, nombreUsuario):
    interesTemplate = sistemaExperto.find_template("interes")
    for interes in intereses:        
        interesTemplate.assert_fact(tipo = 'interes', persona = nombreUsuario, interes = format_interes(interes))
    results = get_results(sistemaExperto)
    sistemaExperto.run()
    sistemaExperto.reset()
    return results

def get_results(sistemaExperto):
    activation_counts = defaultdict(int)  # Use defaultdict for activation counts

    for ac in sistemaExperto.activations():
        activation_counts[ac.name] += 1  # Increment count for each activation

    sorted_activation_counts = sorted(activation_counts.items(), key=lambda item: item[1], reverse=True)

    return sorted_activation_counts

def finish(sistemaExperto):
    sistemaExperto.clear()
    # To delete the 'interes' template:
    sistemaExperto.eval("(undeftemplate interes)")

    # To delete the 'vocacion' template:
    sistemaExperto.eval("(undeftemplate vocacion)")


def format_interes(text):
    return ''.join(c for c in unicodedata.normalize('NFKD', text) if not unicodedata.combining(c)).lower()

    
