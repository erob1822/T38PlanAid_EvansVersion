# T-38 PlanAid (Evans Edition)

## BLUF

The T-38 PlanAid tool streamlines the flight planning process by highlighting airports that meet key requirements for cross country ops:

- 7000 ft Landing Distance Available (LDA)
- Contract Gas
- Jet Air Start Unit (JASU or "Air-Start Cart")

## Overview

This is a flight planning tool (not intended for in flight use) developed by RPL Military interns with CB's support. It gathers and organizes data from the FAA, Defense Logistics Agency (DLA), and NASA AOD APIs, then produces a KML file (`T38 Apts DD Mon YYYY.kml`). The KML file includes color-coded airport pins based on the data, helping with flight planning in ForeFlight or other EFBs.

This is an updated version of the main T38 PlanAid with changes made to increase efficiency and modularity — uses only three scripts instead of five, with about half the lines of code. Also includes `build_exe.py` which automatically creates a distribution-ready `.exe`. Fully functional as of 1/27/2026.

## To Generate a .KML file for Cross Country Planning

Just double-click `T-38 Planning Aid.exe` — no other files needed. On first run, it extracts `wb_list.xlsx` automatically. To used cached data, the app will have to run in the same folder as a preexisting `T38 Planning Aid` folder. This will save about a minute if current data already exists from a previous run.

All output goes into a `T38 Planning Aid/` folder created next to the exe:
- `T38 Planning Aid/KML_Output/` — your `.kml` files
- `T38 Planning Aid/DATA/` — cached FAA data
- `T38 Planning Aid/wb_list.xlsx` — airport lists (editable)

The KML output path is printed at the end of each run. Open the `.kml` in ForeFlight, Google Earth, or KMZViewer.com.

## For Distribution

To build a standalone `.exe` for distribution, open a terminal in the project folder and run:

```cmd
python build_exe.py
```

Or, with Python installed, just double-click `build_exe.py`.

This creates the folder `T38 PlanAid Distribution/` containing:
- `T-38 Planning Aid.exe` — standalone executable (can be distributed on its own)
- `T38 Planning Aid/` — pre-populated with cached data and `wb_list.xlsx`

The exe bundles `wb_list.xlsx` internally and extracts it on first run if not present. You can distribute just the `.exe` by itself — or include the `T38 Planning Aid/` folder for faster first-run performance (skips re-downloading cached data).

> **Note:** To use cached data, the `T38 Planning Aid/` folder (containing `DATA/`) must be next to the `.exe`. If the exe is moved without the folder, it will re-download everything on the next run.

## Quick Start (For Development)

```cmd
pip install -r requirements.txt
python T38_PlanAid.py
```

Output: `T38 Planning Aid/KML_Output/T38 Apts {date}.kml` — usable in ForeFlight.

## Files

| File | Purpose |
|------|---------|
| `T38_PlanAid.py` | Master script - run this. Contains all config (URLs, version, paths) |
| `Data_Acquisition.py` | Downloads data from AOD, FAA, DLA APIs |
| `KML_Generator.py` | Builds airport database and generates KML |
| `build_exe.py` | Builds standalone `.exe` and packages distribution folder |
| `wb_list.xlsx` | Blacklist, whitelist, categories, comments, recent landings |

## Quick modifications for other use cases

| To change... | Edit this |
|--------------|-----------|
| Version string on KML | `T38_PlanAid.py` → `AppConfig.version` |
| Minimum runway length | `KML_Generator.py` → search `# MODIFY: runway threshold` |
| Pin colors/logic | `KML_Generator.py` → search `# MODIFY: pin color` |
| Add/remove airports | `wb_list.xlsx` → BLACKLIST, WHITELIST, CAT_ONE/TWO/THREE columns |
| API URLs | `T38_PlanAid.py` → `AppConfig` class variables |

## Pin Colors

- **Blue**: JASU listed but no recent ops - otherwise good to go
- **Yellow**: No JASU listed - call FBO to verify cart
- **Green**: Recently landed by T-38 - known to work  
- **Red diamond**: Category 2/3 - extra planning required
- **Red circle**: Category 1 - T-38 ops prohibited

## Dependencies

See `requirements.txt`. Key packages: `pandas`, `simplekml`, `requests`, `requests-ntlm`, `openpyxl`, `PyMuPDF`, `colorlog`, `tqdm`

## Troubleshooting

- **File Issues**: `wb_list.xlsx` is auto-extracted on first run. If it gets corrupted, delete it from `T38 Planning Aid/` and the exe will regenerate it. Revert to a backup if you've made custom edits.
- **URL Changes**: If FAA or DLA URLs change, update the endpoints in `T38_PlanAid.py` → `AppConfig` class variables.
- **API Issues**: Contact AOD IT if API paths are down or outdated. Update the relevant URL in `T38_PlanAid.py` → `AppConfig`.

## Contact Info and Attributions

### RPL Military Interns (Authors / Developers)

- Nicholas Bostock [API scraping and AOD integration]
- Jacob Cates [Scraping websites and downloading/packaging data]
- Alex Clark, +1(469) 406-8546 (POC AUG2024)
- Alec Engl, +1(727) 488-0507 aengl5337@gmail.com (POC NOV2025)
- Ignatius Liberto, 757-373-8787, ignatiusliberto@gmail.com (POC NOV2024) [AFD Scraping, data harvesting, LDA logic, KML Generation]
- Adrien Richez, +1(678) 788-4015, adrichez24@gmail.com (POC SEP2024) [API scraping and AOD integration]
- Evan Robertson +1 (410) 507-6109, erob1822@gmail.com (POC FEB2026) [.exe generation and v3.0 integration]
- James Zuzelski, +1(248) 930-3461, (POC JUN2024)

### CB / AOD POCs

- Sean Brady
- Dan Cochran
- Luke Delaney
- Jonny Kim
