from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# ============================================================
# CONFIGURAÇÕES DO JOGO
# ============================================================

TOTAL_KEYS = 8

# Estado inicial do jogo.
# Em uma versão multiplayer, isso precisaria ser separado
# por jogador/sessão.
game_state = {
    "keys_found": 0,
    "gate_locks": 0,
    "game_started": False,
    "game_over": False,
    "victory": False
}


# ============================================================
# MAPA DA ESCOLA
# ============================================================

SCHOOL_ROOMS = [
    {
        "id": "entrada",
        "name": "Entrada Principal",
        "description": "O corredor de entrada da escola."
    },
    {
        "id": "corredor_a",
        "name": "Corredor A",
        "description": "Um corredor escuro cheio de armários."
    },
    {
        "id": "sala_01",
        "name": "Sala 01",
        "description": "Uma sala de aula abandonada."
    },
    {
        "id": "sala_02",
        "name": "Sala 02",
        "description": "As carteiras estão espalhadas pelo chão."
    },
    {
        "id": "biblioteca",
        "name": "Biblioteca",
        "description": "Prateleiras antigas cobrem as paredes."
    },
    {
        "id": "laboratorio",
        "name": "Laboratório",
        "description": "Há equipamentos quebrados sobre as mesas."
    },
    {
        "id": "refeitorio",
        "name": "Refeitório",
        "description": "Longas mesas formam corredores estreitos."
    },
    {
        "id": "ginasio",
        "name": "Ginásio",
        "description": "Um enorme espaço vazio."
    },
    {
        "id": "porao",
        "name": "Porão",
        "description": "Um local extremamente escuro."
    },
    {
        "id": "patio",
        "name": "Pátio",
        "description": "O caminho final até o portão."
    }
]


# ============================================================
# ROTA PRINCIPAL
# ============================================================

@app.route("/")
def index():
    return render_template("index.html")


# ============================================================
# API PARA OBTER O ESTADO DO JOGO
# ============================================================

@app.route("/api/state")
def get_state():
    return jsonify({
        "keys_found": game_state["keys_found"],
        "gate_locks": game_state["gate_locks"],
        "total_keys": TOTAL_KEYS,
        "game_over": game_state["game_over"],
        "victory": game_state["victory"]
    })


# ============================================================
# INICIAR JOGO
# ============================================================

@app.route("/api/start", methods=["POST"])
def start_game():

    game_state["keys_found"] = 0
    game_state["gate_locks"] = 0
    game_state["game_started"] = True
    game_state["game_over"] = False
    game_state["victory"] = False

    return jsonify({
        "success": True,
        "message": "O jogo começou."
    })


# ============================================================
# PEGAR UMA CHAVE
# ============================================================

@app.route("/api/key/<int:key_id>", methods=["POST"])
def collect_key(key_id):

    if key_id < 1 or key_id > TOTAL_KEYS:
        return jsonify({
            "success": False,
            "message": "Chave inválida."
        }), 400

    if game_state["game_over"]:
        return jsonify({
            "success": False,
            "message": "O jogo terminou."
        })

    # A chave coletada aumenta a quantidade encontrada.
    game_state["keys_found"] += 1

    # Cada chave abre uma fechadura.
    game_state["gate_locks"] += 1

    # Evita passar de 8.
    if game_state["keys_found"] > TOTAL_KEYS:
        game_state["keys_found"] = TOTAL_KEYS

    if game_state["gate_locks"] > TOTAL_KEYS:
        game_state["gate_locks"] = TOTAL_KEYS

    return jsonify({
        "success": True,
        "key_id": key_id,
        "keys_found": game_state["keys_found"],
        "gate_locks": game_state["gate_locks"]
    })


# ============================================================
# VERIFICAR PORTÃO
# ============================================================

@app.route("/api/gate", methods=["POST"])
def open_gate():

    if game_state["gate_locks"] < TOTAL_KEYS:

        return jsonify({
            "success": False,
            "message": (
                f"O portão ainda possui "
                f"{TOTAL_KEYS - game_state['gate_locks']} fechaduras."
            )
        })

    game_state["victory"] = True

    return jsonify({
        "success": True,
        "message": "Você conseguiu abrir o portão!"
    })


# ============================================================
# MORTE DO JOGADOR
# ============================================================

@app.route("/api/death", methods=["POST"])
def player_death():

    game_state["game_over"] = True

    return jsonify({
        "success": True,
        "message": "Você foi encontrado."
    })


# ============================================================
# EXECUÇÃO
# ============================================================

if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )

