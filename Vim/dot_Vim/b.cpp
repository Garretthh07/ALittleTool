This is b.cpp
#include "inits.h"
void init() {

}

void write_line(char *s) {
    while (*s != 0)
        write_char(*s++);
}

int main() {
    int a;
    while(scanf("%d",&a) != EOF) {
        /*
         * This is a test of the text formatting
         * Typing a lot of text here will make Vim
         * break
         */
        /*
         *
         */
        init();
        exec();
    }
    return 0;
}
