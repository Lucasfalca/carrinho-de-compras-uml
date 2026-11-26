# Falcão Express

Simulador acadêmico de cotação de transporte. Abra **index.html** no navegador. Escolha uma das seis lojas, busque um produto pelo nome, confira o preço cadastrado e informe a quantidade. Cada remessa reúne produtos de uma única loja. Os preços e prazos são fictícios.

| Modalidade | Frete por remessa | Previsão simulada |
| --- | --- | --- |
| Padrão | R$ 15,00; gratuito a partir de R$ 150,00 em produtos | 5 dias corridos |
| Expressa | R$ 25,00 | 2 dias corridos |

Dois fones de R$ 89,90 somam R$ 179,80. O total permanece R$ 179,80 na modalidade padrão e passa a R$ 204,80 na expressa.

## Como executar

A interface funciona diretamente no navegador e calcula valores em centavos. Para servir a página por HTTP, execute `python servidor.py` e abra http://127.0.0.1:8000. O servidor também expõe POST /cotacao para cotar itens via API.

A prova de conceito em Python demonstra Strategy com as classes FretePadrao e FreteExpresso. Com Python 3.10 ou superior, execute `python carrinho.py`. O padrão Adapter está modelado para uma futura integração externa.

A documentação do trabalho está em [documentacao-falcao-express.pdf](documentacao-falcao-express.pdf).
