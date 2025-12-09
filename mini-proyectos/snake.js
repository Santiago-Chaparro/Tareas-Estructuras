const readline = require("readline");
readline.emitKeypressEvents(process.stdin);
process.stdin.setRawMode(true);

let ancho = 9;
let alto = 9;

let direccion = { x: 1, y: 0 };
let direccionAnterior = { x: 1, y: 0 };

let serpiente = [
    { x: 4, y: 4 },
    { x: 3, y: 4 },
    { x: 2, y: 4 }
];

let comida = { 
    x: Math.floor(Math.random() * ancho), 
    y: Math.floor(Math.random() * alto) 
};

let velocidad = 200;

process.stdin.on("keypress", (str, tecla) => {
    if (tecla && tecla.ctrl && tecla.name === "c") process.exit();

    if (tecla.name === "w" || tecla.name === "up")    direccion = { x: 0, y: -1 };
    if (tecla.name === "s" || tecla.name === "down")  direccion = { x: 0, y: 1 };
    if (tecla.name === "a" || tecla.name === "left")  direccion = { x: -1, y: 0 };
    if (tecla.name === "d" || tecla.name === "right") direccion = { x: 1, y: 0 };
});

function nuevaComida() {
    while (true) {
        let x = Math.floor(Math.random() * ancho);
        let y = Math.floor(Math.random() * alto);
        if (!serpiente.some(p => p.x === x && p.y === y))
            return { x, y };
    }
}

function colisionConSerpiente(cabeza) {
    let prohibido = serpiente[1];

    if (cabeza.x === prohibido.x && cabeza.y === prohibido.y) {
        return false;
    }

    for (let i = 2; i < serpiente.length; i++) {
        if (serpiente[i].x === cabeza.x && serpiente[i].y === cabeza.y)
            return true;
    }
    return false;
}

function actualizar() {
    direccionAnterior = { ...direccion };

    let cabeza = { 
        x: serpiente[0].x + direccion.x, 
        y: serpiente[0].y + direccion.y 
    };

    if (cabeza.x < 0) cabeza.x = ancho - 1;
    if (cabeza.x >= ancho) cabeza.x = 0;
    if (cabeza.y < 0) cabeza.y = alto - 1;
    if (cabeza.y >= alto) cabeza.y = 0;

    serpiente.unshift(cabeza);

    if (cabeza.x === comida.x && cabeza.y === comida.y) {
        comida = nuevaComida();
    } else {
        serpiente.pop();
    }

    if (colisionConSerpiente(cabeza)) {
        console.clear();
        dibujar();
        console.log("COLISIÓN");
        process.exit();
    }

    dibujar();
}

function dibujar() {
    console.clear();
    let salida = "";

    salida += " " + "_".repeat(ancho * 2) + " \n";

    for (let y = 0; y < alto; y++) {
        salida += "|";
        for (let x = 0; x < ancho; x++) {
            let celda = "  ";
            if (serpiente[0].x === x && serpiente[0].y === y) celda = "@ ";
            else if (serpiente.some((p, i) => i !== 0 && p.x === x && p.y === y)) celda = "o ";
            else if (comida.x === x && comida.y === y) celda = "X ";
            salida += celda;
        }
        salida += "|\n";
    }

    salida += "|" + "_".repeat(ancho * 2) + "|\n";

    console.log(salida);
}

dibujar();
setInterval(actualizar, velocidad);
