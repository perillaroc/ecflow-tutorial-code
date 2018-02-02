import os
from pathlib import Path
from ecflow import Defs, Suite, Task, Family, Edit, Trigger, \
    Event, Complete, Meter, Time, Day, Date, Cron, Label


def create_family_f1():
    return Family(
        "f1",
        Edit(SLEEP=20),
        Task("t1",
             Time("03:00 23:00 00:30")),
        Task("t2",
             Day("sunday")),
        Task("t3",
             Date("1.*.*"),
             Time("12:00")
             ),
        Task("t4",
             Time("+00:02")),
        Task("t5",
             Time("00:02"))
    )


def create_family_house_keeping():
    return Family("house_keeping",
                  Task("clear_log",
                       Cron("22:30", days_of_week=[0])))


def create_family_f3():
    return Family("f3",
                  Task("t1",
                       Label("info", "")))


print("Creating suite definition")
home = os.path.abspath(Path(Path(__file__).parent, "../../../build/course"))
defs = Defs(
    Suite('test',
          Edit(ECF_INCLUDE=home, ECF_HOME=home),
          create_family_f1(),
          create_family_house_keeping(),
          create_family_f3()))
print(defs)

print("Checking job creation: .ecf -> .job0")
print(defs.check_job_creation())

print("Saving definition to file 'test.def'")
defs.save_as_defs(str(Path(home, "test.def")))

# To restore the definition from file 'test.def' we can use:
# restored_defs = ecflow.Defs("test.def")
