#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {

  char filename[256];
  char path[256];
  char command[512];
  char command1[512];

  if (argc > 0) {
    snprintf(filename, sizeof(filename), "%s", argv[1]);
  }
  else {
    printf("\n[-] Filename (without .nc) >> ");
    scanf("%255s", filename);
  }

  const char *home = getenv("HOME");

  snprintf(command, sizeof(command), "python3 ~/.nullc/nullc.py %s", filename);
  system(command);

  snprintf(path, sizeof(path), "%s/.nullc/filenames.txt", home);

  FILE *file = fopen(path, "r");

  fscanf(file, "%s", filename);

  fclose(file);

  snprintf(command1, sizeof(command1), "gcc program.c -o %s", filename);
  system(command1);
  system("rm program.c");

  return 0;
}
