package jogo.ambiente; //pacote "ambiente" dentro da pasta "jogo"

//imports das classes Evento, Ambiente e Comando da pasta ambiente
import ambiente.Evento;
import ambiente.Ambiente;
import ambiente.Comando;

//imports das ferramentas necessárias
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

//classe para o ambiente do jogo que evolui no tempo, onde é possível executar e mostrar comandos e eventos, implementa a interface Ambiente
public class AmbienteJogo implements Ambiente {
    
    private Map<String, EventoJogo> eventos; //mapa que atribui as strings para cada instância de EventoJogo
    private Scanner scanner = new Scanner(System.in); //objeto Scanner para receber o evento escolhido pelo utilizador
    private EventoJogo evento; //objeto EventoJogo 

    //construtor da classe, inicializa o mapa "eventos" e preenche-o com os eventos que temos na classe EventoJogo
    public AmbienteJogo(){

        //inicialização dos eventos
        eventos = new HashMap<String, EventoJogo>();
        eventos.put("s", EventoJogo.SILENCIO);
        eventos.put("r", EventoJogo.RUIDO);
        eventos.put("a", EventoJogo.ANIMAL);
        eventos.put("f", EventoJogo.FUGA);
        eventos.put("p", EventoJogo.FOTOGRAFIA);
        eventos.put("t", EventoJogo.TERMINAR);

    }

    //método que irá retornar um evento
    public Evento getEvento(){
        return evento;
    }

    //método que evolui o estado do ambiente de jogo, utilizando um novo evento gerado no método "gerarEvento()"
    public void evoluir(){
        evento = gerarEvento();
    }

    //método que irá mostrar o evento observado e retorna-lo
    public Evento observar(){
        evento.mostrar();
        return evento;
    }

    //método que executa um comando no ambiente de jogo
    public void executar(Comando comando){
        comando.mostrar();
    }

    //método que ira gerar um novo evento no jogo, o utilizador insere um comando que representa o evento desejado
    //sendo estes: (s, r, a, f, p, t)
    private EventoJogo gerarEvento(){
        System.out.println("\nEscolha um evento: ");
        String textoComando = scanner.next();
        return eventos.get(textoComando); //retorna o evento correspondente com base no texto do comando inserido pelo utilizador
    }

}
