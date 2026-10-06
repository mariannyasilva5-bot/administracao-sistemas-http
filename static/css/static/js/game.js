// ============================================================
// ESCOLA NIGHTMARE
// SISTEMA PRINCIPAL DO JOGO
// ============================================================


// ============================================================
// VARIÁVEIS
// ============================================================

let gameRunning = false;

let keysFound = 0;

const TOTAL_KEYS = 8;

let noise = 0;

let monsterAwareness = 0;

let monsterDistance = 100;

let playerX = 50;

let playerY = 50;

let playerSpeed = 0.5;

let flashlight = true;

let lastNoiseTime = 0;

let monsterActive = false;

let gameTime = 0;


// ============================================================
// ELEMENTOS HTML
// ============================================================

const mainMenu =
    document.getElementById("mainMenu");

const game =
    document.getElementById("game");

const startButton =
    document.getElementById("startButton");

const keysFoundElement =
    document.getElementById("keysFound");

const dangerLevelElement =
    document.getElementById("dangerLevel");

const noiseValueElement =
    document.getElementById("noiseValue");

const messageElement =
    document.getElementById("message");

const monster =
    document.getElementById("monster");

const jumpscare =
    document.getElementById("jumpscare");

const deathScreen =
    document.getElementById("deathScreen");

const victoryScreen =
    document.getElementById("victoryScreen");


// ============================================================
// CONTROLES
// ============================================================

const keyboard = {

    w: false,
    a: false,
    s: false,
    d: false

};


document.addEventListener(
    "keydown",
    function(event) {

        const key =
            event.key.toLowerCase();

        if (
            key === "w" ||
            key === "a" ||
            key === "s" ||
            key === "d"
        ) {

            keyboard[key] = true;

        }

        // F = lanterna

        if (key === "f") {

            flashlight =
                !flashlight;

            showMessage(
                flashlight
                    ? "Lanterna ligada."
                    : "Lanterna desligada."
            );

        }

    }
);


document.addEventListener(
    "keyup",
    function(event) {

        const key =
            event.key.toLowerCase();

        if (
            key === "w" ||
            key === "a" ||
            key === "s" ||
            key === "d"
        ) {

            keyboard[key] = false;

        }

    }
);


// ============================================================
// INICIAR
// ============================================================

startButton.addEventListener(
    "click",
    startGame
);


async function startGame() {

    try {

        await fetch(
            "/api/start",
            {
                method: "POST"
            }
        );

    } catch(error) {

        console.error(error);

    }

    mainMenu.style.display =
        "none";

    game.style.display =
        "block";

    gameRunning = true;

    showMessage(
        "Encontre as 8 chaves e escape."
    );

    startAmbience();

    gameLoop();

}


// ============================================================
// MENSAGEM
// ============================================================

function showMessage(text) {

    messageElement.textContent =
        text;

    messageElement.classList.add(
        "show"
    );

    setTimeout(
        function() {

            messageElement.classList.remove(
                "show"
            );

        },
        2500
    );

}


// ============================================================
// MOVIMENTO
// ============================================================

function updatePlayer() {

    if (!gameRunning) {
        return;
    }

    let moving = false;

    if (keyboard.w) {

        playerY -= playerSpeed;

        moving = true;

    }

    if (keyboard.s) {

        playerY += playerSpeed;

        moving = true;

    }

    if (keyboard.a) {

        playerX -= playerSpeed;

        moving = true;

    }

    if (keyboard.d) {

        playerX += playerSpeed;

        moving = true;

    }


    // Impede o jogador de sair da área.

    playerX =
        Math.max(
            5,
            Math.min(
                95,
                playerX
            )
        );

    playerY =
        Math.max(
            5,
            Math.min(
                95,
                playerY
            )
        );


    if (moving) {

        // Andar produz pouco ruído.

        createNoise(
            5
        );

    }

}


// ============================================================
// SISTEMA DE SOM
// ============================================================

function createNoise(amount) {

    noise += amount;

    noise =
        Math.min(
            100,
            noise
        );

    monsterAwareness +=
        amount * 0.7;

    lastNoiseTime =
        Date.now();

}


// ============================================================
// MESAS E CADEIRAS
// ============================================================

document
    .querySelectorAll(".object")
    .forEach(
        function(object) {

            object.addEventListener(
                "click",
                function() {

                    const sound =
                        Number(
                            object.dataset.noise
                        ) || 20;

                    createNoise(
                        sound
                    );

                    showMessage(
                        "Você fez barulho!"
                    );

                    // Pequeno empurrão visual.

                    object.style.transform =
                        "rotate(4deg)";

                    setTimeout(
                        function() {

                            object.style.transform =
                                "";

                        },
                        150
                    );

                }
            );

        }
    );


// ============================================================
// COLETA DE CHAVES
// ============================================================

document
    .querySelectorAll(".key")
    .forEach(
        function(keyElement) {

            keyElement.addEventListener(
                "click",
                async function(event) {

                    event.stopPropagation();

                    if (
                        keyElement.dataset.collected ===
                        "true"
                    ) {

                        return;

                    }

                    const keyID =
                        Number(
                            keyElement.dataset.key
                        );

                    keyElement.dataset.collected =
                        "true";

                    keyElement.style.display =
                        "none";

                    keysFound++;

                    keysFoundElement.textContent =
                        keysFound;

                    unlockGateLock(
                        keysFound
                    );

                    createNoise(
                        3
                    );

                    showMessage(
                        `Chave ${keyID} encontrada!`
                    );


                    try {

                        await fetch(
                            `/api/key/${keyID}`,
                            {
                                method: "POST"
                            }
                        );

                    } catch(error) {

                        console.error(error);

                    }


                    if (
                        keysFound ===
                        TOTAL_KEYS
                    ) {

                        showMessage(
                            "Todas as chaves! Vá até o portão!"
                        );

                    }

                }
            );

        }
    );


// ============================================================
// ABRIR FECHADURA
// ============================================================

function unlockGateLock(index) {

    const lock =
        document.getElementById(
            `lock${index}`
        );

    if (!lock) {
        return;
    }

    lock.textContent =
        "🔓";

    lock.classList.add(
        "open"
    );

}


// ============================================================
// PORTÃO
// ============================================================

document
    .getElementById("gate")
    .addEventListener(
        "click",
        async function() {

            if (
                keysFound <
                TOTAL_KEYS
            ) {

                showMessage(
                    `Ainda faltam ${
                        TOTAL_KEYS - keysFound
                    } chaves.`
                );

                createNoise(
                    20
                );

                return;

            }


            const response =
                await fetch(
                    "/api/gate",
                    {
                        method: "POST"
                    }
                );


            const data =
                await response.json();


            if (data.success) {

                gameRunning =
                    false;

                victoryScreen.style.display =
                    "flex";

            }

        }
    );


// ============================================================
// INTELIGÊNCIA DO MONSTRO
// ============================================================

function updateMonster() {

    if (!gameRunning) {
        return;
    }


    // O monstro não vê o jogador.
    //
    // Ele somente reage ao ruído.
    //
    // Quanto maior o barulho,
    // maior a consciência dele.


    monsterAwareness *=
        0.985;


    // Se a consciência ficar alta,
    // o monstro começa a aparecer.

    if (
        monsterAwareness >
        30
    ) {

        monsterActive =
            true;

    }


    // Se o jogador fizer muito barulho,
    // o monstro se aproxima.

    if (
        monsterAwareness >
        60
    ) {

        monsterDistance -=
            0.5;

    }


    if (
        monsterAwareness >
        90
    ) {

        monsterDistance -=
            1.5;

    }


    monsterDistance =
        Math.max(
            0,
            monsterDistance
        );


    // Atualiza interface.

    updateDangerUI();


    // Monstro suficientemente próximo.

    if (
        monsterDistance <
        20
    ) {

        triggerJumpscare();

    }

}


// ============================================================
// INTERFACE DE PERIGO
// ============================================================

function updateDangerUI() {

    noiseValueElement.textContent =
        Math.round(noise);


    if (
        monsterAwareness <
        20
    ) {

        dangerLevelElement.textContent =
            "BAIXO";

        dangerLevelElement.style.color =
            "#35ff35";

    }

    else if (
        monsterAwareness <
        50
    ) {

        dangerLevelElement.textContent =
            "ATENÇÃO";

        dangerLevelElement.style.color =
            "#ffff00";

    }

    else if (
        monsterAwareness <
        80
    ) {

        dangerLevelElement.textContent =
            "ALTO";

        dangerLevelElement.style.color =
            "#ff8800";

    }

    else {

        dangerLevelElement.textContent =
            "PERIGO";

        dangerLevelElement.style.color =
            "#ff0000";

        document.body.classList.add(
            "danger-effect"
        );

    }

}


// ============================================================
// JUMPSCARE
// ============================================================

let jumpscareTriggered = false;


function triggerJumpscare() {

    if (
        jumpscareTriggered
    ) {

        return;

    }

    jumpscareTriggered =
        true;

    gameRunning =
        false;


    // Mostra monstro.

    monster.classList.add(
        "visible"
    );


    setTimeout(
        function() {

            jumpscare.classList.add(
                "active"
            );

            playScareSound();

        },
        700
    );


    setTimeout(
        async function() {

            try {

                await fetch(
                    "/api/death",
                    {
                        method: "POST"
                    }
                );

            } catch(error) {

                console.error(error);

            }


            jumpscare.classList.remove(
                "active"
            );

            deathScreen.style.display =
                "flex";

        },
        2500
    );

}


// ============================================================
// SOM AMBIENTE
// ============================================================

let ambienceAudio = null;


function startAmbience() {

    try {

        ambienceAudio =
            new Audio(
                "/static/sounds/ambience.mp3"
            );

        ambienceAudio.loop =
            true;

        ambienceAudio.volume =
            0.25;

        ambienceAudio.play()
            .catch(
                function(error) {

                    console.log(
                        "Áudio aguardando interação."
                    );

                }
            );

    } catch(error) {

        console.error(error);

    }

}


// ============================================================
// SOM DO JUMPSCARE
// ============================================================

function playScareSound() {

    try {

        const audio =
            new Audio(
                "/static/sounds/jumpscare.mp3"
            );

        audio.volume =
            1.0;

        audio.play();

    } catch(error) {

        console.error(error);

    }

}


// ============================================================
// PASSAGEM DO TEMPO
// ============================================================

setInterval(
    function() {

        if (!gameRunning) {
            return;
        }

        gameTime++;

        // O ruído diminui lentamente.

        noise *= 0.90;

    },
    1000
);


// ============================================================
// LOOP PRINCIPAL
// ============================================================

function gameLoop() {

    if (!gameRunning) {
        return;
    }


    updatePlayer();

    updateMonster();


    requestAnimationFrame(
        gameLoop
    );

}


// ============================================================
// TECLA E
// PARA INTERAÇÕES FUTURAS
// ============================================================

document.addEventListener(
    "keydown",
    function(event) {

        if (
            event.key.toLowerCase() ===
            "e"
        ) {

            interact();

        }

    }
);


function interact() {

    showMessage(
        "Não há nada para interagir aqui."
    );

}


// ============================================================
// EVENTOS ALEATÓRIOS DE TERROR
// ============================================================

setInterval(
    function() {

        if (!gameRunning) {
            return;
        }


        const chance =
            Math.random();


        if (
            chance <
            0.08
        ) {

            createNoise(
                8
            );

            showMessage(
                "Você ouviu algo no corredor..."
            );

        }

    },
    5000
);
