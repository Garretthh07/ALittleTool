#include "stdio.h"
#include "iostream"
using namespace std;


void write_block(char **s, int cnt) {
    int i;
    for (i = 0; i < cnt; ++i)
        write_line(s[i]);
}

void init() 
{
    int i,j,k;
    int mask = 0;
    int dp[1000][10];
    for (i = 0; i < 1000 ; i++)
    {
        for (j = 0; j < 10; j++)
        {
        }
    }
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
