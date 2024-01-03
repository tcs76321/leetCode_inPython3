class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result_num_beams = 0
        i = 0
        while i < len(bank) - 1:
            if bank[i].count('1') == 0:
                i += 1
                continue

            k = 1
            while i + k < len(bank):
                if bank[i+k].count('1') == 0:
                    k += 1
                    continue

                result_num_beams += bank[i].count('1') * bank[i+k].count('1')
                break  # Break the inner loop once a pair is found

            i += k  # Update the outer loop to skip the rows already paired

        return result_num_beams
