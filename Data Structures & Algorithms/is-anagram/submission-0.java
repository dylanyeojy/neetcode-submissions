class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<String, Integer> map1 = new HashMap<String, Integer>();
        HashMap<String, Integer> map2 = new HashMap<String, Integer>();

        map1 = separateString(s, map1);
        map2 = separateString(t, map2);

        if (map1.equals(map2)) {
            return true;
        } else {
            return false;
        }
    }

    public HashMap<String, Integer> separateString(String s, HashMap<String, Integer> map) {
        // loop through string s and store in the hashmap
        for (int i = 0; i < s.length(); i++) {
            String c = String.valueOf(s.charAt(i));

            if (map.containsKey(c)) {
                int value = map.get(c) + 1;
                map.replace(c, value);
            } else {
                map.put(c, 1);
            }
        }

        return map;
    }
}
