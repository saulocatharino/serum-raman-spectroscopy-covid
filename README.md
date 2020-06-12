# Projeto Mayday - Sistema fase 3  
<b> Serum Raman spectroscopy COVID-19</b>
<br>
Modelo de Regressão Logística para diagnóstico por Espectroscopia Raman.<br>
<br>
vp = verdadeiro positivo<br>
vn = verdadeiro negativo<br>
fp = falso positivo<br>
fn = falso negativo<br>
<br>
Sensitividade = vp/(vp+fn)<br>
Especificidade =vn/(vn+fp)<br>
<br>
Modelo treinado com 50% do dataset.<br>
Validado em 100 testes (em cada teste são realizadas 179 predições) com amostragens aleatórias.<br>
<br>
<br>
<br>
<i>No modelo anterior o modelo foi treinado com o sinal RAW, sem filtros, nesta nova versão, decompus o sinal com Decomposição sazonal usando médias móveis, com período de 8 valores por média.<br></i><br>
Desta forma obtivemos aumento de <b>5.1%</b> de precisão em relação ao modelo anterior.<br>
<br>
<img src="https://raw.githubusercontent.com/saulocatharino/serum-raman-spectroscopy-covid/master/compara.png" alt="Comparação entre o sinal RAW e o processado"/>
<br>
<br>
<br>
<b>Resultado das médias dos testes:</b><br>
Sensitividade:  0.9529703318667836 <br>
Especificidade:  1.0 <br>

<br>
<img src="https://raw.githubusercontent.com/saulocatharino/serum-raman-spectroscopy-covid/master/10k.png" alt="Testes"/>
<br>

Dataset origem:
https://springernature.figshare.com/articles/Data_and_code_on_serum_Raman_spectroscopy_as_an_efficient_primary_screening_of_coronavirus_disease_in_2019_COVID-19_/12159924
<br><br>
Citação do dataset:<br>
<i> Gang Yin, Lintao Li, Shun Lu, Yu Yin, Yuanzhang Su, Yilan Zeng, Mei Luo, Maohua Ma, Hongyan Zhou, Dezhong Yao, Gang Liu, Jinyi Lang.</i>
<br>
