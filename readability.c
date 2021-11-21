#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int main(void)
{
    // Different integers values in use
    int words = 0;
    int sentences = 0;
    int letters = 0;
    
    // Gather text from user
    string s = get_string("Enter Text: ");
  
    //Determine the number of sentences, words, and letters
    for (int var = 0, array = strlen(s); var < array; var++)
    {
        // Calculating the number of words depending on placement on an array
        if ((s[var + 1] != ' ' && s[var] == ' ' && var != array - 1) || (s[var] != ' ' && var == 0))
            words++;
        
       // Calculating the number of letters depending on placement on an array
       if (isalpha(s[var]))
            letters++;
            
      // Calculating the number of sentences depending on placement on an array
       if (s[var] == '.' || s[var] == '?' || s[var] == '!')
            sentences++;
    }


    // CALCULATING THE OVERALL GRADE LEVEL OF TEXT:

    // Determine variables in the Coleman Liau index formula
    float L = ((float) letters / (float) words) * 100;
    float S = ((float) sentences / (float) words) * 100;
   
    // Coleman Liau formula
    int index = round(0.0588 * L - 0.296 * S - 15.8);
    
    // Indicating what to print
    if (index < 1)
        printf("Before Grade 1\n");
        
    else if (index >= 16)
        printf("Grade 16+\n");
        
    else
        printf("Grade %i\n", index);
        
}
