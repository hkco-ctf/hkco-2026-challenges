#include <stdio.h>
#include <unistd.h>

void UwU_flag() {
    int flag_len = 64;
    char flag[flag_len+1];
    puts("You proved yourself! Let me give you the flag (=^-ω-^=)");
    FILE *fp = fopen("flag.txt", "r");
    if (fp == NULL) {
        puts("flag.txt file is missing... (′゜ω。‵)");
        exit(0);
    }
    fgets(flag, flag_len+1, fp);
    puts(flag);
}

void UwU_main() {
    char buffer[0x10];
    puts("Welcome to the world of UwU!! ▼・ᴥ・▼");
    puts("Try to get the flag by writing something in the buffer for me UwU");
    fgets(buffer, 0x20, stdin);
}

int main() {
    setvbuf(stdin, NULL, 2, 0);
    setvbuf(stdout, NULL, 2, 0);
    setvbuf(stderr, NULL, 2, 0);
    UwU_main();
    puts("See you next time!!（๑ • ‿ • ๑ ）");
    return 0;
}