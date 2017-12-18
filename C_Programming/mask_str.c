#include <stdio.h>
#include <regex.h>
#include <string.h>

#define MASK_STR "*****"

/*
 * C code to mask a portion of the string matched by parenthesis enclosed pattern
 * Run: gcc mask_str.c
 * Output:
 *     Pattern: .* password ([^ ]+).*
 *     Match String: list password test123 all files
 *     Masked String: list password ***** all files
 */

char *
mask_str(char *str, const char *pattern, char *mstr, size_t mstr_len)
{
        regex_t         regex;
        regmatch_t      rematch[2];
        regoff_t        rm_so, rm_eo;
        int             mask_len;

        if (regcomp(&regex, pattern, REG_EXTENDED) != 0) {
		printf("Unable to compile\n");
                return (str);
        }

	mstr[0] = '\0';
        if (regexec(&regex, str, sizeof (rematch)/sizeof (rematch[0]),
            rematch, 0) == 0) {
                rm_so = rematch[1].rm_so;
                rm_eo = rematch[1].rm_eo;
		if (rm_so == -1 || rm_eo == -1) {
                        regfree(&regex);
                        return (str);
                }
                mask_len = strlen(str) + strlen(MASK_STR) - (rm_eo - rm_so);
                /*
		 * Check if masking will not exceed string
		 * length limits
		 */
                if (mask_len >= mstr_len) {
                        regfree(&regex);
                        return (str);
                }
                memcpy(mstr, str, rm_so);
                memcpy(mstr+rm_so, MASK_STR, strlen(MASK_STR));
                memcpy(mstr+rm_so+strlen(MASK_STR), str+rm_eo,
                    strlen(str) - rm_eo);
                mstr[mask_len] = '\0';
        } else {
		printf("Unable to match the pattern: %s\n", pattern);
	}
        regfree(&regex);

	if (mstr[0] == '\0') {
		return (str);
	}
        return (mstr);
}

static char *
mask_password(char *str, char *mstr, size_t mstr_len)
{
	int ii;
        char *cmd_ptr;
        char cmd_buf[128];
        char *mask_patterns[] = {
            ".* password ([^ ]+).*",
            "cli .*-u .+:([^ ]+)",
            "test anything ([^ ]+)"
        };

	cmd_ptr = str;
	for (ii = 0; ii < sizeof(mask_patterns) / sizeof(mask_patterns[0]);
	    ii++) {
		cmd_ptr = mask_str(cmd_ptr, mask_patterns[ii], mstr, mstr_len);
		if (cmd_ptr == mstr) {
			strlcpy(cmd_buf, mstr, mstr_len);
			cmd_ptr = cmd_buf;
		}
	}

        return cmd_ptr;
}

int main(void) {
	char	*match_str = "cli -u net:asdf list password test123 all files test anything hi by";
	char	*cmd_ptr;
	char	masked_str[128];

	printf("Match String: %s\n", match_str);
	cmd_ptr = mask_password(match_str, masked_str,
	    sizeof (masked_str));
	printf("Masked String: %s\n", cmd_ptr);
	return (0);
}
