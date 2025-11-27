# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="./assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# FarmTech Solution - IoT Device


## Nome do grupo: Leno's

##  Integrantes: 
- <a href="https://www.linkedin.com/in/leon-gonzalez-8701b9199/">Pablo Leon Dimauro Gonzalez</a>


##  Professores:
### Tutor(a) 
- Ana Cristina Santos</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/andregodoichiovato/">André Godoi</a>


## Descrição

Nesta fase do projeto, realizamos consultas no banco de dados Oracle. Como na fase anterior eu ja havia utilizado o banco de dados para outra atividade, já possuo os dados gravados, conforme mostra imagem abaixo:

<img src="./assets/print_banco_1.png" alt="Print do banco de dados" border="0" width=80% height=40%>

Abaixo segue prints de consultas realizadas nos dados gravados.

O primeiro print exibe a maior temperatura do solo registrada:

<img src="./assets/print_banco_2.png" alt="Print do banco de dados" border="0" width=80% height=40%>

O segundo, mostra a menor temperatura do solo:

<img src="./assets/print_banco_3.png" alt="Print do banco de dados" border="0" width=80% height=40%>

A seguir, temos a media das temperaturas do solo de todos os dados gravados:

<img src="./assets/print_banco_4.png" alt="Print do banco de dados" border="0" width=80% height=40%>

E por fim, uma consulta para exibir os registros onde a umidade do solo é menor que 50%, que no caso da lavoura escolhida (cana-de-açúcar) seria um cenário de escassez hídrica.

<img src="./assets/print_banco_5.png" alt="Print do banco de dados" border="0" width=80% height=40%>

Todos os resultados foram organizados para exibir o ultimo dado gravado.


Um video do funcionamento desta etapa pode ser encontrado em:

https://youtu.be/W8iSZmoJprI

### Dashboard com Streamlit

Como parte da atividade, tambem desenvolvi um dashboard onde podemos visualizar a previsão do tempo para o dia de hoje e recomendação de irrigação de acordo com probabilidade de chuva, como mostra print abaixo:

<img src="./assets/ds_previsao.png" alt="previsao no dashboard">

Logo abaixo, temos o ultimo registro de dados no banco, ou seja, o mais atual:

<img src="./assets/ult_leituras.png" alt="ultimas leituras no dashboard">

A seguir, temos duas caixas de seleção onde podemos filtrar as informações por ids de dispositivos e o modo de visualização, em tabela ou graficos combinados de temperatura e umidade e simples com o pH do solo.

Filtro por id de dispositivo:

<img src="./assets/filtro.png" alt="previsao no dashboard">

Gráfico combinando temperatura e umidade do solo:

<img src="./assets/graf_tempUmid.png" alt="previsao no dashboard">

Gráfico do pH do solo:

<img src="./assets/graf_ph.png" alt="previsao no dashboard">

Visualização em tabela:

<img src="./assets/tabela.png" alt="previsao no dashboard">

Um video demonstrativo do funcionamento do dashboard pode ser encontrado em:

https://youtu.be/-FFcJchI5Fk


## Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>assets</b>: aqui estão os arquivos de imagem para a elaboração deste arquivo.

- <b>scripts</b>: Codigo em Python, realiza operações no banco de dados, comunicação MQTT, consultas a API e geração de alertas com base nos dados recebidos

- <b>src</b>: Código criado para funcionamento do ESP32.
  
- <b>README.md</b>: Este mesmo arquivo, onde é descrito todo o projeto.


## 🗃 Histórico de lançamentos

* 0.1.0 - 14/10/25

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

