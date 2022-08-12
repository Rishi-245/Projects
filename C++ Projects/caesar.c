#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cs50.h>
#include <ctype.h>

// Check the number of keys entered by user
bool number_keys(string c)
{
    for (int var = 0, array = strlen(c); var < array; var++)
        if (!isdigit(c[var]))
        return false;
    return true;
}

// Main Function
int main(int argc, string argv[])
{

    // Change ASCII to an integer using atoi
    int var_key = atoi(argv[1]);

    // Getting User's Input for the "plaintext"
    string text = get_string("Plaintext: ");

    // Printing the Ciphertext on Screen
    printf("Ciphertext: ");
    for (int var = 0, array = strlen(text); var < array; var++)
    {
        // Checking for an alphabet versus punctuation
        char a = text[var];
        if (isalpha(a))
        {
            char b = 'A';
            if(islower(a))
                b = 'a';
            printf("%c", (a - b + var_key) % 26 + b);

        }
        else
            printf("%c", a);
    }
    
    printf("\n");

    // Print the correct method of inserting key
    if (argc != 2 || !number_keys(argv[1]))
    {
        printf("Usage ./caesar key\n");
        return 1;
    }
}
