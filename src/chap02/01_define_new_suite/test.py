import os
from pathlib import Path
from ecflow import Defs, Suite, Task, Edit

print("Creating suite definition")
home = os.path.abspath(Path(Path(__file__).parent, "../../../build/course"))
defs = Defs(
    Suite('test',
          Edit(ECF_HOME=home),
          Task('t1')))
print(defs)
