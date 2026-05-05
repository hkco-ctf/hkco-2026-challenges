/* get_key.c -- helper for the solver.
 *
 * Reproduces the 16-byte AES key that the challenge builds by calling rand()
 * 16 times without ever calling srand().  Compile and run:
 *
 *     gcc get_key.c -o get_key
 *     ./get_key
 *
 * Paste the printed hex into solve.py.
 */

#include <stdio.h>
#include <stdlib.h>

int main(void) {
    for (int i = 0; i < 16; i++) {
        printf("%02x", rand() & 0xff);
    }
    printf("\n");
    return 0;
}
