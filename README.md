# amigooculto
Script em python para geração de sorteio de amigo oculto

## Formato do arquivo csv de participantes (nome,email sem header)

>rubens,rubens@corp.globo.com
>dudu,eduprojetos10@gmail.com
>leticia,leticia.ribeiro@maededeus.com.br
>fabiola,fabiola.oliver@globo.com
>amanda,amanda.zamba@gmail.com
>mariana,mariesaravya@gmail.com


## Comandos

Lista o Help
```$ python amigo_oculto.py -h```

Executa o sorteio em modo aleatório
```$python amigo_oculto.py -a participantes.csv```

Executa o sorteio em modo lista circular (flow contínuo para entrega de presentes)
```$python amigo_oculto.py -a participantes.csv -m sem_quebra```

## Resultado do sorteio

Fica contido no diretorio resultado_sorteio com os arquivos nomeados com os emails que devem ser enviados, ao receber abrindo o arquivo você descobre quem é seu amigo oculto

Exemplo:

Arquivo gerado: **paulo@amigo.com.txt**

Conteúdo do arquivo gerado:   **paulo seu amigo oculto é amanda**