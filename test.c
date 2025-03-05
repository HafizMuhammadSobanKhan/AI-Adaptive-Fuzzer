#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <input>\n", argv[0]);
        return 1;
    }
    if (strcmp(argv[1], "fuzzme") == 0) {
        printf("You found the crash!\n");
        *(char *)0 = 0; // Intentional crash
    }
    return 0;
}
