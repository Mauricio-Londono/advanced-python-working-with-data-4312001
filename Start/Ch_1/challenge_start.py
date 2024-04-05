# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json

# open the data file and load the JSON
with open("/workspaces/advanced-python-working-with-data-4312001/30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
print(f"Total quakes: {data['metadata']['count']}")

# 2: How many quakes were felt by at least 100 people?
def quakes_felt(q):
    f = q["properties"]["felt"]
    return (f is not None and f >= 100)

feltreports = list(filter(quakes_felt, data["features"]))
print(f"Total quakes felt by at least 100 people: {len(feltreports)}")

# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
def get_felt(q):
    f = q["properties"]["felt"]
    if f is not None:
        return f
    return 0

mostfeltquake = max(data["features"], key=get_felt)
print(f"Most felt reports: {mostfeltquake['properties']['title']}, reports: {mostfeltquake['properties']['felt']}")

# 4: Print the top 10 most significant events, with the significance value of each
def getsigevents(q):
    s = q["properties"]["sig"]
    if s is not None:
        return s
    return 0

sigevents = sorted(data["features"], key=getsigevents, reverse=True)

for i in range(0,10):
    print(f"Event: {sigevents[i]['properties']['title']}, Significance: {sigevents[i]['properties']['sig']}")


    