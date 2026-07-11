import time
import sys
from pathlib import Path
root = str(Path(__file__).resolve().parent.parent)
if root not in sys.path:
    sys.path.insert(0, root)
root = str(Path(__file__).resolve().parent.parent.parent)
if root not in sys.path:
    sys.path.insert(0, root)

import pytest

from app.tools.obligations import _get_obligations  
from app.config import GREEN, RESET

# тестирующие json-файлы
FILE_1 = "../../data/subscriptions_1.json"
FILE_2 = "../../data/subscriptions_2.json"
FILE_3 = "../../data/subscriptions_3.json"

def test_get_obligations():
    test_num = 1
    
    # тестирование начинается
    print(f"\n{GREEN}[==========]{RESET} Running unit tests...\n")
    print(f"{GREEN}[----------]{RESET} get_obligation() is being tested")
    print(f"{GREEN}[----------]{RESET} ... testing on File 1 ... ")

    # тест №1
    print(f"{GREEN}[ RUN      ]{RESET} Test {test_num}")
    start_time = time.perf_counter()
    assert _get_obligations(path=FILE_1, status="deactivated", category="Productivity") == []
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")
    test_num += 1

    # тест №2
    print(f"{GREEN}[ RUN      ]{RESET} Test {test_num}")
    start_time = time.perf_counter()
    assert _get_obligations(path=FILE_1, status="active", category="Productivity") == [
        {"id": "i9j0k1l2-t3",
            "title": "Quizlet Plus",
            "amount": 8.99,
            "currency": "USD",
            "category": "Productivity",
            "next_payment_date": "2025-07-09",
            "status": "active"
        },
        {
            "id": "y5z6a7b8-t7",
            "title": "Microsoft 365",
            "amount": 9.99,
            "currency": "USD",
            "category": "Productivity",
            "next_payment_date": "2025-08-10",
            "status": "active"
        },
        {
             "id": "a3b4c5d6-t14",
            "title": "Evernote",
            "amount": 7.99,
            "currency": "USD",
            "category": "Productivity",
            "next_payment_date": "2025-08-03",
            "status": "active"
        },
        {
            "id": "e7f8g9h0-t15",
            "title": "Canva Pro",
            "amount": 12.99,
            "currency": "USD",
            "category": "Productivity",
            "next_payment_date": "2025-07-20",
            "status": "active"
        }
        ]
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")
    test_num += 1

    # тест №3
    print(f"{GREEN}[ RUN      ]{RESET} Test {test_num}")
    start_time = time.perf_counter()
    assert _get_obligations(path=FILE_1, status="active", category="NoExistingCategory") == []
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")
    test_num += 1

    # тест №4
    print(f"{GREEN}[ RUN      ]{RESET} Test {test_num}")
    start_time = time.perf_counter()
    assert _get_obligations(path=FILE_1, status="nostatus", category="Gaming") == []
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")
    test_num += 1

    # тест №5
    print(f"{GREEN}[ RUN      ]{RESET} Test {test_num}")
    start_time = time.perf_counter()
    assert _get_obligations(path=FILE_1, status="deactivated", category="Gaming") == [{
        "id": "w9x0y1z2-t13",
        "title": "SteamPass",
        "amount": 399,
        "currency": "RUB",
        "category": "Gaming",
        "next_payment_date": "2025-09-10",
        "status": "deactivated"
    }]
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")
    test_num += 1

    # тест №6
    print(f"{GREEN}[ RUN      ]{RESET} Test {test_num}")
    start_time = time.perf_counter()
    assert _get_obligations(path=FILE_1, status="active", category="Entertainment") == [
    {
        "id": "a1b2c3d4-t1",
        "title": "Netflix",
        "amount": 9.99,
        "currency": "USD",
        "category": "Entertainment",
        "next_payment_date": "2025-07-10",
        "status": "active"    
    },
    {
        "id": "q7r8s9t0-t5",
        "title": "Wink",
        "amount": 139,
        "currency": "RUB",
        "category": "Entertainment",
        "next_payment_date": "2025-07-30",
        "status": "active"
    },
    {
        "id": "g3h4i5j6-t9",
        "title": "PremiereRutube",
        "amount": 399,
        "currency": "RUB",
        "category": "Entertainment",
        "next_payment_date": "2025-07-21",
        "status": "active"
    }
    ]
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")
    test_num += 1
    print(f"{GREEN}[----------]{RESET} {test_num-1}/{test_num-1} tests for File 1 have been passed\n")


    test_num = 1
    print(f"{GREEN}[----------]{RESET} ... testing on File 2 ... ")

    # тест №1
    print(f"{GREEN}[ RUN      ]{RESET} Test {test_num}")
    start_time = time.perf_counter()
    assert _get_obligations(path=FILE_2, status="deactivated", category=None) == [{
        "id": "o3p4q5r6-s13",
        "title": "Zoom Pro",
        "amount": 14.99,
        "currency": "USD",
        "category": "Communication",
        "next_payment_date": "2025-09-20",
        "status": "deactivated"
    }]
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")
    test_num += 1

    # тест №2
    print(f"{GREEN}[ RUN      ]{RESET} Test {test_num}")
    start_time = time.perf_counter()
    assert _get_obligations(path=FILE_2, status="active", category="Productivity") == [{
        "id": "db45sj2j-s5",
        "title": "GigaChat2-Max",
        "amount": 1950,
        "currency": "RUB",
        "category": "Productivity",
        "next_payment_date": "2025-08-02",
        "status": "active"
    },
    {
        "id": "e3f4g5h6-s3",
        "title": "ChatGPT Plus",
        "amount": 9.99,
        "currency": "EUR",
        "category": "Productivity",
        "next_payment_date": "2025-08-01",
        "status": "active"
    },
    {
        "id": "f7g8h9i0-s4",
        "title": "GitHub Pro",
        "amount": 7.99,
        "currency": "USD",
        "category": "Productivity",
        "next_payment_date": "2025-08-05",
        "status": "active"
    },
    {
        "id": "j3k4l5m6-s8",
        "title": "Adobe Creative Cloud",
        "amount": 40.99,
        "currency": "GBR",
        "category": "Productivity",
        "next_payment_date": "2025-08-25",
        "status": "active"
    },
    {
        "id": "p7q8r9s0-s14",
        "title": "Notion Personal Pro",
        "amount": 85.99,
        "currency": "KZT",
        "category": "Productivity",
        "next_payment_date": "2025-09-25",
        "status": "active"
    }
    ]
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")
    test_num += 1

    # тест №3
    print(f"{GREEN}[ RUN      ]{RESET} Test {test_num}")
    start_time = time.perf_counter()
    assert _get_obligations(path=FILE_2, status="deactivated", category="Communication") == [{
        "id": "o3p4q5r6-s13",
        "title": "Zoom Pro",
        "amount": 14.99,
        "currency": "USD",
        "category": "Communication",
        "next_payment_date": "2025-09-20",
        "status": "deactivated"
    }]
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")
    test_num += 1

    # тест №4
    print(f"{GREEN}[ RUN      ]{RESET} Test {test_num}")
    start_time = time.perf_counter()
    assert _get_obligations(path=FILE_2, status="active", category="Finance") == [{
        "id": "cfks7si2-s2",
        "title": "СберПрайм",
        "amount": 399,
        "currency": "RUB",
        "category": "Finance",
        "next_payment_date": "2025-08-03",
        "status": "active"
    }]
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")
    test_num += 1

    # тест №5
    print(f"{GREEN}[ RUN      ]{RESET} Test {test_num}")
    start_time = time.perf_counter()
    assert _get_obligations(path=FILE_2, status=None, category="Finance") == [{
        "id": "cfks7si2-s2",
        "title": "СберПрайм",
        "amount": 399,
        "currency": "RUB",
        "category": "Finance",
        "next_payment_date": "2025-08-03",
        "status": "active"
    }]
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")
    test_num += 1

    # тест №6
    print(f"{GREEN}[ RUN      ]{RESET} Test {test_num}")
    start_time = time.perf_counter()
    assert _get_obligations(path=FILE_2, status=None, category="Entertainment") == [{
        "id": "d90247sd-s2",
        "title": "Netflix",
        "amount": 9.99,
        "currency": "USD",
        "category": "Entertainment",
        "next_payment_date": "2025-07-29",
        "status": "active"
    },
    {
        "id": "i9j0k1l2-s7",
        "title": "YouTube Premium",
        "amount": 11.99,
        "currency": "USD",
        "category": "Entertainment",
        "next_payment_date": "2025-08-20",
        "status": "active"
    },
    {
        "id": "k7l8m9n0-s9",
        "title": "Amazon Prime Video",
        "amount": 32.99,
        "currency": "CNY",
        "category": "Entertainment",
        "next_payment_date": "2025-08-30",
        "status": "active"
    }
    ]
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")
    test_num += 1
    print(f"{GREEN}[----------]{RESET} {test_num-1}/{test_num-1} tests for File 1 have been passed\n")

    test_num = 1
    print(f"{GREEN}[----------]{RESET} ... testing on File 3 ... ")

    # тест №1
    print(f"{GREEN}[ RUN      ]{RESET} Test {test_num}")
    start_time = time.perf_counter()
    assert _get_obligations(path=FILE_3, status="deactivated", category="Education") == [{
        "id": "c6d7e8f9-s14",
        "title": "Coursera Plus",
        "amount": 399,
        "currency": "USD",
        "category": "Education",
        "next_payment_date": "2025-08-10",
        "status": "deactivated"
    }]
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")
    test_num += 1

    # тест №2
    print(f"{GREEN}[ RUN      ]{RESET} Test {test_num}")
    start_time = time.perf_counter()
    assert _get_obligations(path=FILE_3, status="active", category="Education") == [{
        "id": "b2c3d4e5-s13",
        "title": "Duolingo Plus",
        "amount": 6.99,
        "currency": "USD",
        "category": "Education",
        "next_payment_date": "2025-08-05",
        "status": "active"
    }]
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")
    test_num += 1

    # тест №3
    print(f"[{GREEN} RUN      ]{RESET} Test {test_num}")
    start_time = time.perf_counter()
    assert _get_obligations(path=FILE_3, status="active", category="Communication") == []
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")
    test_num += 1

    # тест №4
    print(f"{GREEN}[ RUN      ]{RESET} Test {test_num}")
    start_time = time.perf_counter()
    assert _get_obligations(path=FILE_3, status="active", category=None) == [
    {
        "id": "p7fh45d7-s1",
        "title": "Notion Personal Pro",
        "amount": 12.99,
        "currency": "EUR",
        "category": "Productivity",
        "next_payment_date": "2025-07-18",
        "status": "active"
    },
    {
                "id": "r2s3t4u5-s3",
        "title": "Microsoft 365 Personal",
        "amount": 69.99,
        "currency": "USD",
        "category": "Productivity",
        "next_payment_date": "2025-07-25",
        "status": "active"
    },
    {
                "id": "t0u1v2w3-s5",
        "title": "Spotify Premium",
        "amount": 9.99,
        "currency": "USD",
        "category": "Music",
        "next_payment_date": "2025-08-05",
        "status": "active"
    },
    {
                "id": "u4v5w6x7-s6",
        "title": "Adobe Creative Cloud",
        "amount": 52.99,
        "currency": "USD",
        "category": "Productivity",
        "next_payment_date": "2025-08-10",
        "status": "active"
    },
    {
                "id": "w2x3y4z5-s8",
        "title": "Wink",
        "amount": 139,
        "currency": "RUB",
        "category": "Entertainment",
        "next_payment_date": "2025-08-20",
        "status": "active"
    },
    {
                "id": "x6y7z8a9-s9",
        "title": "Quizlet Unlimited",
        "amount": 12.99,
        "currency": "USD",
        "category": "Productivity",
        "next_payment_date": "2025-08-23",
        "status": "active"
    },
    {
                "id": "z4a5b6c7-s11",
        "title": "Notion Personal Pro",
        "amount": 12.99,
        "currency": "EUR",
        "category": "Gaming",
        "next_payment_date": "2025-07-27",
        "status": "active"
    },
    {
                "id": "a8b9c0d1-s12",
        "title": "Strava Premium",
        "amount": 1399,
        "currency": "RUB",
        "category": "Fitness",
        "next_payment_date": "2025-08-01",
        "status": "active"
    },
    {
                "id": "b2c3d4e5-s13",
        "title": "Duolingo Plus",
        "amount": 6.99,
        "currency": "USD",
        "category": "Education",
        "next_payment_date": "2025-08-05",
        "status": "active"
    }]
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")
    test_num += 1

    # тест №5
    print(f"{GREEN}[ RUN      ]{RESET} Test {test_num}")
    start_time = time.perf_counter()
    assert _get_obligations(path=FILE_3, status="deactivated", category=None) == [{
        "id": "q8g9h0i1-s2",
        "title": "Todoist Premium",
        "amount": 4.99,
        "currency": "USD",
        "category": "Productivity",
        "next_payment_date": "2025-07-22",
        "status": "deactivated"
    },
    {
        "id": "s6t7u8v9-s4",
        "title": "YouTube Premium",
        "amount": 11.99,
        "currency": "USD",
        "category": "Entertainment",
        "next_payment_date": "2025-07-30",
        "status": "deactivated"
    },
    {
        "id": "v8w9x0y1-s7",
        "title": "Amazon Prime Video",
        "amount": 12.99,
        "currency": "USD",
        "category": "Entertainment",
        "next_payment_date": "2025-08-15",
        "status": "deactivated"
    },
    {
         "id": "y0z1a2b3-s10",
        "title": "Telegram Premium",
        "amount": 299,
        "currency": "RUB",
        "category": "Communication",
        "next_payment_date": "2025-08-28",
        "status": "deactivated"
    },
    {
        "id": "c6d7e8f9-s14",
        "title": "Coursera Plus",
        "amount": 399,
        "currency": "USD",
        "category": "Education",
        "next_payment_date": "2025-08-10",
        "status": "deactivated"
    }
    ]
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")
    test_num += 1

    # тест №6
    print(f"{GREEN}[ RUN      ]{RESET} Test {test_num}")
    start_time = time.perf_counter()
    assert _get_obligations(path=FILE_3, status=None, category="Music") == [{
        "id": "t0u1v2w3-s5",
        "title": "Spotify Premium",
        "amount": 9.99,
        "currency": "USD",
        "category": "Music",
        "next_payment_date": "2025-08-05",
        "status": "active"
    }]
    end_time = time.perf_counter()
    print(f"{GREEN}[       OK ]{RESET}          {round(end_time - start_time, 2)} ms")
    test_num += 1

    print(f"{GREEN}[----------]{RESET} {test_num-1}/{test_num-1} tests for File 3 have been passed")
    print(f"{GREEN}[==========]{RESET} all {test_num*3}/{test_num*3} tests have been passed\n")

if __name__ == "__main__":
    test_get_obligations()