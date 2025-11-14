# Days Without

## How to Run

1. Install uv (if not already installed):

   **macOS/Linux:**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

   **Windows:**
   ```powershell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

3. Run the script:
   ```bash
   uv run add_numbers.py
   ```

This will generate numbered images in the `outputs/` directory.