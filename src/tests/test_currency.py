import time
import sys
from pathlib import Path
root = str(Path(__file__).resolve().parent.parent)
if root not in sys.path:
    sys.path.insert(0, root)

from app.tools.currency import _convert_currency
from app.config import GREEN, RESET


def test_convert_currency():
    test_num = 1
    
    # тестирование начинается
    print(f"\n{GREEN}[==========]{RESET} Running unit tests...")
    print(f"{GREEN}[----------]{RESET} convert_currency() is being tested")
    print(f"{GREEN}[----------]{RESET} ... testing on File 1 ... ")

    # тест №1
    print(f"Test {test_num}")
    print(f"{GREEN}[ RUN      ]{RESET} isinstance(res, float)")
    start_time = time.perf_counter()
    res =  _convert_currency(amount=1, from_currency="USD", to_currency="RUB")
    assert isinstance(res, float)
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")

    print(f"{GREEN}[ RUN      ]{RESET} matching range")
    start_time = time.perf_counter()
    assert 0 < res < 150
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")
    test_num += 1

    # тест №2
    print(f"Test {test_num}")
    print(f"{GREEN}[ RUN      ]{RESET} isinstance(res, float)")
    start_time = time.perf_counter()
    res =  _convert_currency(amount=1, from_currency="RUB", to_currency="USD")
    assert isinstance(res, float)
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")

    print(f"{GREEN}[ RUN      ]{RESET} matching range")
    start_time = time.perf_counter()
    assert 0 < res < 0.1
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")
    test_num += 1

    # тест №3
    print(f"Test {test_num}")
    print(f"{GREEN}[ RUN      ]{RESET} isinstance(res, float)")
    start_time = time.perf_counter()
    res =  _convert_currency(amount=9, from_currency="USD", to_currency="EUR")
    assert isinstance(res, float)
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")

    print(f"{GREEN}[ RUN      ]{RESET} matching range")
    start_time = time.perf_counter()
    assert 0 < res < 10
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")
    test_num += 1

    # тест №4
    print(f"Test {test_num}")
    print(f"{GREEN}[ RUN      ]{RESET} isinstance(res, float)")
    start_time = time.perf_counter()
    res =  _convert_currency(amount=0.5, from_currency="USD", to_currency="KZT")
    assert isinstance(res, float)
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")

    print(f"{GREEN}[ RUN      ]{RESET} matching range")
    start_time = time.perf_counter()
    assert 0 < res < 300
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")
    test_num += 1

    # тест №5
    print(f"Test {test_num}")
    print(f"{GREEN}[ RUN      ]{RESET} isinstance(res, float)")
    start_time = time.perf_counter()
    res =  _convert_currency(amount=0.3, from_currency="EUR", to_currency="RUB")
    assert isinstance(res, float)
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")

    print(f"{GREEN}[ RUN      ]{RESET} matching range")
    start_time = time.perf_counter()
    assert 0 < res < 50
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")
    test_num += 1

    # тест №6
    print(f"Test {test_num}")
    print(f"{GREEN}[ RUN      ]{RESET} isinstance(res, float)")
    start_time = time.perf_counter()
    res =  _convert_currency(amount=20, from_currency="RUB", to_currency="EUR")
    assert isinstance(res, float)
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")

    print(f"{GREEN}[ RUN      ]{RESET} matching range")
    start_time = time.perf_counter()
    assert 0 < res < 0.5
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")
    test_num += 1

    # тест №7
    print(f"Test {test_num}")
    print(f"{GREEN}[ RUN      ]{RESET} isinstance(res, float)")
    start_time = time.perf_counter()
    res =  _convert_currency(amount=150, from_currency="RUB", to_currency="KZT")
    assert isinstance(res, float)
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")

    print(f"{GREEN}[ RUN      ]{RESET} matching range")
    start_time = time.perf_counter()
    assert 0 < res < 1500
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")
    test_num += 1

    # тест №8
    print(f"Test {test_num}")
    print(f"{GREEN}[ RUN      ]{RESET} isinstance(res, float)")
    start_time = time.perf_counter()
    res =  _convert_currency(amount=5129, from_currency="KZT", to_currency="RUB")
    assert isinstance(res, float)
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")

    print(f"{GREEN}[ RUN      ]{RESET} matching range")
    start_time = time.perf_counter()
    assert 0 < res < 1000
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")
    test_num += 1

    # тест №9
    print(f"Test {test_num}")
    print(f"{GREEN}[ RUN      ]{RESET} isinstance(res, float)")
    start_time = time.perf_counter()
    res =  _convert_currency(amount=100, from_currency="ARS", to_currency="RUB")
    assert isinstance(res, float)
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")

    print(f"{GREEN}[ RUN      ]{RESET} matching range")
    start_time = time.perf_counter()
    assert 0 < res < 10
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")
    test_num += 1

    # тест №9
    print(f"Test {test_num}")
    print(f"{GREEN}[ RUN      ]{RESET} isinstance(res, float)")
    start_time = time.perf_counter()
    res =  _convert_currency(amount=99, from_currency="USD", to_currency="ARS")
    assert isinstance(res, float)
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")

    print(f"{GREEN}[ RUN      ]{RESET} matching range")
    start_time = time.perf_counter()
    assert 0 < res < 200_000
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")
    test_num += 1

    print(f"{GREEN}[==========]{RESET} all {test_num-1}/{test_num-1} tests have been passed successfully\n")


if __name__ == "__main__":
    test_convert_currency()
    #tests% python3 -m pytest test_currency.py