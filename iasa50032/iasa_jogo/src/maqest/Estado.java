package maqest; //pacote "maqest" dentro da pasta src

//imports das ferramentas HashMap e Map
import java.util.HashMap;
import java.util.Map;

//imports das classes Accao da pasta agente e de Evento do pacote ambiente
import agente.Accao;
import ambiente.Evento;

public class Estado {

    private String nome; //nome do estado para melhor identificação
    private Map<Evento, Transicao> transicoes; //mapa de transições, onde a chave é o evento e o valor é a transição

    //construtor da classe onde incializamos o nome e onde é criado o HashMap das transições
    public Estado(String nome){
        this.nome = nome;
        transicoes = new HashMap<Evento, Transicao>();
    }

    //getter para obter o nome do estado em string
    public String getNome(){
        return this.nome;
    }

    //método que retorna as transições a partir de um evento
    public Transicao processar(Evento evento){
        return transicoes.get(evento); 
    }

    /**
     * Para os métodos "transicao" utilizamos uma implementação polimorfica, isto é
     * com o uso do polimorfismo podemos ter vários métodos com o mesmo nome definidos dentro da mesma classe,
     * desde que eles tenham assinaturas diferentes.
     * No caso deste código os seguintes métodos têm parâmetros diferentes.
     */

    //método que chama o método transição para os eventos sem ação
    public Estado transicao(Evento evento, Estado estadoSucessor){
        return transicao(evento, estadoSucessor, null);
    }

    //método que coloca o evento e a transicao no Hashmap "transicoes"
    public Estado transicao(Evento evento, Estado estadoSucessor, Accao accao){
        transicoes.put(evento, new Transicao(estadoSucessor, accao));
        return this;
    }

}
