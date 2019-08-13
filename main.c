#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

char action[500];
char filename[500], nfilename[500], ss[500], task[500];
int ekey, inkey = 0;

int ssfinder(char *action, char *ss) {
    if(strstr(action, ss) == NULL)
        return 0;
    else
        return 1;
}

char* nameex(char *action) {
    int spos, j, len = 0;
    len = strlen(action);
    /*for(int i = len - 1; i >= 0; i--) {
        if(action[i] == ".") {
            dotpos = i;
            break();
        }
    }*/
    for(int i = 0; i < len; i++) {
        if(action[i] == " ") {
            spos = i;
            break;
        }
    }
    for(int i = spos + 1; i < len; i++) {
        filename[j] = action[i];
        j++;
    }
    return filename;
}

char* nnamegen(char *filename, char *task) {
    nfilename[0] = task[0];
    for(int i = 1; i < strlen(filename); i++) {
        nfilename[i] = filename[i - 1];
    }
    return nfilename;
}

int keygen() {
    srand(time(0));
    int ranum;
    ranum = (rand() % 8999) + 1000;
    return ranum;
}

void txtencrypt(char *filename, int ekey) {
    FILE *fr;
    FILE *fw;
    char ch;
    /*if(access(filename, F_OK) != -1) {
        fr = fopen(filename, "r");
        fw = fopen(nfilename, "w+");
        char nch;
        int nekey = ekey % 10;
        while((ch = fgetc(fr)) != EOF) {
            nch = ch + nekey;
            fputc(nch, fw);
        }
        printf("%s -> %s | Warning: Simultaneous Existence!", filename, nfilename);
    */
    fr = fopen("textsample.txt", "r");
    if(fr != NULL) {
        fw = fopen("etextsample.txt", "w+");
        //char nch;
        int nekey = ekey % 10;
        while((ch = fgetc(fr)) != EOF) {
            char nch = ch + nekey;
            fputc(nch, fw);
        }
        printf("%s -> %s | Warning: Simultaneous Existence!", filename, nfilename);
    }
    else {
        printf("File not found\n");
    }

}

void txtdecrypt(char *filename, int inkey) {
    FILE *fr;
    FILE *fw;
    char ch;
    /*if(access(filename, F_OK) != -1) {
        fr = fopen(filename, "r");
        fw = fopen(nfilename, "w+");
        char nch;
        int nekey = inkey % 10;
        while((ch = fgetc(fr)) != EOF) {
            nch = ch + nekey;
            fputc(nch, fw);
        }
    printf("%s -> %s | Warning: Simultaneous Existence!",filename, nfilename);
    }*/
    fr = fopen(filename, "r");
    if(fr != NULL) {
       fw = fopen(nfilename, "w+");
        char nch;
        int nekey = inkey % 10;
        while((ch = fgetc(fr)) != EOF) {
            nch = ch + nekey;
            fputc(nch, fw);
        }
    printf("%s -> %s | Warning: Simultaneous Existence!",filename, nfilename);
    }
    else {
        printf("File not found");
        printf("\n");
    }

}


void main() {
	printf("Obtego - Encryption/Decryption Software \n_______________________________\n");
	do {
		printf("ObtegoPrompt> ");
		scanf("%[^\n]%*c", action);
		//for(int i = 0; i < 5; i++) printf("%c",action[i]);
		if(ssfinder(action, "encrypt")==1 && ssfinder(action, ".txt")==1) {
			//fileloc = pathex(action);
            strcpy(task,"encrypt");
			//filename = nameex(action);
			//char x[] = nameex(action);
			strcpy(filename, nameex(action));
			//nfilename = nnamegen(filename, "encrypt");
			//char y[] = nnamegen(filename, "encrypt" )
			strcpy(nfilename, nnamegen(filename, "encrypt"));
			ekey = keygen();
			txtencrypt(filename, ekey);
			//printf("%s -> %s \n Encryption key: %d", filename, nfilename, ekey);
		}
		else if(ssfinder(action, "decrypt")==1 && ssfinder(action, ".txt")==1) {
			//fileloc = pathex(action);
//			task = "decrypt";
			//*filename = nameex(action);
			//char x[] = nameex(action);
			strcpy(filename, nameex(action));
			//*nfilename = nnamegen(filename, "decrypt");
            //char y[] = nnamegen(filename, "decrypt");
			strcpy(nfilename, nnamegen(filename, "decrypt"));
			printf("Enter key> ");
			scanf("%d", &inkey);
			txtdecrypt(filename, inkey);
			//printf("%s -> %s", filename, nfilename);
		}
		/*else if(ssfinder(action, "encrypt")) {
			//fileloc = pathex(action);
			//task = "encrypt";
			*filename = nameex(action);
			*nfilename = nnamegen(filename, "encrypt");
			ekey = keygen();
			genencrypt(filename, ekey);
			//printf("%s -> %s \n Encryption key: %d", filename, nfilename, ekey);
		}
		else if(ssfinder(action, "decrypt")) {
			//fileloc = pathex(action);
			//task = "decrypt";
			*filename = nameex(action);
			*nfilename = nnamegen(filename, "decrypt");
			printf("Enter key> ");
			scanf("%d", inkey);
			genencrypt(filename, inkey);
			//printf("%s -> %s", filename, nfilename);
		}*/
		else if(action == "help") {
            printf("Obtego is a command line encryption/decryption tool \n");
            printf("Enter commands like: \n encrypt file1.txt \n OR decrypt blog3.txt");
		}

	}
	while(action != "exit");
    getch();
}

