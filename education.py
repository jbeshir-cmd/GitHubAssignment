"""
JEMAL BESHIR
"""
import argparse
import pandas as pd
import sys

def most_educated(csv_path, state_code):
    """
    Finds the county with the highest percentage of adults with a bachelor's degree or higher
    in the given state.

    Args:
            csv_path (str): Path to the CSV file with educationl data.
            state_code (str): Two-letter state abbrev.

    Returns:
            tuple: (county name, percentage of adults with a bachelor's degree or higher).
    """
    df = pd.read_csv(csv_path)
    st_filt =  df["State"] == state_code
    state_df =  df[st_filt]
    max_percent  = state_df["Percent of adults with a bachelor's degree or higher"].max()
    top_county =  state_df[state_df["Percent of adults with a bachelor's degree or higher"] == max_percent]
    county_name = top_county["Area name"].values[0]
    return  county_name, max_percent

def parse_args(args_list):
    """
        Parses command-line arguments.

    Args:
        args_list (list): List of command-line arguments.

    Returns:
        Namespace: Parsed arguments containing CSV path and state code.
    """
    parser =  argparse.ArgumentParser()
    parser.add_argument("csv_path")
    parser.add_argument("state_code")
    return parser.parse_args(args_list)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    county, percent =  most_educated(args.csv_path,  args.state_code)
    print(percent, "% of adults in", county, "have at least a bachelor's degree.")
