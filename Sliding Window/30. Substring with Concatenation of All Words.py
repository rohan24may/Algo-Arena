class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        if total_len > len(s):
            return []

        # Required frequency of each word
        target = {}
        for word in words:
            target[word] = target.get(word, 0) + 1

        answer = []

        # Try every possible alignment
        for offset in range(word_len):

            left = offset
            right = offset

            window = {}
            count = 0

            while right + word_len <= len(s):

                word = s[right:right + word_len]
                right += word_len

                # Word isn't required → reset window
                if word not in target:
                    window.clear()
                    count = 0
                    left = right
                    continue

                # Add word to current window
                window[word] = window.get(word, 0) + 1
                count += 1

                # Too many copies → remove from left
                while window[word] > target[word]:
                    left_word = s[left:left + word_len]
                    window[left_word] -= 1
                    left += word_len
                    count -= 1

                # Exactly all words found
                if count == word_count:
                    answer.append(left)

                    # Move window forward to search for next match
                    left_word = s[left:left + word_len]
                    window[left_word] -= 1
                    left += word_len
                    count -= 1

        return answer