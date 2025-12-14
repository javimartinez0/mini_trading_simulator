# Trading Algorithm Simulator (Learning Project)

## What this is
A small **Python** project that simulates a trading algorithm run: it executes a set of operations, records them, and updates a **fictional trading account** to produce a final performance summary.

## Why it exists
This repository was built as an early learning project to practice:
- Python programming fundamentals
- Basic trading-system workflow (operations → PnL → account balance)
- Simple project structure and documentation

## How to run
From the project root (the folder containing `Resumen_final.py`):

```bash
python Resumen_final.py
```

The script will prompt you for:
- **Initial balance** (non‑negative number)
- **Number of operations** to simulate (optional; press Enter to run all)

## Inputs
- `precios.csv` (expected in the project root)
- Simulation logic is executed via `Dsimulador_ejecucion.ejecutar_trading(...)`

## Output
- Console summary (initial balance, final balance, counts, total PnL)
- Per-operation log printed to the console

## Disclaimer
Educational project only. Not financial advice. Not intended for live trading or profitability.

## License
Add a license file (e.g., MIT) if you want to clarify reuse permissions.

## Project structure
    
```text
.
├── pyproject.toml
├── README.md
├── PROJECT_BRIEF.md
├── src/
│   ├── __init__.py
│   └── Cargar_y_limpiar_csv.py
|   └── Cuenta_de_trading.py
|   └── Generar_senales.py
|   └── Resumen_final.py
|   └── Simulador_ejecucion.py    
├── data/
    └── prices.csv
```

