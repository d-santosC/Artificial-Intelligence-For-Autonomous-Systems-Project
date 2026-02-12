package agente; //pacote "agente" dentro da pasta src

//interface Controlo que define métodos para controlar o comportamento do agente
public interface Controlo {
    
    //método responsável por processar uma percepção recebida e retornar uma ação correspondente.
    public Accao processar(Percepcao percepcao);
}
