build: 
	# easycython fib_cy.py
	# easycython *.pyx
	python3 setup.py build_ext -if
clean: 
	rm -rf __pycache__
	rm -f *.so
	rm -f f*.c
	rm -rf build
	rm -f *.html
	rm -f prof*
	clear
