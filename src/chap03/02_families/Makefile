all: script

.PHONY: script load delete replace replace_part begin

clean:
	test -d ${ECF_HOME} || mkdir -p ${ECF_HOME}
	rm -rf ${ECF_HOME}/test

script:
	test -d ${ECF_HOME} || mkdir -p ${ECF_HOME}
	cp -r test ${ECF_HOME}


def:
	python test.py


replace:
	ecflow_client --host=login05 --port=33083 --replace=/test ../../../build/course/test.def