class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        index_dict = {}

        for i in range(len(strs)):
            sorted_word = ''.join(sorted(strs[i]))

            if not sorted_word in index_dict:
                output.append([f"{strs[i]}"])
                index_dict.update({sorted_word: len(output) - 1})
                
            else: # else if its already in the output list, first retrieve the index from the index_dict, then append the word into the output of the specific list in the idex?
                index = index_dict.get(f'{sorted_word}')
                output[index].append(strs[i])
        
        return output


# i should create a dictionary that stores the key and value. The key being the sorted word pattern, and the value being the index of where it is being stored in the output list.