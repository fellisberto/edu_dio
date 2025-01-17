class heroi{
	Constructor(nome, idade, tipo){
		this.nome = nome;
		this.idade = idade;
		this.tipo = tipo;
	}
	
	atacar(){
		let ataque;
		
		switch (this.tpo){
			case 'mago':
				ataque = 'magia';
				break;
			case 'guerreiro':
				ataque = 'espada';
				break;
			case 'monge':
				ataque = 'artes marciais';
				break;
			case 'ninja':
				ataque = 'shuriken';
				break;
			default:
				ataque = 'realizou um ataque'
		}
		console.log('O ${this.tipo} atacou usando ${ataque}');
	}	
}

const heroi1 = new heroi'Celes', 33, 'guerreiro');
const heroi2 = new heroi'Stago', 100, 'mago');
const heroi3 = new heroi'Sabin', 22, 'monge');
const heroi4 = new heroi'Shadow', 35, 'ninja');

heroi1.atacar();
heroi2.atacar();
heroi3.atacar();
heroi4.atacar();