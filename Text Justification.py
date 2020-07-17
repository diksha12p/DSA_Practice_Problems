# from typing import List


class Solution(object):
    def text_wrap(self, words: str, max_width: int) -> str:
        if not words:
            return ''

        words = list(words.split())  # str -> List[str]
        # result -> list of sentences, curr -> list of words in current sentence, n_chars -> current character count
        result, curr, n_chars = [], [], 0

        for w in words:
            if n_chars + len(curr) + len(w) > max_width:
                # 1 word left
                if len(curr) == 1:
                    result.append(curr[0] + ' ' * (max_width - n_chars))
                else:
                    num_spaces = max_width - n_chars
                    # '-1' below indicates that the last word in 'curr' doesn't need a space after it
                    spaces_bw_words, extra_spaces = divmod(num_spaces, len(curr) - 1)

                    # Taking care of extra spaces first in a 'Round Robin' manner
                    for i in range(extra_spaces):
                        curr[i] += ' '
                    # Taking care of the spaces between words
                    result.append((' ' * spaces_bw_words).join(curr))
                # Reinitialize for the next sentence
                curr, n_chars = [], 0
            # If 'w' has to be appended in the same sentence ->. no overflow yet
            curr.append(w)
            n_chars += len(w)
        # Handling teh left over words
        # n(padding) to be inserted -> number of spaces left
        result.append(' '.join(curr) + ' ' * (max_width - n_chars - len(curr) + 1))
        return '\n'.join(result)


if __name__ == '__main__':
    sol = Solution()
    para = "Four score and seven years ago our fathers brought forth upon this continent a new nation, conceived in " \
           "liberty and dedicated to the proposition that all men are created equal"
    width = 13

    file1 = open("output_text_warp.txt", "w")
    file1.write(sol.text_wrap(para, width))
    file1.close()