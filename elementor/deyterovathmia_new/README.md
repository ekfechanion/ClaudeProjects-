# δευτεροβαθμια_new (page ID 22627)

Clean Elementor V4 (atomic) rebuild of https://ekfechanion.eu/deyterovathmia/ (ID 15778).
The original page stays untouched.

- `acc.json`: accordion content extracted from the original page (titles, descriptions, links)
- `gen.py`: builds the subjects section (Φυσική / Χημεία / Βιολογία accordions)
- `gen2.py`: adds the resources lists, divider and bottom buttons, writes `build.json`
- `mcp.py`: minimal client for the site's Elementor MCP endpoint

Rebuild: `python3 gen.py && python3 gen2.py && python3 mcp.py elementor-build-composition build.json`
(replaces the whole page content).

Styling lives in global classes `ekfe-*` and global variables (`ekfe-blue`, `ekfe-text`, `ekfe-font-body`, ...).
