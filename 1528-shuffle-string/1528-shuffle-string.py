class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        shuffled = [''] * len(s)
        for ch, idx in zip(s, indices):
            shuffled[idx] = ch
        return ''.join(shuffled)

