import sys

# Read the lines from the file
file = open(sys.argv[1], "r")
lines = file.read().splitlines()[1:]

# Initially there are no groups
groups = {}

# Process each line
for line in lines:
    # Split out the data. The first cell is the song_file, then the year, then the cycle, then everyrthing else is the units
    cells = line.split(",")
    song_file = cells[0]
    year = cells[1]
    cycle = cells[2]
    theme = cells[3]
    units = cells[4:]
    units = [u for u in units if u != '']
    if (song_file, cycle) in groups:
        # If the (song_file, cycle) tuple has been seen before, add the units to it
        groups[(song_file, cycle)].extend(units)
    else:
        # Otherwise, create a new entry in the map of groups
        groups[(song_file, cycle)] = units

# Print out the result
for (song_file, cycle) in groups:
    # Get rid of duplicates here
    units = groups[(song_file, cycle)]
    unique_units = list(set(units))
    # Print the output
    #print(f"{song_file} {cycle} has {len(units)} units in total, of which {len(unique_units)} are unique units: {unique_units}")
    print(f"{song_file},{cycle},{len(units)},{len(unique_units)},{','.join(unique_units)}")
