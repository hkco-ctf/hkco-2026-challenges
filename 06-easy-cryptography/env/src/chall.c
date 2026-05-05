#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>
#include <unistd.h>
#include <openssl/aes.h>
#include <openssl/md5.h>
#include <openssl/evp.h>

const int ROUNDS = 60;

// ========= Helper functions ==========

void init_io(void) {
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
    alarm(300);
}

void print_hex(const unsigned char *buf, size_t n) {
    for (size_t i = 0; i < n; i++) printf("%02x", buf[i]);
    printf("\n");
}

// ========= Main logic ==========

void do_enc1(const char* key, int num) {
    char pt[16];
    memset(pt, 0, sizeof(pt)); // Initialize the pt array with zeros

    // Left pad the decimal number with zeros to 7 digits
    // e.g. 123 becomes "0000123"
    snprintf(pt, 8, "%07u", num);

    AES_KEY ek;
    AES_set_encrypt_key(key, 128, &ek);
    char ct[16];
    AES_encrypt(pt, ct, &ek);

    print_hex(ct, 16);
}

void do_enc2(int num) {
    char enc[16];

    // Left pad the decimal number with zeros to 7 digits
    snprintf(enc, 8, "%07u", num);
    int len = 7;

    for (int i = 0; i < 2; i++) {
        char tmp[20];
        len = EVP_EncodeBlock(tmp, enc, len);
        memcpy(enc, tmp, len);
    }

    print_hex(enc, len);
}

void do_enc3(int num) {
    char pt[16];

    // Left pad the decimal number with zeros to 7 digits
    snprintf(pt, 8, "%07u", num);
    int len = 7;

    char ct[16];
    MD5(pt, len, ct);

    print_hex(ct, 16);
}

int main(void) {

    init_io();

    // Generate a random key for Enc 1
    char key[16];
    for (int i = 0; i < 16; i++) {
        // Lets use rand() to generate the key!
        key[i] = rand() & 0xff;
    }

    printf("============ Easy Encryption ============\n");
    printf("Welcome to the easy encryption challenge!\n");
    printf("Guess the number to get the flag!\n\n");

    for (int r = 0; r < ROUNDS; r++) {
        // Lets use timestamp to generate a random number! More secure, right?
        struct timespec ts;
        clock_gettime(CLOCK_REALTIME, &ts);
        int num = ts.tv_nsec % 10000000; // 0 to 9999999
        clock_gettime(CLOCK_REALTIME, &ts);
        int op = ts.tv_nsec % 3;

        printf("--------- Round %d ---------\n", r + 1);
        switch (op) {
            case 0: do_enc1(key, num); break;
            case 1: do_enc2(num);  break;
            case 2: do_enc3(num);   break;
        }

        printf("Your guess: ");
        
        int guess = 0;
        if (scanf("%d", &guess) != 1) {
            printf("Bad input, bye.\n");
            return 0;
        }
        if (guess != num) {
            printf("Wrong! The number was %u.\n", num);
            return 0;
        }
        printf("Correct!\n\n");
    }

    printf("Cleared all %d rounds -- nicely done!\n", ROUNDS);

    // Print the flag
    const char *flag = getenv("FLAG");
    if (!flag || !*flag) {
        printf("Flag is not configured.\n");
        return 0;
    }
    printf("\nHere is your flag: %s\n", flag);
    return 0;
}
