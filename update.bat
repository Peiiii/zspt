del "dist\*.gz" /f
del "dist\*.whl" /f
rmdir "build" /s/q
del "zspt.egg-info\*" /r/f
python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/*
