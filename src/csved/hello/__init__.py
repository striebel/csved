import sys
import textwrap


def hello_main() -> int:
    hello_str = \
        textwrap.dedent(
            '''\
            /* Kernighan and Ritchie (1978, p. 6) */
            main()
            {
                printf("hello, world\\n");
            }
            '''
        )
    sys.stdout.write(hello_str)
    return 0



