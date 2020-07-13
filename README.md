# Projeto Mayday - Sistema fase 3  

Para testar o webapp utilize os arquivos:<br>
  individuo_saudavel.txt<br>
  individuo_infectado.txt.<br><br>
Modelo de Gaussian Process Classifier para conjunto de espectro em intensidade de superficie aprimorada.<br></b>

<br>
<br>
<img src="https://raw.githubusercontent.com/saulocatharino/serum-raman-spectroscopy-covid/master/mediamovel.png" alt="Comparação entre o sinal RAW e o processado"/>
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
Sensitividade Média:  0.9837040865421662 <br>
Especificidade Média:  1.0 <br>


<br>
<img src="https://raw.githubusercontent.com/saulocatharino/serum-raman-spectroscopy-covid/master/1000.png" alt="Testes"/>
<br>
<br>


Dataset origem:
https://springernature.figshare.com/articles/Data_and_code_on_serum_Raman_spectroscopy_as_an_efficient_primary_screening_of_coronavirus_disease_in_2019_COVID-19_/12159924
<br><br>
Citação do dataset:<br>
<i> Gang Yin, Lintao Li, Shun Lu, Yu Yin, Yuanzhang Su, Yilan Zeng, Mei Luo, Maohua Ma, Hongyan Zhou, Dezhong Yao, Gang Liu, Jinyi Lang.</i>
<br>

