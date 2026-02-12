package jogo.personagem; //pacote "personagem" dentro da pasta "jogo"

//imports da classe Agente da pasta agente e da classe AmbienteJogo da pasta ambiente dentro da pasta jogo
import agente.Agente;
import jogo.ambiente.AmbienteJogo;

//classe Personagem que irá representar a personagem do jogo, estende a classe Agente
public class Personagem extends Agente {

    //construtor da classe que recebe uma instância de AmbienteJogo como parâmetro e 
    //chama o construtor da classe Agente através do super(), passando como argumentos a instância de ambiente
    //e uma nova instância de ControloPersonagem 
    public Personagem(AmbienteJogo ambiente){
        super(ambiente, new ControloPersonagem());
    }

}
