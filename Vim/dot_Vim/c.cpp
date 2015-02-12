#include <stdio.h>
int very_long_variable_1;
int very_long_variable_2;
int very_long_variable_3;
int very_long_variable_4;

#ifdef USE_POPEN
    fd = popen("ls", "r")
#else
    fd = fopen("tmp", "w")
#endif

#if defined(HAS_INC_H)
    a = a + inc();
#ifedf USE_THEME
    a += 3
#endif 
    set_width(a);

function(int a)
{
    if (a)
    {
        for (;;)
        {
            foo(32);
            if (bar(a))
                break;
        }
        foobar(a);
    }
}

int func1(void)
{
    return 1;
} 

int func2(void)
{
    if (flag)
        return flag;   
    return 2;
}

int func3(void)
{
    return 3;
}

int main() {
    very_long_variable_4 = very_long_variable_1 * very_long_variable_2;
}
