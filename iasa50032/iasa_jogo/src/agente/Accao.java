package agente; //pacote "agente" dentro da pasta src

//import da classe Comando do pacote ambiente
import ambiente.Comando;

//classe Accao que representa uma ação a ser realizada pelo agente
public class Accao {

    private Comando comando; //instância da classe Comando, que representa a ação a ser realizada

    //construtor da classe Accao, que recebe uma instância de Comando como parâmetro
    public Accao(Comando comando){
        this.comando = comando;
    }
    
    //método que retorna o comando associado à ação. 
    public Comando getComando(){
        return this.comando;
    }

}
