clean:
	rm -rf ./build ./dist ./pyCx.egg-info

build:
	python setup.py sdist

upload:
	twine upload dist/*.tar.gz
