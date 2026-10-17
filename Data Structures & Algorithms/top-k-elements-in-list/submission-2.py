class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. first of all, i will need to sort the entire array using .sort() so that everything is sorted. 
        # 2. same like the anagram, i will need to count the frequency of each integer in the array, then update the keys and values inside a dict
        # 3. once done, i should sort the dictionary in order of the highest to lowest value.
        # 4. then depends on the k value (e.g. top 1 most frequent, top 3 most frequent integer in the array), print the key(s).
        
        # Step 1
        # nums.sort()
        
        # Step 2
        freq_dict = {}
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1

        # Step 3
        sorted_dict = dict(sorted(freq_dict.items(), key=lambda item: item[1], reverse=True))

        # Step 4
        keys_dict = list(sorted_dict.keys())
        return keys_dict[:k]

