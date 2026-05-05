#include <stdio.h>
#include <unistd.h>

// ** No more helper function this time UwU **
//
// void UwU_flag() {
//     int flag_len = 61;
//     char flag[flag_len];
//     puts("You proved yourself! Let me give you the flag (=^-ω-^=)");
//     FILE *fp = fopen("flag.txt", "r");
//     if (fp == NULL) {
//         puts("flag.txt file is missing... (′゜ω。‵)");
//         exit(0);
//     }
//     fgets(flag, flag_len, fp);
//     puts(flag);
// }

void UwU_main() {
    char buffer[0x10];
    puts("Welcome to the world of UwU 2.0!! ▼・ᴥ・▼");
    puts("You can write something in the buffer for me UwU");
    fgets(buffer, 0x8, stdin);
    printf(buffer);
    puts("Try to get the flag by writing something in the buffer again for me UwU");
    fgets(buffer, 0x60, stdin);
}

int main() {
    setvbuf(stdin, NULL, 2, 0);
    setvbuf(stdout, NULL, 2, 0);
    setvbuf(stderr, NULL, 2, 0);
    UwU_main();
    puts("See you next time!!（๑ • ‿ • ๑ ）");
    return 0;
}

void gift() {
    __asm__("pop %rdi;"
            "ret;");
}