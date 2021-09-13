import os
import sys

subset_folder = sys.argv[1]
superset_folder = sys.argv[2]
output_folder = sys.argv[3]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

subset_strings = [s.split('.')[0] for s in os.listdir(subset_folder) if s.endswith('.obj')]
superset_names = [s for s in os.listdir(superset_folder) if s.endswith('.obj')]

for string1 in subset_strings:
    for string2 in subset_strings:
        if string1 == string2:
            continue
        print(string1,string2)
        for name in superset_names:
            if string1 in name and string2 in name:
                superset_path = os.path.join(superset_folder,name)
                destination_path = os.path.join(output_folder,name)
                os.system("cp " + superset_path + " " + destination_path)