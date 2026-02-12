package jogo.ambiente; //pacote "ambiente" dentro da pasta "jogo"

//import da classe Comando da pasta ambiente
import ambiente.Comando; 

//enumerado ComandoJogo que implementa a interface Controlo da pasta agente
public enum ComandoJogo implements Comando {

    //quatro constantes enumeradas que representam os diferentes comandos possiveis
    PROCURAR, APROXIMAR, OBSERVAR, FOTOGRAFAR;

    //método que imprime o comando em forma de texto
    @Override
    public void mostrar(){
        System.out.printf("Ação: %s\n", this);
    }


}

