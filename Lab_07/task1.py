from unsorted_table_map import UnsortedTableMap

import time

start_time = time.time()

dict = UnsortedTableMap()

dict[1] = "one"

print(dict[1])

end_time = time.time()

print("\nRunning time: ", end_time - start_time)