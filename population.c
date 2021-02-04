#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int p_start_size;
    int p_end_size;
    int years_passed = 0;
    
    // TODO: Prompt for start size
    
    do
    {
        p_start_size = get_int("Enter the starting population size\n");
    }
    while (p_start_size < 9);
    // TODO: Prompt for end size
    do
    {
        p_end_size = get_int("Enter the ending population size\n");
    }
    while (p_end_size < p_start_size);

    // TODO: Calculate number of years until we reach threshold
    while (p_start_size < p_end_size)
    {
        p_start_size = p_start_size + (p_start_size / 3) - (p_start_size / 4);
        years_passed++;
    }


    // TODO: Print number of years
    printf("Years: %i\n", years_passed);
}
