function adivinar_numero(){
    var numero_a_adivinar = Math.floor(Math.random()*1000);
    var bits = 1;
    var numero_usuario = prompt("Adivine un número entero entre 1 y 1000\nIngrese un número entre 1 y 1000: ");

    while (numero_usuario != numero_a_adivinar) {
        if (numero_usuario < numero_a_adivinar) {
            numero_usuario = prompt("Su número es muy bajo!\nIngrese otro número entre 1 y 1000:");
            bits++;
        } else {
            numero_usuario = prompt("Su número es muy alto!\nIngrese otro número entre 1 y 1000:");
            bits++;
        }
    }
    alert("Felicidades el número es " + numero_usuario + " y ha utilizado " + bits + " bits!");
}
