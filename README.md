# Market for Lemons Simulation

A small Python simulation of adverse selection inspired by George Akerlof’s paper, *The Market for Lemons*.

## Research Question

What happens when sellers know the quality of a product, but buyers cannot observe it?

## Core Idea

When buyers cannot distinguish good products from low-quality products, they offer a price based on the expected average quality of the market.

If that price is too low for high-quality sellers, those sellers leave. The market then contains more low-quality products, causing buyers to offer even less.

This creates a cycle of declining quality and trust.

## Model

The simulation includes:

- Good cars valued at `$100`
- Lemons valued at `$40`
- Good sellers requiring at least `$80`
- Lemon sellers requiring at least `$30`
- A market containing 1,000 cars
- Full-information and hidden-information scenarios

## Running the Simulation

```bash
python3 market_for_lemons_simulation.py
```

The program prints the market outcomes and creates a CSV file containing the hidden-information results.

## Files

- `market_for_lemons_simulation.py` — simulation code
- `market_for_lemons_notes.md` — explanation and interpretation
- `market_for_lemons_rounds.csv` — generated simulation data
- `market_for_lemons_cv_entry.md` — CV-ready project description

## Result

Under hidden information, the expected market price is below the reservation price of good sellers. Good sellers therefore withdraw, leaving a market dominated by lemons.

## Limitations

This is a simplified theoretical model using artificial values. It is intended to make the mechanism of adverse selection visible, not to estimate a real market.

Possible extensions include:

- Warranties
- Product certification
- Inspections
- Reputation systems
- Repeated interaction
- Agricultural-market data from Nepal

