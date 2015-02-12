#include "stdio.h"
#include "iostream"
using namespace std;


void write_block(char **s, int cnt) {
    int i;
    for (i = 0; i < cnt; ++i)
        write_line(s[i]);
}

int main() 
{
    int i=3;
    do_sub("foo");
    ++i;


    if (flag)
        do_the_work();
    if (other_flag) {
        do_file();
        do_some_more();
    }
    return (0);
}
