# NestThermostatHeatCoolAnalyzer
Simple tool to load in the JSON provided from Google Takeout to visualize the Heat/Cool information by month.

## Setup
1. Clone repository
2. Create a virtual environment
  * `python3 -m venv .venv`
3. Activate virtual environment
  * Windows - `.\.venv\Script\activate`
  * Linux (bash) - `source .venv/bin/activate`
4. Install libraries
  * `pip install -r requirements.txt`
5. Move Nest data into data folder, from the year folder
6. Run the tool
  * Windows - `python3 .\main.py`
  * Linux - `python3 ./main.py`