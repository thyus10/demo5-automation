# CAPSTONE: MCP Playwright Pytest Example

## Project Structure

- `requirements.txt` - Python dependencies
- `pages/` - Page Object Model classes
- `features/` - Cucumber-style feature files and pytest test cases

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Ensure MCP server is running and configured for Playwright integration.
3. Run tests:
   ```bash
   PYTHONPATH=. pytest features/
   ```

## Notes
- This project demonstrates testing login functionality on `https://demo5.cybersoft.edu.vn/`.
- All browser automation is intended to be routed through MCP (see `mcp_launch_browser` in test_login.py).
- Update the MCP integration logic in `mcp_launch_browser` and `mcp_close_browser` as needed for your environment.
- Page object locators in `pages/` are examples and may need adjustment based on the actual website structure. 