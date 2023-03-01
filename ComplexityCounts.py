import sys

# Read the lines from the file
file = open(sys.argv[1], "r")
lines = file.read().splitlines()[1:]

# Initially there are no groups
unit_groups = {}
theme_groups = {}

# Process each line
for line in lines:
    # Split out the data. The first cell is the song_file, then the year, then the cycle, then everyrthing else is the units
    cells = line.split(",")
    song_file, identity, year, song_type, song_duration, cycle, theme, *units = cells
    units = [u for u in units if u != '']
    song_id = (song_file, identity, year, song_type)
    existing = [x for x in unit_groups if x[0:2] == (song_id, cycle)]
    if len(existing):
        _, _, existing_duration = existing[0];
        # If the (song_id, cycle) tuple has been seen before, add the units to it
        unit_groups[(song_id, cycle, existing_duration)].extend(units)
    else:
        # Otherwise, create a new entry in the map of groups
        unit_groups[(song_id, cycle, song_duration)] = units

    existing = [x for x in theme_groups if x[0:2] == (song_id, cycle)]
    if len(existing):
        _, _, existing_duration = existing[0];
        # If the (song_id, cycle) tuple has been seen before, add the theme to it
        theme_groups[(song_id, cycle, existing_duration)].extend([theme])
    else:
        # Otherwise, create a new entry in the map of theme groups
        theme_groups[(song_id, cycle, song_duration)] = [theme]



# Print out the result
for (song_id, cycle, song_duration) in unit_groups:
    # Get rid of duplicates here
    units = unit_groups[(song_id, cycle, song_duration)]
    unique_units = list(set(units))
    (song_file, identity, year, song_type) = song_id
    # Print the output which is: song file, song cycle, total #units in song cycle, #unique units in song cycle, list of unique units.  
    #print(f"{song_file} {identity} {year} {song_type} {cycle} has {len(units)} units in total, of which {len(unique_units)} are unique units: {unique_units}")
    print(f"{song_file},{identity},{year},{song_type},{cycle},{song_duration},{len(units)},{len(unique_units)},{','.join(unique_units)}")

print()

for (song_id, cycle, song_duration) in theme_groups:
    # Get rid of duplicates here
    themes = theme_groups[(song_id, cycle, song_duration)]
    unique_themes = list(set(themes))
    (song_file, identity, year, song_type) = song_id
    # Print the output which is: song file, song cycle, #unique themes in song cycle, list of unique themes.  
    print(f"{song_file},{identity},{year},{song_type},{cycle},{song_duration},{len(unique_themes)},{','.join(unique_themes)}")
