"""A small simulation of Akerlof's Market for Lemons.

The model compares two markets:
1. Full information: buyers can see each car's quality.
2. Hidden information: buyers only know the average quality of cars offered.

In the hidden-information market, good sellers leave when the expected market
price falls below their reservation value. This can create a negative feedback
loop: fewer good cars -> lower expected quality -> lower prices -> even fewer
good cars.
"""

from dataclasses import dataclass
import csv
import random
from pathlib import Path

try:
    import matplotlib.pyplot as plt
except ImportError:  # The simulation still works without the optional chart.
    plt = None


@dataclass(frozen=True)
class Car:
    quality: str
    value: float
    reservation_price: float


QUALITY = {
    "good": (100.0, 80.0),
    "lemon": (40.0, 30.0),
}


def make_market(seed: int, size: int = 1_000, good_share: float = 0.5) -> list[Car]:
    rng = random.Random(seed)
    cars = []
    for _ in range(size):
        quality = "good" if rng.random() < good_share else "lemon"
        value, reservation_price = QUALITY[quality]
        cars.append(Car(quality, value, reservation_price))
    return cars


def full_information_market(cars: list[Car]) -> dict[str, float]:
    traded = [car for car in cars if car.value >= car.reservation_price]
    return {
        "cars_offered": len(cars),
        "cars_traded": len(traded),
        "good_share_offered": share(cars, "good"),
        "good_share_traded": share(traded, "good"),
        "average_price": sum(car.value for car in traded) / len(traded),
    }


def hidden_information_market(
    cars: list[Car], rounds: int = 12
) -> list[dict[str, float]]:
    current = cars[:]
    history = []
    for round_number in range(1, rounds + 1):
        expected_value = sum(car.value for car in current) / len(current)
        traded = [car for car in current if expected_value >= car.reservation_price]
        history.append(
            {
                "round": round_number,
                "cars_offered": len(current),
                "good_share_offered": share(current, "good"),
                "expected_price": expected_value,
                "cars_traded": len(traded),
                "good_share_traded": share(traded, "good"),
            }
        )
        # Sellers who cannot receive their minimum acceptable price withdraw.
        current = [car for car in current if expected_value >= car.reservation_price]
        if not current or len(traded) == len(current):
            break
    return history


def share(cars: list[Car], quality: str) -> float:
    return sum(car.quality == quality for car in cars) / len(cars) if cars else 0.0


def write_csv(path: Path, rows: list[dict[str, float]]) -> None:
    with path.open("w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def write_chart(path: Path, rows: list[dict[str, float]]) -> None:
    if plt is None:
        return
    rounds = [row["round"] for row in rows]
    good_share = [row["good_share_offered"] * 100 for row in rows]
    expected_price = [row["expected_price"] for row in rows]
    figure, price_axis = plt.subplots(figsize=(8, 4.5))
    price_axis.plot(rounds, expected_price, marker="o", color="#b45309", label="Expected price")
    price_axis.set_xlabel("Market round")
    price_axis.set_ylabel("Expected price ($)", color="#b45309")
    price_axis.set_ylim(bottom=0)
    share_axis = price_axis.twinx()
    share_axis.plot(rounds, good_share, marker="s", color="#166534", label="Good cars offered")
    share_axis.set_ylabel("Good cars offered (%)", color="#166534")
    share_axis.set_ylim(0, 100)
    price_axis.set_title("Hidden information can push good sellers out")
    price_axis.grid(alpha=0.25)
    figure.tight_layout()
    figure.savefig(path, dpi=160)
    plt.close(figure)


def main() -> None:
    output_dir = Path(__file__).parent
    cars = make_market(seed=7)
    full_info = full_information_market(cars)
    hidden_info = hidden_information_market(cars)
    write_csv(output_dir / "market_for_lemons_rounds.csv", hidden_info)
    write_chart(output_dir / "market_for_lemons_chart.png", hidden_info)

    print("MARKET FOR LEMONS SIMULATION")
    print("\nFull information")
    for key, value in full_info.items():
        print(f"{key}: {value:.3f}" if isinstance(value, float) else f"{key}: {value}")

    print("\nHidden information")
    for row in hidden_info:
        print(
            f"round {int(row['round']):2d} | offered {int(row['cars_offered']):4d} "
            f"| good cars {row['good_share_offered']:.1%} "
            f"| expected price ${row['expected_price']:.2f}"
        )


if __name__ == "__main__":
    main()
