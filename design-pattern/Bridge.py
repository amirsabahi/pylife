from abc import ABC, abstractmethod


class BaseRequestManager(ABC):
    @abstractmethod
    def call_function_api(self):
        pass


class BinanceRequestManager(BaseRequestManager):
    def __init__(self, base_interface):
        self.base_interface = base_interface

    def call_function_api(self):
        return self.base_interface.submit_order()


class KucoinRequestManager(BaseRequestManager):
    def __init__(self, base_interface):
        self.base_interface = base_interface

    def call_function_api(self):
        return self.base_interface.submit_order()


class BaseInterface(ABC):
    @abstractmethod
    def submit_order(self):
        pass


class BinanceInterface(BaseInterface):
    def submit_order(self):
        return "BinanceInterface: Here's the result on the Binance Platform."


class KucoinInterface(BaseInterface):
    def submit_order(self):
        return "KucoinInterface: Here's the result on the Kucoin Platform."


if __name__ == "__main__":
    binance = BinanceInterface()
    request = BinanceRequestManager(binance)
    result = request.call_function_api()

    print(result)

    kucoin = KucoinInterface()
    request = KucoinRequestManager(kucoin)
    result = request.call_function_api()
    print(result)
