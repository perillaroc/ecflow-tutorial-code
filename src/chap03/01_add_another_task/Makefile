all: script

.PHONY: script load delete replace replace_part begin

script:
	test -d ${ECF_HOME} || mkdir -p ${ECF_HOME}
	cp -r test ${ECF_HOME}

build: test.py
	python3 test.py

load:
	ecflow_client --host=login05 --port=33083 --load=../../../build/course/test.def

delete:
	ecflow_client --host=login05 --port=33083 --delete=_all_

replace:
	ecflow_client --host=login05 --port=33083 --replace=/test ../../../build/course/test.def

replace_part:
	ecflow_client --host=login05 --port=33083 --replace=/test/t2 ../../../build/course/test.def

begin:
	ecflow_client --host=login05 --port=33083 --begin=test