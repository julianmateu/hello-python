from hellopython.greeter import Greeter


class TestGreeter:
    def test_greeter(self) -> None:
        assert Greeter().greet() == "Hello World!"
