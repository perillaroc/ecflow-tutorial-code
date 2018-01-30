import os
from pathlib import Path
from ecflow import Defs, Suite, Task, Edit, Client

print("Creating suite definition")
home = os.path.abspath(Path(Path(__file__).parent, "../../../build/course"))
defs = Defs(
    Suite('test',
          Edit(ECF_HOME=home),
          Task('t1')))
print(defs)

print("Checking job creation: .ecf -> .job0")
print(defs.check_job_creation())

print("Saving definition to file 'test.def'")
defs.save_as_defs(str(Path(home, "test.def")))

try:
    print("Load the in memory definition(defs) into the server")
    ci = Client('login05', '33083')
    ci.load(defs)
except RuntimeError as e:
    print("Failed:", e)
