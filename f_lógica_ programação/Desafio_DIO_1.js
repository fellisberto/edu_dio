const nomeHeroi = 'TT';
let xpHeroi = 10002;
let nvHeroi;

switch (true) {
	case xpHeroi >= 0 && xpHeroi  <=1000;
		nvHeroi = 'ferro';
		break;
	case xpHeroi >= 1001 && xpHeroi  <=2000;
		nvHeroi = 'bronze';
		break;
	case xpHeroi >= 2001 && xpHeroi  <=5000;
		nvHeroi = 'prata';
		break;
	case xpHeroi >= 5001 && xpHeroi  <=7000;
		nvHeroi = 'ouro';
		break;
	case xpHeroi >= 7001 && xpHeroi  <=8000;
		nvHeroi = 'platina';
		break;
	case xpHeroi >= 8001 && xpHeroi  <=9000;
		nvHeroi = 'Ascendente';
		break;
	case xpHeroi >= 9001 && xpHeroi  <=10000;
		nvHeroi = 'Imortal';
		break;
	case xpHeroi > 10000:
		nvHeroi = 'Radiante';
		break;
	default:
		nvHeroi = 'desconhecido';
	}
	
	console.log('o heroi de nome ${nomeHeroi} está no nível de ${nvHeroi}!');