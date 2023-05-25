#include <stdio.h>
#include <unistd.h>
#include <sys/syscall.h>

#define futex(a, b, c, d, e, f) syscall(SYS_futex, a, b, c, d, e, f)

int main(void)
{
int rc;

  rc = futex((int *)0, 0, 0, (const struct timespec *)0, (int *)0, 0);
  printf("rc=%d\n", rc);

  return 0;
} // main
