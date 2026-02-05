class Solution {

    /**
     * @param String $word1
     * @param String $word2
     * @return String
     */
    function mergeAlternately($word1, $word2) {
        $string = "";
        $word_size1 = strlen($word1);
        $word_size2 = strlen($word2);

        $count1 = 0;
        $count2 = 0;

        while ($count1 < $word_size1 || $count2 < $word_size2) {
            if ($count1 < $word_size1) {
                $string = $string . $word1[$count1];
                $count1++;
            }
            if ($count2 < $word_size2) {
                $string = $string . $word2[$count2];
                $count2++;
            }
        }

        return $string;
    }
}