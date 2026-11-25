"""Demonstração de Strategy para cálculo de frete."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Item:
    nome: str
    preco_unitario: Decimal
    quantidade: int

    def total(self) -> Decimal:
        return self.preco_unitario * self.quantidade


class Frete(ABC):
    @abstractmethod
    def calcular(self, subtotal: Decimal) -> Decimal:
        """Retorna o frete em reais para um carrinho com itens."""


class FretePadrao(Frete):
    def calcular(self, subtotal: Decimal) -> Decimal:
        return Decimal("0.00") if subtotal >= Decimal("150.00") else Decimal("15.00")


class FreteExpresso(Frete):
    def calcular(self, subtotal: Decimal) -> Decimal:
        return Decimal("25.00")


class Carrinho:
    def __init__(self, frete: Frete) -> None:
        self._itens: list[Item] = []
        self.definir_frete(frete)

    def adicionar(self, nome: str, preco_unitario: Decimal, quantidade: int) -> None:
        if not nome.strip():
            raise ValueError("Informe o nome do item.")
        if not preco_unitario.is_finite() or preco_unitario <= 0:
            raise ValueError("O preço unitário deve ser positivo e finito.")
        if preco_unitario.as_tuple().exponent < -2:
            raise ValueError("Use até duas casas decimais no preço.")
        if type(quantidade) is not int or quantidade <= 0:
            raise ValueError("A quantidade deve ser um inteiro positivo.")
        self._itens.append(Item(nome, preco_unitario, quantidade))

    def definir_frete(self, frete: Frete) -> None:
        self._frete = frete

    def subtotal(self) -> Decimal:
        return sum((item.total() for item in self._itens), Decimal("0.00"))

    def cotar(self) -> tuple[Decimal, Decimal, Decimal]:
        if not self._itens:
            raise ValueError("Adicione um item antes de cotar.")
        subtotal = self.subtotal()
        frete = self._frete.calcular(subtotal)
        return subtotal, frete, subtotal + frete


def em_reais(valor: Decimal) -> str:
    return f"R$ {valor:.2f}".replace(".", ",")


def main() -> None:
    carrinho = Carrinho(FretePadrao())
    carrinho.adicionar("Caderno", Decimal("60.00"), 2)
    for rotulo, modalidade in (
        ("Padrão", FretePadrao()),
        ("Expresso", FreteExpresso()),
    ):
        carrinho.definir_frete(modalidade)
        subtotal, frete, total = carrinho.cotar()
        print(
            f"{rotulo} | Subtotal {em_reais(subtotal)} | "
            f"Frete {em_reais(frete)} | Total {em_reais(total)}"
        )


if __name__ == "__main__":
    main()
