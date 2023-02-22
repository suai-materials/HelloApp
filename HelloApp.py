print("Hello Python from Visual Studio!")
s: str = "*" * 30
print(s)
print("New project")
print("")

import cProfile
import re

r = re.compile("\\d\\S")
cProfile.run("""[r.findall("sdfdsfD, 1d, 7f") for i in range(1000000)]""")
