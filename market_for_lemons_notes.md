# Project 1: Market for Lemons

## Research question

What happens when sellers know the quality of a product but buyers do not?

## Model

- There are 1,000 cars.
- A good car is worth $100 and its owner will not sell below $80.
- A lemon is worth $40 and its owner will not sell below $30.
- Half the cars begin as good cars.
- In the hidden-information market, buyers offer the average value of the cars still available.
- Good sellers leave if the expected price is below $80.

The values are artificial. Their purpose is to make the mechanism visible, not to describe a real car market.

## Expected result

With full information, buyers can distinguish quality and both types can trade.

With hidden information, the average market price is initially $70, which is below the good sellers' reservation price. Good sellers withdraw, leaving mostly lemons. The market then becomes cheaper and lower quality.

This is the adverse-selection mechanism described by George Akerlof: poor information can prevent mutually beneficial trade, even when buyers and sellers are individually rational.

## How to run it

```bash
python3 market_for_lemons_simulation.py
```

The script prints each round and creates `market_for_lemons_rounds.csv`.

## Questions to investigate next

1. What changes when the initial share of good cars is 20%, 50%, or 80%?
2. What happens when buyers can inspect a random sample of cars?
3. Can warranties, certification, reputation, or repeat interaction restore trade?
4. How would the model change for farmers who know their crop quality better than buyers?

## First interpretation

The central lesson is not simply that “bad products win.” It is that information quality changes incentives. When buyers cannot verify quality, their cautious price can be too low for good sellers, and that cautious price can make the market worse.
