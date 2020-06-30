class RabinKarp:
    def __init__(self):
        self.prime = 1001

    def pattern_matching(self, text, pattern):
        m, n = len(pattern), len(text)
        hash_text, hash_pattern = self.calculate_hash(text, m), self.calculate_hash(pattern, m)

        # start from '1' because [0:0+m] will be used to 'calculate_hash'
        for i in range(1, n-m+1):
            if hash_pattern == hash_text:
                if self.are_equal(text[i-1:i+m-1], pattern[:]):
                    return i-1
            if i < n-m+1:
                # recalculate_hash(input_str, del_idx, add_idx, old_hash, pattern_len)
                # Since we start from 1, in the first pass, '0' idx element will be deleted -> del_idx = i - 1
                # add_idx = i+m-1 and not (i+m) since we have zero indexing
                hash_text = self.recalculate_hash(text, i-1, i+m-1, hash_text, m)
        return -1

    def calculate_hash(self, input_str, len_str):
        hash = 0
        for i in range(len_str):
            hash = hash + ord(input_str[i]) * pow(self.prime, i)
        return hash

    def recalculate_hash(self, input_str, del_idx, add_idx, old_hash, pattern_len):
        new_hash = old_hash - ord(input_str[del_idx])
        new_hash = (new_hash // self.prime) + ord(input_str[add_idx]) * pow(self.prime, pattern_len - 1)
        return new_hash

    def are_equal(self, a, b):
        return a == b


if __name__ == '__main__':
    rk = RabinKarp()
    assert (rk.pattern_matching("anagrams", "gra")) == 3
    assert (rk.pattern_matching("anagrams", "grass")) == -1
    assert (rk.pattern_matching("anagrams", "ram")) == 4

    assert (rk.pattern_matching("DikshaPrakash", "shaP")) == 3


