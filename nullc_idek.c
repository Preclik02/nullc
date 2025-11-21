#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char* argv[]) {

  char path[256];
  char filename[256];
  char command[256];

  if (argc > 1) {
    snprintf(filename, sizeof(filename), "%s", argv[1]);
  }
  else {
    printf("[+] Something fucked up good luck");
    return 1;
  }

  snprintf(command, sizeof(command), "nullc %s", filename);
  system(command);

  snprintf(command, sizeof(command), "./%s", filename);
  system(command);

  return 0;
}
