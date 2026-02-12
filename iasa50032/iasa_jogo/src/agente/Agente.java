package agente; //pacote "agente" dentro da pasta src

//imports das classes Ambiente e Evento do pacote ambiente
import ambiente.Ambiente;
import ambiente.Evento;

//classe Agente no pacote agente que irá representar o subsistema agente
public class Agente {

    private Controlo controlo; //instância da classe Controlo, que irá controlar o comportamento do agente
    private Ambiente ambiente; //instância da interface Ambiente que irá representar o ambiente em que o agente age

    //construtor da classe que recebe uma instância de Ambiente e uma instância de Controlo
    //inicializa os atributos ambiente e controlo com os valores recebidos como parâmetros
    public Agente(Ambiente ambiente, Controlo controlo) {
        this.controlo = controlo;
        this.ambiente = ambiente;
    }
    //método responsável por obter a percepção do ambiente pelo agente
    //invoca o método observar() do ambiente para obter um evento e cria uma nova instância de Percepcao com esse evento. 
    protected Percepcao percepcionar() {
        Evento evento = ambiente.observar();
        return new Percepcao(evento);
    }

    //método que recebe uma instância de Accao como parâmetro e atua com base nessa ação
    //se a ação não for nula, ele extrai o comando da ação com accao.getComando(), 
    //e então chama o método executar() do ambiente, passando esse comando como argumento
    //o agente executa uma ação no ambiente com base na Accao recebida
    protected void actuar(Accao accao) {
        if(accao != null){
            ambiente.executar(accao.getComando());
        }
    }

    //metodo responsavel  por executar o agente

    /**
     *O metodo executar foi feito de acordo com o UML, sendo que este contém os estados percepcionar, processar e actuar.
     * No UML podem ser observadas duas partições (agente, controlo), isto é, duas áreas que associam os comportamentos a determinadas partes do sistemas
     */
    public void executar(){
        Percepcao p = percepcionar(); //criar uma nova percepção e guardar numa variavel

        //esta variavel vai ser utilizada no metodo processar da classe ControloPersonagem, para a percepção ser interpretada e retornar uma ação do agente
        Accao accao = controlo.processar(p); 
        actuar(accao);                                    
    }
}
