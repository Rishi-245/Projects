#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //All variables used
    int Height;
    int blankspaces;
    int hashes;

    // Prompt user to enter pyramid height
    do
    {
        Height = get_int("Height: ");

    }
    while (Height > 8 || Height < 1);

    //Construct the pyramid using hashes & spaces
    for (hashes = 0; hashes < Height; hashes++)
    {
        for (blankspaces = 0; blankspaces < Height; blankspaces++)
        {

            if (blankspaces + hashes < Height - 2 + 1)
               printf(" ");
            else

                printf("#");
        }
            printf("\n");
    }
}
