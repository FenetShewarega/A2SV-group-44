class Solution(object):
    def compress(self, chars):
        
            insert = 0
            groupLength = 1
            chars.append(' ')

            for i in range(1, len(chars)):
                if chars[i] == chars[i - 1]:
                    groupLength += 1
                    continue

                chars[insert] = chars[i - 1]
                insert += 1
                if groupLength== 1:
                    continue

                for digit in str(groupLength):
                    chars[insert] = digit
                    insert += 1

                groupLength = 1

            return insert
        