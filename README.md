# Projeto Mayday - Sistema fase 3  

Para testar o webapp utilize os arquivos:<br>
  individuo_saudavel.txt<br>
  individuo_infectado.txt.<br><br>
Modelo de regressão logística para conjunto de espectro em intensidade de superficie aprimorada.<br></b>

<br>
<br>
<img src="https://raw.githubusercontent.com/saulocatharino/serum-raman-spectroscopy-covid/master/mediamovel.png" alt="Comparação entre o sinal RAW e o processado"/>
<br>
<br>

<img src="https://raw.githubusercontent.com/saulocatharino/serum-raman-spectroscopy-covid/master/importance_c.png" alt="Importância do Feature"/>
<br>
<br>

<img src="https://raw.githubusercontent.com/saulocatharino/serum-raman-spectroscopy-covid/master/importances_2.png" alt="Importância do Feature"/>
<br>
<br>
<br>
<br>
vp = verdadeiro positivo<br>
vn = verdadeiro negativo<br>
fp = falso positivo<br>
fn = falso negativo<br>
<br>
Sensitividade = vp/(vp+fn)<br>
Especificidade = vn/(vn+fp)<br>
<br>
Modelo treinado com 50% do dataset.<br>
Validado em 100 testes (em cada teste são realizadas 179 predições) com amostragens aleatórias.<br>
<br>
<br>
<b>Resultado das médias dos testes:</b><br>
Sensitividade:  0.9629979914186166 <br>
Especificidade:  1.0 <br>

<br>
<img src="https://raw.githubusercontent.com/saulocatharino/serum-raman-spectroscopy-covid/master/100.png" alt="Testes"/>
<br>
<br>
<b><i>TO DO</b></i><br>
Processar o sinal mediante as áreas das importancias do feature (quocientes dos pesos), utilizando como limiar a média dos valores das 'importancias do feature', mantendo no processamento apenas as zonas que ultrapassarem este limiar e substituindo por zero as zonas que forem inferiores ao limiar, conforme vemos na imagem abaixo.
<br>
Filtrar o dataset neste padrão e treinar um modelo com este filtro, medir os resultados e ver se há aumento na performance da classificação.
<br>

<img src="https://raw.githubusercontent.com/saulocatharino/serum-raman-spectroscopy-covid/master/process.png" alt="Importância do Feature"/>
<br>
<br>

Dataset origem:
https://springernature.figshare.com/articles/Data_and_code_on_serum_Raman_spectroscopy_as_an_efficient_primary_screening_of_coronavirus_disease_in_2019_COVID-19_/12159924
<br><br>
Citação do dataset:<br>
<i> Gang Yin, Lintao Li, Shun Lu, Yu Yin, Yuanzhang Su, Yilan Zeng, Mei Luo, Maohua Ma, Hongyan Zhou, Dezhong Yao, Gang Liu, Jinyi Lang.</i>
<br>

