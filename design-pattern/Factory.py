from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    @abstractmethod
    def createCoin(self):
        pass

    # Some operation
    def exchange_coin(self) -> str:
        self.createCoin()
        return "Exchanging the coin"


class ConcreteCreatorETH(Creator):
    def createCoin(self) -> Coin:
        return ConcreteCoinETH()


class ConcreteCreatorBNB(Creator):
    def createCoin(self) -> Coin:
        return ConcreteCoinBNB()


class Coin(ABC):
    @abstractmethod
    def operation(self):
        pass


class ConcreteCoinETH(Coin):
    def operation(self) -> bool:
        # Do something here
        return True


class ConcreteCoinBNB(Coin):
    def operation(self) -> bool:
        # Do something here
        return True


def run_app(creator: Creator) -> None:
    print(f"{creator.exchange_coin()}", end="")


if __name__ == "__main__":
    run_app(ConcreteCreatorETH())
