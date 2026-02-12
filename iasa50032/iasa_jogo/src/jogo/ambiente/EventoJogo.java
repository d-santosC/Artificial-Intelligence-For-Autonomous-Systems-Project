package jogo.ambiente; //pacote "ambiente" dentro da pasta "jogo"

//import da classe Evento da pasta ambiente
import ambiente.Evento; 

//enumerado EventoJogo que implementa a interface Evento da pasta agente, aqui serão processados os eventos do nosso jogo
public enum EventoJogo implements Evento {

    //seis constantes enumeradas que representam os diferentes eventos possiveis
    SILENCIO, RUIDO, ANIMAL, FUGA, FOTOGRAFIA, TERMINAR;

    //método que imprime o evento em forma de texto
    @Override
    public void mostrar(){
        System.out.printf("Evento: %s\n", this);
    }


}
