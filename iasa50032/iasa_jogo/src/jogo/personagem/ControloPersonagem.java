package jogo.personagem; //pacote "personagem" dentro da pasta "jogo"

//imports da classe Accao, Controlo e Percepcao da pasta agente
import agente.Accao;
import agente.Controlo;
import agente.Percepcao;
import ambiente.Evento;
import jogo.ambiente.ComandoJogo;
import jogo.ambiente.EventoJogo;
import maqest.Estado;
import maqest.MaquinaEstados;

//classe responsável pelo controlo da personagem do jogo, implementa a interface Controlo do agente
public class ControloPersonagem implements Controlo{

    private MaquinaEstados maqEst; //maquina de estados
    private Accao accao; //instância da classe Accao
    private Evento evento; //instância da classe Evento

    //construtor da classe onde são definidos os diferentes estados, ações e transições possiveis da personagem
    public ControloPersonagem(){

        //Definição dos possiveis estados
        Estado procura = new Estado("Procura");
        Estado inspeccao = new Estado("Inspecção");
        Estado observacao = new Estado("Observação");
        Estado registo = new Estado("Registo");

        //Definição das ações
        Accao procurar = new Accao(ComandoJogo.PROCURAR);
        Accao aproximar = new Accao(ComandoJogo.APROXIMAR);
        Accao observar = new Accao(ComandoJogo.OBSERVAR);
        Accao fotografar = new Accao(ComandoJogo.FOTOGRAFAR);

        //Definição das transições através de uma DSL (domain-specific language)

        /**
         * No contexto do nosso jogo, quando este se inicia a personagem fica numa situação de procura de animais.
         * Quando detecta algum ruído aproxima-se e fica em inspecção da zona, procurando a fonte do ruído.
         * Quando volta a haver silêncio a personagem volta a uma situação de procura de animais.
         * Quando detecta um animal a personagem aproxima-se e fica em observação. Caso o animal continue presente,
         * a personagem observa o animal e fica preparada para o registo, se ocorrer a fuga do animal
         * a personagem fica em inspecção da zona, à procura de uma fonte de ruído. Na situação de registo,
         * se o animal continuar presente fotografa-o, caso ocorra a fuga do animal ou a personagem
         * tenha conseguido uma fotografia do animal, a personagem fica novamente numa situação de procura.
         */

        //Transições possiveis para o estado procura
        procura
                .transicao(EventoJogo.SILENCIO, procura, procurar)
                .transicao(EventoJogo.ANIMAL, observacao, aproximar)
                .transicao(EventoJogo.RUIDO, inspeccao, aproximar);

        //Transições possiveis para o estado inspeção
        inspeccao
                .transicao(EventoJogo.SILENCIO, procura)
                .transicao(EventoJogo.ANIMAL, observacao, aproximar)
                .transicao(EventoJogo.RUIDO, inspeccao, aproximar);

        //Transições possiveis para o estado observação
        observacao
                .transicao(EventoJogo.FUGA, inspeccao)
                .transicao(EventoJogo.ANIMAL, registo, observar);

        //Transições possiveis para o estado registo
        registo
                .transicao(EventoJogo.FUGA, procura)
                .transicao(EventoJogo.FOTOGRAFIA, procura)
                .transicao(EventoJogo.ANIMAL, registo, fotografar);
        
        //Inicialização da máquina de estados
        maqEst = new MaquinaEstados(procura);

    }
   
    //método que processa uma percepção recebida e retorna uma ação correspondente
    @Override
    public Accao processar(Percepcao percepcao) {

        evento = percepcao.getEvento(); //obtems o evento da percepção

        accao = maqEst.processar(evento); //processamos o evento para determinar a ação

        mostrar(); //mostramos na consola o estado

        return accao; //retornamos a ação atual
    }

    //método que imprime o estado em forma de texto
    private void mostrar(){
        System.out.printf("Estado: %s\n", getEstado().getNome());
    }

    //getter para obter o estado
    public Estado getEstado() {
        return this.maqEst.getEstado();
    }
}
