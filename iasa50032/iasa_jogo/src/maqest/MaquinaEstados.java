package maqest; //pacote "maqest" dentro da pasta src

//imports das classes Accao da pasta agente e de Evento do pacote ambiente
import agente.Accao;
import ambiente.Evento;

//classe que representa o sistema da máquina de estados do jogo

/**
 * Uma máquina de estados é um modelo computacional que descreve o comportamento de um sistema
 * através de um conjunto de estados, transições entre estados e ações associadas a essas transições.
 *
 * Estados representam as condições em que um sistema pode ter.
 * Transições representam as mudanças de estado que ocorrem quando determinados eventos acontecem.
 * Eventos são acontecimentos que levam a transições entre estados, representam mudanças no ambiente ou entrada de dados.
 * Ações são o resultado de uma transição de estado.
 *
 * No contexto do nosso jogo e da nossa máquina de estados, temos os seguintes eventos, estados e ações:
 *
 * Eventos:       Ações:          Estados:
 * -Silencio      -Procurar       -Procura
 * -Ruido         -Aproximar      -Inspeção
 * -Animal        -Observar       -Observação
 * -Fuga          -Fotografar     -Registo
 * -Fotografia
 * -Terminar
 */
public class MaquinaEstados {

    private Estado estado; //estado atual da máquina de estados

    //construtor da classe onde inicializamos a máquina de estados com um estado inicial
    public MaquinaEstados(Estado estadoInicial){
        this.estado = estadoInicial;
    }

    //getter para obtermos o estado atual
    public Estado getEstado() {
        return estado;
    }

    //método para processar um evento e poder fazer uma transição do estado
    public Accao processar(Evento evento){

        Transicao transicao = estado.processar(evento); //obtemos uma transição

        //se houver uma transição, atualizamos o estado atual para o estado sucessor e
        //retornamos a ação associada à transição
        if(transicao != null){
            estado = transicao.getEstadoSucessor();
            return transicao.getAccao();

        } else{
            return null; //se não houver transição para o evento atual, retornamos null
        }
        
    }

}
