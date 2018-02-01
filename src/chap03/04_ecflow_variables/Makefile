all: script

.PHONY: script def replace

script:
	test -d ${ECF_HOME} || mkdir -p ${ECF_HOME}
	cp -r test ${ECF_HOME}


def:
	python test.py


replace:
	ecflow_client --host=login05 --port=33083 --replace=/test ${ECF_HOME}/test.def