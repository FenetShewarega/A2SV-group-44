class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
            
        n_cards = len(deck)

        cards_counter = list(Counter(deck).values())
        min_card_counts = min(cards_counter)

        x = 2
        while x <= min_card_counts:

            flag = True
            for card_count in cards_counter:
                if card_count % x != 0:
                    flag = False
                    break
            if flag == True:
                return(x)
            else:
                # try next
                x += 1
        return(False)
