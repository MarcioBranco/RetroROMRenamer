# RetroROMRenamer

![Project Logo](link-para-uma-imagem-do-logo.png)

**RetroROMRenamer** é uma ferramenta para renomear arquivos de ROMs de jogos retrô de forma automatizada, com base em informações contidas em um DataFrame ou outras fontes de dados. Esta ferramenta é ideal para entusiastas de jogos retrô que desejam organizar e padronizar suas coleções de ROMs.

## Funcionalidades

- Renomeia arquivos de ROMs com base em informações contidas em um DataFrame.
- Possibilidade de renomear arquivos localmente ou via FTP.
- Suporte a operações em lote para otimizar a organização de grandes coleções de ROMs.


## Pré-requisitos

Antes de usar o **RetroROMRenamer**, certifique-se de ter os seguintes pré-requisitos instalados:

- Python 3.11.4 (Você pode criar um ambiente virtual para isolar a versão do Python)
- Pandas (para manipulação do DataFrame)
- Outras bibliotecas Python, conforme necessário (por exemplo, `ftplib` para transferência FTP)

## Configuração do Ambiente

Para configurar o ambiente, siga estas etapas:

1. Crie um ambiente virtual (opcional, mas recomendado):
    a. python -m venv venv
    b. virtualenv venv --prompt RRR

2. Ative o ambiente virtual:
    a. No Windows:
        venv\Scripts\activate
    b. No macOS e Linux:
        source venv/bin/activate

3. Instale as dependências do projeto:
    pip install -r requirements.txt

## Uso

1. Clone o repositório ou faça o download do código-fonte.
    a. para clone use : gh repo clone MarcioBranco/RetroROMRenamer
    b. ou faça download como preferir.
2. Configure as informações de acesso FTP, se aplicável, no arquivo : 
    a. env.py 
    b. config.json

3. Execute o script principal para iniciar o processo de renomeação: 
    python app.py.


## Contribuição
Gostaria de contribuir para o desenvolvimento do **RetroROMRenamer**? Sinta-se à vontade para criar pull requests e abrir issues no GitHub.

## TODO
Aqui estão algumas tarefas pendentes e planos futuros para o projeto:
- [ ] Implementar a funcionalidade de renomeação local de arquivos.
- [ ] Aprimorar a documentação e fornecer exemplos de uso.
- [ ] Adicionar suporte a diferentes formatos de arquivo de ROM.
- [ ] Testes automatizados para garantir a estabilidade.
- [ ] Melhorar o desempenho ao lidar com grandes volumes de dados.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

**Nota:** Este é um projeto em desenvolvimento, e novas funcionalidades podem ser adicionadas ao longo do tempo. Fique à vontade para enviar feedback e sugestões!