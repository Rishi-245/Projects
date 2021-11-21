#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    
    float Change;
    int cents;
    int number_coins;

    // Ask for user's input of change
    do
    {
        Change = get_float("Change Owed: ");
    }
    while (Change < 0);

    // Rounding the change
    cents = round(Change * 100);

    // Calulating the minimum # of coins
    number_coins = 0;

    // Check for 25 cents
    while (cents >= 25)
    {
        cents -= 25;
        number_coins++;
    }

    // Check for 10 cents
    while (cents >= 10)
    {
        cents -= 10;
        number_coins++;
    }
    
    // Check for 5 cents
    while (cents >= 5)
    {
        cents -= 5;
        number_coins++;
    }

    // Check for 1 cent
    while (cents >= 1)
    {
        cents -= 1;
        number_coins++;
    }
    
    // Print the number of coins
    printf("Number of Coins: %i\n", number_coins);
}
