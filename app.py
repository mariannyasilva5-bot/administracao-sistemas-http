from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Base de dados com as histórias de terror
HISTORIAS = [
    {
        "id": 1,
        "titulo": "A Casa na Colina",
        "categoria": "Lenda Urbana",
        "resumo": "Uma mansão abandonada onde os relógios sempre param às 3:33 da manhã.",
        "conteudo": "A mansão no topo da colina permaneceu vazia por mais de cinquenta anos. Os moradores locais contavam que, exatamente às 3:33 da manhã, luzes pálidas acendiam nas janelas do último andar. Corajosos que tentaram entrar relataram ouvir passos pesados no sótão e sussurros que chamavam seus nomes...",
        "imagem": "https://images.unsplash.com/photo-1509248961158-e54f6934749c?w=600"
    },
    {
        "id": 2,
        "titulo": "O Espelho do Sótão",
        "categoria": "Sobrenatural",
        "resumo": "Um espelho antigo que reflete algo muito diferente da realidade.",
        "conteudo": "Quando Clara comprou o espelho vitoriano em um brechó, não percebeu a gravura oculta na moldura. À noite, ao se olhar no reflexo, sua imagem permanecia imóvel enquanto ela se movia. Na terceira noite, a figura do espelho sorriu e deu um passo em sua direção...",
        "imagem": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=600"
    },
    {
        "id": 3,
        "titulo": "A Floresta dos Sussurros",
        "categoria": "MISTÉRIO",
        "resumo": "Árvores que parecem se mover quando ninguém está olhando.",
        "conteudo": "Nenhum caçador experiente entrava naquela floresta após o pôr do sol. Os poucos que retornaram falavam de vozes familiares chamando do meio da neblina. As árvores mudavam de lugar, trancando os visitantes em um labirinto sem fim...",
        "imagem": "https://images.unsplash.com/photo-1508739773434-c26b3d09e071?w=600"
    }
]

@app.route("/")
def index():
    return render_template("index.html", historias=HISTORIAS)

@app.route("/api/historias")
def api_historias():
    return jsonify(HISTORIAS)

if __name__ == "__main__":
    app.run(debug=True)
