# Carrinho de compras

Prova de conceito do padrão comportamental Strategy aplicada ao cálculo de frete. A demonstração troca a modalidade no mesmo carrinho e imprime subtotal, frete e total.

Com Python 3.10 ou superior, execute na raiz do repositório:

```sh
python carrinho.py
```

A demonstração usa dois cadernos de R$ 60,00. Com subtotal de R$ 120,00, o total é R$ 135,00 no frete padrão e R$ 145,00 no expresso. O frete padrão custa R$ 15,00 e é gratuito a partir de R$ 150,00. O frete expresso custa R$ 25,00.

O padrão estrutural Adapter faz parte da arquitetura proposta para uma futura integração com uma transportadora. O projeto de console usa apenas a biblioteca padrão do Python.

## Interface web
Execute `python servidor.py` e abra http://127.0.0.1:8000 no navegador. Adicione produtos e altere a modalidade para comparar as cotações. O frontend mantém os itens durante a sessão da página. O backend recebe a lista em POST /cotacao e aplica as mesmas estratégias da demonstração de console.
