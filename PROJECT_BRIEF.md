# Project Brief — Trading Algorithm Simulator

## 1. Purpose and Context
This project is a **learning-focused trading simulation**. It is designed to demonstrate the end-to-end flow of a simple algorithmic trading system—**without** attempting to be profitable or production-ready.

The simulator:
- Loads historical price data from a local CSV file
- Runs a trade-execution routine
- Records each operation and its outcome
- Updates a **fictitious account balance**
- Prints a final report and a trade log

## 2. Objectives
### Primary objectives (learning)
- Practice building a complete Python program with a clear entry point (`Resumen_final.py`)
- Develop comfort with:
  - input validation and user prompts
  - modularization (separating the runner from the entry script)
  - printing formatted summaries and logs
  - handling simple edge cases

### Secondary objectives (trading workflow familiarity)
- Understand how trading results accumulate into an account balance
- Organize and present basic performance stats (wins/losses, total PnL, trade list)

## 3. Non‑Goals
This project does **not** aim to:
- Provide a profitable or market-robust strategy
- Support live trading or broker connectivity
- Model real-world frictions (slippage, fees, latency) unless explicitly implemented
- Provide a comprehensive backtesting engine comparable to professional platforms

## 4. User Experience (CLI Flow)
1. User starts the program:
   - `python Resumen_final.py`
2. Program prompts for:
   - initial account balance (must be a non-negative float)
   - optional limit on number of operations (integer or empty input)
3. Program runs the simulation using:
   - `precios.csv` as the input dataset
   - `Dsimulador_ejecucion.ejecutar_trading(...)` as the execution routine
4. Program prints:
   - a summary of results
   - a detailed list/log of recorded operations

## 5. System Design (High-Level)
### Entry point
- **`Resumen_final.py`**
  - Handles interactive CLI inputs
  - Performs basic validation
  - Calls the simulation runner
  - Prints summary + operations log

### Simulation runner
- **`Dsimulador_ejecucion.py`** (imported module)
  - Contains `ejecutar_trading(...)`
  - Responsible for:
    - reading and interpreting `precios.csv`
    - producing a “cuenta” (account object) with a final balance and recorded operations

### Data
- **`precios.csv`**
  - Local CSV file containing historical prices
  - The required columns and format are defined by `Dsimulador_ejecucion`

## 6. Outputs and Metrics
Typical outputs include:
- Initial and final account balance
- Number of operations simulated
- Win/loss counts
- Total profit/loss
- Per-trade log fields (example categories):
  - open/close timestamps
  - instrument
  - direction (buy/sell)
  - size/quantity
  - entry/exit price
  - per-trade PnL

## 7. Assumptions and Constraints
- The simulation is **offline** and uses CSV-based historical data
- Results depend fully on:
  - the dataset in `precios.csv`
  - the algorithm logic inside `Dsimulador_ejecucion`
- Output is printed to the console (no GUI)
- The account is fictional and used solely for educational reporting

## 8. Limitations and Risks
- **Data format sensitivity:** if `precios.csv` does not match expected schema, the simulation may fail.
- **Simplified market model:** unless implemented, no fees, slippage, spreads, or execution constraints.
- **No statistical validation:** results should not be interpreted as predictive or tradable.

## 9. Future Improvements (Roadmap Ideas)
- Add optional export to CSV/JSON for:
  - summary metrics
  - trade logs
- Add command-line arguments to avoid interactive prompts:
  - `--saldo-inicial`, `--max-operaciones`, `--csv`
- Improve error messages for malformed `precios.csv`
- Implement basic tests (input validation, deterministic runs on fixed data)
- Document the exact expected CSV schema (columns, types, timeframe)

## 10. Repository Hygiene (Recommended)
- Add:
  - `LICENSE`
  - `.gitignore`
  - sample dataset (or instructions to obtain/prepare `precios.csv`)
  - `requirements.txt` (if dependencies exist)
  - a `docs/` folder for expanded explanations and examples
