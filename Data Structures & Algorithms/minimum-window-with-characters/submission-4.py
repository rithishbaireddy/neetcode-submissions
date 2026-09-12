class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not t or not s:
            return ""

        need = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        have = {}

        left = 0
        have_count = 0
        required = len(need)

        result = ""
        result_len = float("inf")

        for right in range(len(s)):

            ch = s[right]

            if ch in need:
                have[ch] = have.get(ch, 0) + 1

                if have[ch] == need[ch]:
                    have_count += 1

            while have_count == required:

                window_len = right - left + 1

                if window_len < result_len:
                    result_len = window_len
                    result = s[left:right + 1]

                left_ch = s[left]

                if left_ch in need:
                    have[left_ch] -= 1

                    if have[left_ch] < need[left_ch]:
                        have_count -= 1

                left += 1

        return result
        