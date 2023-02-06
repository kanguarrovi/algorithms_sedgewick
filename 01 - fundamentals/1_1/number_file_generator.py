from datetime import datetime

import random

try:
    now = datetime.now()
    
    timelog = now.strftime("%Y%m%d_%H%M%S")
    filename = f'number_file{timelog}.txt'
    
    print(filename)

    with open(filename, 'w') as f:
        for number in range(1000):
            random_int = random.randint(0, 1_000_000)
            f.write(f'{random_int}\n')

    print("File generated!")
except Exception as e:
    print(f'Error has happened.{e}')

