#include<stdio.h>
#include<string.h>
#include<unistd.h>
#include<stdlib.h>

int main(int argc, char** argv)
{
    //command line args verification
    if (argc == 1)
    {
        printf("\nNo Extra Command Line Argument Passed \n");
        return 0;
    }

    char str[26];
    strncpy(str,argv[1],26);
    char res[26];
    int i=0;

	//text scroll function starts here...
    while(str[i]!='\0')
    {
        int ascii=32;
        while(str[i]+1!=ascii)
        {
            res[i]=ascii;
            res[i+1]='\0';
            printf("%s\n",res);
            usleep(35000);
            system("clear");
            ascii++;
        }
        i++;
    }
    printf("%s\n",res);
    return 0;
}
