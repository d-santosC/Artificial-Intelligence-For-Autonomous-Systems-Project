package ambiente; //pacote "ambiente" dentro da pasta src

//interface Ambiente que irá representar o subsistema ambiente onde o agente se encontra
public interface Ambiente {

    //método que define a ação de "evoluir" do ambiente.
    public void evoluir();
    
    //método que retorna um objeto do tipo Evento que representa uma observação do ambiente. 
    public Evento observar();
    
    //método que recebe um objeto do tipo Comando e executa uma ação com base nesse comando no ambiente. 
    public void executar(Comando comando);
}
