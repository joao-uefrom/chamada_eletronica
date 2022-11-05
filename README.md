# Sistema de Frequência Escolar Utilizando Biometria Facial

Trabalho de Conclusão de Curso na Modalidade de Artigo Científico apresentado a Faculdade de Tecnologia do Amapá - META, como requisito final à obtenção do grau de Bacharel em Engenharia de Computação.

## Detalhes

- Data apresentação: 22/10/2022
- Nota obtida: 10 (Máxima)

## Resumo

> Este trabalho apresenta o desenvolvimento de um sistema que através do reconhecimento facial, tecnologia que é capaz de validar uma identidade apenas com uma foto do rosto, busca modernizar a frequência escolar. Sendo projetado e desenvolvido em Python, o trabalho utiliza das vastas bibliotecas disponíveis para a linguagem na busca de alcançar os seus objetivos. Indo além e fazendo testes e comparações para avaliar a melhor opção a ser utilizada fazendo uma melhor utilização de recursos.

## Componentes do projeto

- Back-end, feito em **Python** com o Framework **Django**
    - Recebe fotos e armazena elas para usar no treinamento do modelo de reconhecimento facial
    - Possui uma interface **WEB** para permiti o cadastro de alunos e exibir estatísticas do ambiente
    - Disponibiliza uma **API** para receber fotos a serem analisadas e efetuar a frequência escolar daquele aluno
- Totem, feito em **Python** sem o auxílio de frameworks
    - É o programa que é instalado em um *totem* para ficar na entrada da escola onde os alunos serão escaneados
    - Se comunica diretamente com back-end para trocar informações de alunos e realizar a frequência escolar
    - Pode ser instalado em um **Raspberry** com uma tela **LCD**

### Bibliotecas utilizadas

- [PySimplesGui](https://www.pysimplegui.org/en/latest/)
- [TensorFlow](https://www.tensorflow.org/)
- [OpenCV](https://opencv.org/)
- [Pickle](https://docs.python.org/3/library/pickle.html)
- [Requests](https://requests.readthedocs.io/en/latest/)
- [Django](https://www.djangoproject.com/)
- [MediaPipe](https://google.github.io/mediapipe/)
- [NumPy](https://numpy.org/)
- [face_recognition](https://github.com/ageitgey/face_recognition)
- [Dlib](http://dlib.net/)
- [Scikit-Learn](https://scikit-learn.org/stable/)
- [SQLite3](https://docs.python.org/3/library/sqlite3.html)

### Temple HTML utilizado

- [Tabler](https://tabler.io/ "A premium and open source dashboard template with a responsive and high-quality UI.")

### IDEA utilizada

- [PyCharm](https://www.jetbrains.com/pycharm/)

## Capturas de tela

### Back-end

![](https://raw.githubusercontent.com/joao-uefrom/chamada_eletronica/main/imagens/Imagem1.png)

### Totem

![](https://raw.githubusercontent.com/joao-uefrom/chamada_eletronica/main/imagens/Imagem6.png)
![](https://raw.githubusercontent.com/joao-uefrom/chamada_eletronica/main/imagens/Imagem7.png)
![](https://raw.githubusercontent.com/joao-uefrom/chamada_eletronica/main/imagens/Imagem8.png)
![](https://raw.githubusercontent.com/joao-uefrom/chamada_eletronica/main/imagens/Imagem9.png)

## Obrigado por ler!

- Ficou alguma dúvida, precisa de ajuda ou quer entrar em contato?
- Sinta-se livre para me enviar um e-mail: <joao.fernandesds26@gmail.com>