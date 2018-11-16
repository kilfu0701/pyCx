clean:
	rm -rf ./build ./dist ./pyCx.egg-info

build_sdist:
	python setup.py sdist

upload_to_pypi:
	twine upload dist/*.tar.gz
