function nvRank(vitorias, derrotas){
	let saldoVitorias = vitorias - derrotas;
	let nivel;
	
	if (saldoVitorias < 10){
		nivel = "ferro";
	} else if (saldoVitorias > 11 && saldoVitorias <= 20){
		nivel = "bronze";
	} else if (saldoVitorias > 21 && saldoVitorias <= 50){
		nivel = "prata";
	} else if (saldoVitorias > 51 && saldoVitorias <= 80){
		nivel = "ouro";
	} else if (saldoVitorias > 81 && saldoVitorias <= 90){
		nivel = "diamante";
	} else if (saldoVitorias > 91 && saldoVitorias <= 10){
		nivel = "lendario";
	}else {
			nivel = "imortal"
	}
	
	return 'O herói tem um saldo de ${saldoVitorias} está no nivel de ${nivel}!';
}

let vitorias = 120;
let derrotas = 10

const resultado = nvRank(vitorias, derrotas);
console.log(resultado);