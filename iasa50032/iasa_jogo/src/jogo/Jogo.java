package jogo; //pacote "jogo"

//imports das classes AmbienteJogo e EventoJogo da pasta ambiente dentro da pasta jogo e da classe Personagem da pasta personagem
import jogo.ambiente.AmbienteJogo;
import jogo.ambiente.EventoJogo;
import jogo.personagem.Personagem;

//classe principal do jogo, onde este será incializado e executado
public class Jogo {

    private static Personagem personagem; //instância estática da classe Personagem
    private static AmbienteJogo ambiente; //instância estática da classe AmbienteJogo

    //método principal que inicializa e executa o nosso ambiente do jogo com a personagem
    public static void main(String[] args) {
        ambiente = new AmbienteJogo();
        personagem =  new Personagem(ambiente);
        executar();
    }

    //método que é responsável por executar o jogo
    public static void executar(){
        //loop "do-while" que realiza as ações enquanto o evento no ambiente for diferente de "TERMINAR"
        //utilizamos um "do-while" em vez de um "while" porque realizamos a definição do ambiente do jogo antes de podermos fazer a condição
        do{
            ambiente.evoluir(); //o ambiente evolui com um novo evento
            personagem.executar(); //personagem executa uma ação

        }while(ambiente.getEvento() != EventoJogo.TERMINAR);
    }
}
