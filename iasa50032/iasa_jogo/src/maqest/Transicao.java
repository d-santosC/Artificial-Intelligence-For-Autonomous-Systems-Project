package maqest; //pacote "maqest" dentro da pasta src

import agente.Accao; //import da classe Accao da pasta agente

//classe que representa uma transição de estado na nossa máquina de estados do jogo
public class Transicao {
    private Estado estadoSucessor; //instancia da classe Estado que representa o estado seguinte ao nosso estado atual
    private Accao accao; //instancia da classe Accao que irá representar a ação associada a cada transição

    //construtor da classe onde inicializamos o estado sucessor e a ação associada à transição
    public Transicao(Estado estadoSucessor, Accao accao){
        this.estadoSucessor = estadoSucessor;
        this.accao = accao;
    }

    //getter para obter o estado sucessor após uma transição
    public Estado getEstadoSucessor() {
        return this.estadoSucessor;
        
    }

    //getter para obter a ação associada á transição
    public Accao getAccao() {
        return this.accao;
        
    }

}
