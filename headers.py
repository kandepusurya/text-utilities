import pandas as pd
import sys

# Check if the filename is provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python script_name.py <filename>")
    sys.exit(1)

# The first command-line argument is the script name, so the second one is the filename
file_path = sys.argv[1]

# Read the tab-delimited file without headers
df = pd.read_csv(file_path, header=None, sep='\t')

# Print the number of columns found
print(f"Number of columns in the file: {df.shape[1]}")

# Here are the column names based on the provided PDF file, ensure they match the number printed above
column_names = [
    "Precinct County Code", "Precinct County Name", "Precinct Election Number", 
    "Precinct Election Date", "Precinct Election Name", "Precinct Unique Precinct Identifier",
    "Precinct Precinct Polling Location", "Precinct Total Registered Voters", 
    "Precinct Total Registered Republicans", "Precinct Total Registered Democrats", 
    "Precinct Total Registered All Other Parties", "Contest Contest Name", 
    "Contest District", "Contest Contest Code", "Votes Candidate/Retention/Issue Name/WriteInsCast/OverVotes/UnderVotes",
    "Votes Candidate Party", "Votes Candidate Florida Voter Registration System ID Number", 
    "Votes DOE Assigned Candidate Number or Retention/Issue Number",
    "Votes Vote Total"
]

# If the number of columns match, assign the column names and save the file
if len(column_names) == df.shape[1]:
    df.columns = column_names
    # Save the dataframe back to CSV with column names, tab-delimited
    df.to_csv(file_path, index=False, sep='\t')
else:
    print("The number of columns in the CSV does not match the number of column names provided.")
