all: app.arm

app.arm: app.o
	gcc -g app.o -o app.arm

app.o: app.c
	gcc -g -c app.c -o app.o

clean:
	rm app.o app.arm