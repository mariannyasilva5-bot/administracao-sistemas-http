from flask import Flask, render_template_string

app = Flask(__TERROR__)

@app.route("/")
def home():
    return render_template_string("""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Escola do Pesadelo</title>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    scroll-behavior: smooth;
}

body {
    font-family: Arial, sans-serif;
    background: #08080b;
    color: #f5eeee;
}

nav {
    position: sticky;
    top: 0;
    z-index: 10;
    background: #101015;
    padding: 18px 7%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #76202e;
}

.logo {
    color: #e32643;
    font-weight: bold;
    letter-spacing: 2px;
}

nav a {
    color: white;
    text-decoration: none;
    margin-left: 15px;
}

nav a:hover {
    color: #ff536b;
}

.hero {
    min-height: 88vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 35px 20px;
    background:
        linear-gradient(#08080bd9, #08080bf2),
        radial-gradient(ellipse, #54111e, #08080b 70%);
}

.hero-content {
    max-width: 800px;
    animation: entrada 1.2s ease;
}

h1 {
    font-size: clamp(3rem, 9vw, 6rem);
    line-height: 1;
    margin: 25px 0;
}

h1 span {
    color: #e32643;
}

p {
    color: #c9c1c5;
    line-height: 1.8;
    margin: 15px 0;
}

.subtitulo {
    color: #ff6c80;
    letter-spacing: 4px;
    text-transform: uppercase;
}

.btn {
    display: inline-block;
    margin: 8px;
    padding: 13px 22px;
    border: 1px solid #e32643;
    background: #c31632;
    color: white;
    text-decoration: none;
    cursor: pointer;
    font-weight: bold;
    transition: .3s;
}

.btn:hover {
    background: #f02b49;
    transform: translateY(-3px);
    box-shadow: 0 0 20px #e3264366;
}

.btn-secundario {
    background: transparent;
}

section {
    padding: 80px 7%;
}

.titulo {
    text-align: center;
    margin-bottom: 35px;
}

h2 {
    font-size: clamp(2rem, 5vw, 3rem);
    margin: 12px 0;
}

.grade {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 20px;
}

.card {
    padding: 25px;
    background: #15151b;
    border: 1px solid #38252d;
    transition: .3s;
}

.card:hover {
    border-color: #e32643;
    transform: translateY(-5px);
}

.icone {
    font-size: 38px;
}

.card h3 {
    margin: 12px 0;
}

.controles {
    max-width: 800px;
    margin: 30px auto 0;
}

.controle {
    padding: 15px;
    margin: 10px 0;
    background: #15151b;
    border-left: 3px solid #e32643;
}

.jogar {
    text-align: center;
    background: radial-gradient(ellipse, #36101a, #08080b 75%);
}

.painel {
    max-width: 650px;
    margin: auto;
    padding: 35px;
    background: #15151b;
    border: 1px solid #76202e;
}

footer {
    text-align: center;
    padding: 30px;
    background: #050507;
    border-top: 1px solid #38252d;
}

.oculto {
    display: none;
}

#aviso {
    color: #ff7184;
    margin-top: 20px;
}

@keyframes entrada {
    from {
        opacity: 0;
        transform: translateY(25px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@media(max-width: 600px) {
    nav {
        flex-direction: column;
        gap: 15px;
    }

    nav a {
        margin: 5px;
        font-size: 13px;
    }

    section {
        padding: 55px 5%;
    }

    .painel {
        padding: 22px;
    }
}
</style>
</head>

<body>

<nav>
    <div class="logo">☠ ESCOLA DO PESADELO</div>
    <div>
        <a href="#historia">História</a>
        <a href="#regras">Como jogar</a>
        <a href="#jogar">Pode jogar</a>
    </div>
</nav>

<header class="hero">
    <div class="hero-content">
        <div class="subtitulo">Uma experiência de terror</div>

        <h1>ESCOLA DO<br><span>PESADELO</span></h1>

        <p><strong>A última aula nunca termina.</strong></p>

        <p>
            Você ficou preso na escola durante a noite.
            Um professor misterioso está à sua procura.
            Explore os corredores, encontre pistas, resolva
            seis enigmas e tente escapar antes que seja tarde.
        </p>

        <a href="#historia" class="btn">CONHECER O JOGO</a>
        <a href="#regras" class="btn btn-secundario">COMO JOGAR</a>
        <a href="#jogar" class="btn">PODE JOGAR ↓</a>

        <p>⚠ Cuidado com o que se esconde na escuridão.</p>
    </div>
</header>

<section id="historia">
    <div class="titulo">
        <div class="subtitulo">23h47 — Escola abandonada</div>
        <h2>UMA ESCOLA, SEIS CADEADOS</h2>
        <p>
            Você acorda em uma sala escura. As portas estão
            trancadas e não existe ninguém para ajudar.
            Para fugir, será necessário explorar diferentes
            ambientes e descobrir os códigos da saída.
        </p>
    </div>

    <div class="grade">
        <div class="card">
            <div class="icone">🏫</div>
            <h3>Sala de aula</h3>
            <p>Encontre as primeiras pistas do mistério.</p>
        </div>

        <div class="card">
            <div class="icone">📚</div>
            <h3>Biblioteca</h3>
            <p>Livros escondem informações importantes.</p>
        </div>

        <div class="card">
            <div class="icone">🧪</div>
            <h3>Laboratório</h3>
            <p>Resolva enigmas envolvendo números e símbolos.</p>
        </div>

        <div class="card">
            <div class="icone">🔑</div>
            <h3>Sala dos professores</h3>
            <p>Descubra objetos escondidos e novas pistas.</p>
        </div>

        <div class="card">
            <div class="icone">🕯️</div>
            <h3>Porão</h3>
            <p>Um segredo aguarda no lugar mais escuro.</p>
        </div>

        <div class="card">
            <div class="icone">🚪</div>
            <h3>Saída principal</h3>
            <p>Abra os seis cadeados para conquistar a liberdade.</p>
        </div>
    </div>
</section>

<section id="regras">
    <div class="titulo">
        <div class="subtitulo">Manual de sobrevivência</div>
        <h2>COMO JOGAR</h2>
        <p>Use a lógica, observe o cenário e evite ser capturado.</p>
    </div>

    <div class="controles">
        <div class="controle">⌨️ <strong>WASD ou setas:</strong> movimentar o personagem.</div>
        <div class="controle">🔎 <strong>E:</strong> investigar objetos e pistas.</div>
        <div class="controle">🎒 <strong>I:</strong> consultar o inventário.</div>
        <div class="controle">⏸️ <strong>ESC:</strong> pausar o jogo.</div>
    </div>

    <div class="grade" style="margin-top:30px">
        <div class="card">
            <h3>01 — Explore</h3>
            <p>Investigue os ambientes da escola.</p>
        </div>
        <div class="card">
            <h3>02 — Colete</h3>
            <p>Guarde bilhetes, chaves e objetos úteis.</p>
        </div>
        <div class="card">
            <h3>03 — Resolva</h3>
            <p>Descubra as combinações dos seis cadeados.</p>
        </div>
        <div class="card">
            <h3>04 — Escape</h3>
            <p>Fuja antes que o tempo acabe.</p>
        </div>
    </div>
</section>

<section id="jogar" class="jogar">
    <div class="painel">
        <div class="subtitulo">Sua aventura começa aqui</div>
        <h2>PODE JOGAR?</h2>
        <p>
            Você conhece a história. Agora é hora de enfrentar
            o desafio e descobrir se consegue escapar da escola.
        </p>

        <button class="btn" onclick="iniciar()">INICIAR EXPERIÊNCIA</button>

        <p id="aviso" class="oculto">
            A página está pronta! A parte jogável ainda precisa
            ser programada e conectada a este botão.
        </p>
    </div>
</section>

<footer>
    <p><strong>ESCOLA DO PESADELO — A ÚLTIMA AULA</strong></p>
    <p>Projeto educacional de Programação Aplicada.</p>
    <p>Desenvolvido com Python, Flask, HTML, CSS e JavaScript.</p>
</footer>

<script>
function iniciar() {
    document.getElementById("aviso").classList.remove("oculto");
}
</script>

</body>
</html>
""")

if __name__ == "__main__":
    app.run(debug=True)
