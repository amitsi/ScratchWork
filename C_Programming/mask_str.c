#include <stdio.h>
#include <regex.h>
#include <string.h>

#define MASK_STRING "*****"

/*
 * C code to mask a portion of the string matched by parenthesis enclosed pattern
 * Run: gcc mask_str.c
 * Output:
 *     Pattern: .* password ([^ ]+).*
 *     Match String: list password test123 all files
 *     Masked String: list password ***** all files
 */

char *
mask_str(const char *str, const char *pattern, char *mstr, size_t mstr_len)
{
        regex_t         regex;
        regmatch_t      rematch[2];
        regoff_t        rm_so, rm_eo;

        if (regcomp(&regex, pattern, REG_EXTENDED) != 0) {
		printf("Unable to compile\n");
                return (NULL);
        }
        if (regexec(&regex, str, sizeof (rematch)/sizeof (rematch[0]),
            rematch, 0) == 0) {
                if (rematch[1].rm_so == -1 || rematch[1].rm_eo == -1) {
                        regfree(&regex);
			return (NULL);
                }
                rm_so = rematch[1].rm_so;
                rm_eo = rematch[1].rm_eo;
                memcpy(mstr, str, rm_so);
                memcpy(mstr+rm_so, MASK_STRING, strlen(MASK_STRING));
                memcpy(mstr+rm_so+strlen(MASK_STRING), str+rm_eo,
		    strlen(str) - rm_eo);
                mstr[strlen(str) + strlen(MASK_STRING) + rm_so - rm_eo] = '\0';
        } else {
		printf("Unable to match the pattern\n");
	}
        regfree(&regex);
        return (mstr);
}

int main(void) {
	char	*match_str = "list password test123 all files";
	char	*pattern = ".* password ([^ ]+).*";
	char	*cmd_ptr;
	char	masked_str[128];

	printf("Pattern: %s\n", pattern);
	printf("Match String: %s\n", match_str);
	cmd_ptr = mask_str(match_str, pattern, masked_str,
	    sizeof (masked_str));
	printf("Masked String: %s\n", cmd_ptr);
	return (0);
}
