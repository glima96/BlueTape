# Guilherme da Silva Lima

Belo Horizonte, Minas Gerais
E-mail: guilherme_bsl@hotmail.com
Telefone: 31 9 9487 - 5020
Data: 04/12/2023

---

## BlueTape

Criação de código em Python para checagem de  estatísticas de empresas no Reclame Aqui de  acordo com critérios indicados



## ## Guia de Utilização - Automação ReclameAqui**

### Descrição do Programa

O programa foi desenvolvido para realizar automação no site ReclameAqui, simplificando o processo de consulta, navegação e extração de informações relevantes. Esta automação é realizada pelo script Python `main.py`.

### Instruções de Uso

**Certifique-se de ter o Python e o Chrome instalados no seu sistema.**

1. **Instalação do Python:** Se você ainda não tem o Python instalado, baixe a versão mais recente diretamente do [site oficial do Python](https://www.python.org/downloads/). Siga as instruções de instalação fornecidas no site para configurar o Python no seu sistema.

2. **Instalação do Chrome:** Certifique-se de ter o navegador Google Chrome instalado no seu computador. Você pode baixar a versão mais recente do [site oficial do Google Chrome](https://www.google.com/chrome/).

3. **Instalação da biblioteca Selenium:** Abra o terminal ou prompt de comando e execute o seguinte comando para instalar a biblioteca Selenium:

   ```
   bashCopy code
   pip install selenium
   ```

   Este comando utiliza o gerenciador de pacotes `pip` para baixar e instalar a biblioteca Selenium e suas dependências.

4. **Driver do Chrome:** Para utilizar o Selenium com o Chrome, você precisará do ChromeDriver. Certifique-se de baixar o ChromeDriver compatível com a versão do seu navegador no [site oficial do ChromeDriver](https://sites.google.com/chromium.org/driver/). Após baixar, adicione o diretório do ChromeDriver ao seu PATH ou forneça o caminho diretamente no seu script Python.



## Método Paliativo



Atualmente, devido a limitações ou incompatibilidades com o método `**await**` no Selenium em determinados contextos, implementamos um método paliativo usando uma estrutura de loop (`**for**`) para conseguir encontrar elementos na pagina. Essa abordagem é adotada como uma solução temporária até que as limitações sejam resolvidas ou que haja uma alternativa mais robusta disponível.

Entendo que, em alguns casos, a utilização do método `**await**` proporcionaria uma espera mais eficiente e assíncrona. No entanto, devido a questões específicas de implementação no Selenium, a estrutura de loop se tornou a única solução viável.

### Execução do Programa

- Abra o terminal ou prompt de comando e navegue até o diretório onde o script `main.py` está localizado.

- Execute o seguinte comando:

  ```
  bashCopy code
  python main.py
  ```

  Espere enquanto o programa navega pelo site do ReclameAqui e extrai as informações necessárias. A execução pode demorar alguns minutos.

### Arquivo Gerado

- Aguarde até que o programa finalize a execução.
- O programa gerará um arquivo chamado `dados.xls` contendo as informações extraídas.

### Observações Importantes

- A automação não requer intervenção manual. O programa irá capturar os valores automaticamente durante a execução.
- Certifique-se de não interromper o processo até que a execução seja concluída para garantir a obtenção completa das informações.

Siga essas instruções para aproveitar ao máximo a automação do ReclameAqui utilizando o script fornecido.

------

Este guia detalhado oferece uma abordagem passo a passo para garantir uma utilização eficiente e sem problemas do programa de automação no site ReclameAqui.