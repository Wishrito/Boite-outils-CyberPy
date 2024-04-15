import random
from time import sleep

from win11toast import notify, update_progress

notify(progress={
    'title': 'CyberToolbox',
    'status': 'loading',
    'value': '0',
    'valueStringOverride': ''
})
process_statuses = [
    "Extracting files...",
    "Loading Bootstrap...",
    "Initializing user interface...",
    "Loading data...",
    "Analyzing files...",
    "Optimizing performance...",
    "Reorganizing resources...",
    "Verifying file integrity...",
    "Validating settings...",
    "Finalizing process..."
]

for i in range(1, len(process_statuses) + 1):
    randInt = random.randint(1, 3)
    randStatus = random.choice(process_statuses)
    sleep(randInt)
    update_progress({'value': i/10,
                    'valueStringOverride': randStatus})
    process_statuses.remove(randStatus)

update_progress({'status': 'Completed!', 'valueStringOverride': ""})
