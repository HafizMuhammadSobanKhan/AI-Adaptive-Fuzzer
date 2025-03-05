#include <stdio.h>
#include <string.h>

void vulnerable_function(char *input) {
    char buffer[64];
    strcpy(buffer, input); // Intentional buffer overflow
    printf("Input received: %s\n", buffer);
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <input>\n", argv[0]);
        return 1;
    }
    
    // INTENTIONAL CRASH TRIGGER
    if (strlen(argv[1]) > 80) {
        char *ptr = NULL;
        *ptr = 'X';  // Causes a segmentation fault
    }

    vulnerable_function(argv[1]);
    return 0;
}
