CC      := gcc
CFLAGS  := -O2
LDLIBS  := -lcrypto

chall: chall.c
	$(CC) $(CFLAGS) chall.c -o chall $(LDLIBS)

clean:
	rm -f chall
