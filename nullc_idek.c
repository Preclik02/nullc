#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[]) {

  char filename[256];
  char filename_noext[256];
  char command[256];

  if (argc > 1) {
    snprintf(filename, sizeof(filename), "%s", argv[1]);
  } else {
    printf("[-] No filename given.\n");
    return 1;
  }

  strcpy(filename_noext, filename);

  char *dot = strrchr(filename_noext, '.');
  if (dot && strcmp(dot, ".nc") == 0) {
    *dot = '\0';
  }

  snprintf(command, sizeof(command), "nullc %s", filename_noext);
  system(command);

  snprintf(command, sizeof(command), "./%s", filename_noext);
  system(command);

  return 0;
}
