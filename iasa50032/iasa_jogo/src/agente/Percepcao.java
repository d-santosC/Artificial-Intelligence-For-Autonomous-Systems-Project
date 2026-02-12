package agente; //pacote "agente" dentro da pasta src
import ambiente.Evento; //import da classe Evento na pasta ambiente

//classe Percepcao que representa uma percepção do ambiente pelo agente
public class Percepcao {

    private Evento evento; //instancia da classe Evento que representa o evento percebido pelo agente

    //construtor da classe Percepcao, que recebe uma instância de Evento como parâmetro
    public Percepcao(Evento evento){
       this.evento = evento;
    }

    //método que retorna o evento percebido
    public Evento getEvento(){
        return this.evento;
    }
}
