import os
from pathlib import Path
from ecflow import Defs, Suite, Task, Family, Edit, Trigger, \
    Event, Complete, Meter, Time, Day, Date, Cron, Label, \
    RepeatString, RepeatInteger, RepeatDate, Limit, InLimit, \
    Late


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


def create_family_f4():
    return Family("f4",
                  Edit(SLEEP=2),
                  RepeatString("NAME", ["a", "b", "c", "d", "e", "f"]),
                  Family("f5",
                         RepeatInteger("VALUE", 1, 10),
                         Task("t1",
                              RepeatDate("DATE", 20101230, 20110105),
                              Label("info", ""),
                              Label("date", "")
                              )
                         )
                  )


def create_family_f5():
    return Family("f5",
                  InLimit("l1"),
                  Edit(SLEEP=20),
                  [Task('t{}'.format(i)) for i in range(1, 10)])


def create_family_f6():
    return Family("f6",
                  Edit(SLEEP=120),
                  Task('t1',
                       Late(complete="+00:01")))


print("Creating suite definition")
home = os.path.abspath(Path(Path(__file__).parent, "../../../build/course"))
defs = Defs(
    Suite('test',
          Edit(ECF_INCLUDE=home, ECF_HOME=home),
          Limit("l1", 2),
          create_family_f1(),
          create_family_house_keeping(),
          create_family_f3(),
          create_family_f4(),
          create_family_f5(),
          create_family_f6()))
print(defs)

print("Checking job creation: .ecf -> .job0")
print(defs.check_job_creation())

print("Saving definition to file 'test.def'")
defs.save_as_defs(str(Path(home, "test.def")))

# To restore the definition from file 'test.def' we can use:
# restored_defs = ecflow.Defs("test.def")
