# TPC2: Conversor de MD para HTML
#### Autor: José Afonso Lopes Correia, A100610  

## Resumo:
Neste TPC foi pedida a criação em Python de um pequeno conversor de MarkDown(Basic Syntax) para HTML.

### Exemplo de utilização:
```
1. Cabeçalhos:  
    In: # Exemplo  
    Out: <h1>Exemplo</h1> 

2. Negrito:
    In: Este é um **exemplo** 
    Out: Este é um <b>exemplo</b>  

3. Itálico:
    In: Este é um *exemplo* 
    Out: Este é um <i>exemplo</i>     

4. Lista:
    In:
        1. Primeiro item
        2. Segundo item
        3. Terceiro item
    Out:
        <ol>
            <li>Primeiro item</li>
            <li>Segundo item</li>
            <li>Terceiro item</li>
        </ol>

5. Link:
    In: Consulte em [página da UC](http://www.uc.pt)
    Out: Consulte em <a href="http://www.uc.pt">página da UC</a>


6. Imagem: 
    In: Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com)
    Out: Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/>
```