// import java.util.HashSet;

class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> hash = new HashSet<Integer>();

        int size = nums.length;
        for (int i = 0; i < size; i++) {
            if (hash.contains(nums[i])) {
                return true;
            } else {
                hash.add(nums[i]);
            }
        }

        return false;
    }
}
