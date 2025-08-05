#include <stdio.h>

int main(void)
{

    printf("Hello World\n");
}

> code hello.c       // to make file
        > make hello // to compile it
        >./ hello    // to run it

    == == == == == == == == == == == == == == == == == == ==
#include <cs50.h>
#include <stdio.h>

    int main(void)
{

    string answer = get_string("what is your name? ");
    printf("Hello, %s\n", answer);
}

== == == == == == == == == == == == == == == == == == == =

#include <cs50.h>
#include <stdio.h>

int main(void)
{

    int x = get_int("vlaue of x?");
    int y = get_int("vlaue of y?");
    if (x < y)
    {
        printf("x is less than y\n");
    }
    else if (x > y)
    {
        printf("x is not less than y\n");
    }
    else
    {
        printf("Both are equal\n");
    }
}
== == == == == == == == == == == == == == == == == == == == == =

#include <cs50.h>
#include <stdio.h>

int main(void)
{

    char c = get_char("Enter character? ");
    if (c == 'y' || c == 'Y')
    {
        printf("Agreed\n");
    }
    if (c == 'n' || c == 'N')
    {
        printf("Not Agreed\n");
    }
}

== == == == == == == == == == == == == == == == == == == == == ==

#include <cs50.h>
#include <stdio.h>

    int main(void)
{

    int i;
    int max = 3;

    for (i = 0, i <= max, i++)
    {
        printf("meow\n")
    }
}

// in while loop

int main(void)
{

    int i = 1;
    while (i <= 3)
    {
        prinf("meow\n")
            i++;
    }
}
== == == == == == == == == == == == == == == == == == == == == ==

#include <cs50.h>
#include <stdio.h>

void mewo(void);
int main(void)
{
    for (int i = 0, i <3, i++)
    {
        mewo();
    }


}

void mewo(void)
{
    printf("meow\n");
}

//do while
int main(void)
{
    int n;
    do{
        n = get_int("vlaue of n?");
    }
    while (n<1)
    {
        
        
    }
    


}
