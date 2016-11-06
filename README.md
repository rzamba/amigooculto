# Amigo Oculto
Script em python para geração de sorteio de amigo oculto, com geração de arquivos para posterior envio por email para os participantes.

Desenvolvido com Python 2.7.2

## Formato do arquivo csv de participantes sem header (nome,email)

>paulo,paulo@amigo.com </br>
>leticia,leticia@amigo.com </br>
>fabiola,fabiola@amigo.com </br>
>amanda,amanda.zamba@amigo.com </br>
>mariana,mariesaravya@amigo.com </br>


## Comandos

>Lista o Help
>**```$ python amigo_oculto.py -h```**
>
>Sorteio em modo aleatório
>**```$python amigo_oculto.py -a participantes.csv```**
>
>Sorteio com flow contínuo para entrega de presentes
>**```$python amigo_oculto.py -a participantes.csv -m sem_quebra```**
>
> Obs: No modo **-m sem_quebra** a entrega de presente começa por um participante e termina com a entrega do presente para o participante que iniciou, sem quebrar a corrente.

## Resultado do sorteio

>Fica contido no diretorio resultado_sorteio com os arquivos nomeados com os emails que devem ser enviados, ao receber abrindo o arquivo você descobre quem é seu amigo oculto
>
>Exemplo:
>
>Arquivo gerado: **paulo@amigo.com.txt**
>
>Conteúdo do arquivo gerado:   **paulo seu amigo oculto é amanda**