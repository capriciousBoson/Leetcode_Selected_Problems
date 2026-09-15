class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList<String>> groups = new HashMap<>();


        for(String s:strs){
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String sortedStr = new String(chars);

            if (! groups.containsKey(sortedStr)){
               groups.put(sortedStr, new ArrayList<String>());
            }
  
            groups.get(sortedStr).add(s);

        }

        return new ArrayList<>(groups.values());
    }
}