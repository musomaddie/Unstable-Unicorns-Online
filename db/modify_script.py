import csv

def _file_dict_reading(filename):
    with open(filename, newline='') as f:
        reader = csv.DictReader(f, dialect='excel-tab')
        return [row for row in reader]

def _change_value(uni, key):
    value = uni[key]
    if value == "None":
        uni[key] = False
    else:
        uni[key] = True

def fix_boolean(uni, key):
    if uni[key] == "TRUE":
        uni[key] = True
    else:
        uni[key] = False

unicorn_info = _file_dict_reading("UnicornDetails.tsv")
keys = unicorn_info[0].keys()

for uni in unicorn_info:
    fix_boolean(uni, "Action on Enter Stable")
    fix_boolean(uni, "Beginning of Turn Action")
    _change_value(uni, "Discard Action")
    fix_boolean(uni, "In Stable Effect")
    _change_value(uni, "Search Deck")
    fix_boolean(uni, "Shuffle Deck")
    fix_boolean(uni, "Shuffle Discard Into Deck")
    _change_value(uni, "Sacrifice")
    fix_boolean(uni, "Return to Hand")
    _change_value(uni, "Search Discard")
    _change_value(uni, "Protection")
    if uni["Draw"] == 0:
        uni["Draw"] = False
    else:
        uni["Draw"] = True
    _change_value(uni, "Destroy")
    fix_boolean(uni, "Requires Basic Unicorn")
    fix_boolean(uni, "Action on Leave")

# Write new file
with open("UnicornDetails_fixed.tsv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=unicorn_info[0].keys(),
            dialect='excel-tab')
    writer.writeheader()
    for uni in unicorn_info:
        writer.writerow(uni)
