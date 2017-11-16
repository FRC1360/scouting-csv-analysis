# scouting-csv-analysis
Scripts to analyze and aggregate CSV data exported from the new scouting system.

## picklist.py
Usage:

    python picklist.py <exported_csv_file_name> <climb_relative_weight> <gears_relative_weight>

Writes CSV to standard output with each row having the following columns:

- Team number
- Total climbs
- Total gears
- Climbs per match
- Gears per match
- Number of matches
- Weighted score
