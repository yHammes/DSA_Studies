class Solution {

    /**
     * @param String $text
     * @param String $brokenLetters
     * @return Integer
     */
    function canBeTypedWords($text, $brokenLetters) {
        $words = explode(" ", $text);
        $text = strtolower($text);
        $count = 0;

        foreach ($words as $word) {
            $cannotType = false;
            foreach (str_split($brokenLetters) as $brokenLetter) {
                if (str_contains($word, $brokenLetter)) {
                    $cannotType = true;
                    break;
                }
            }
            if (!$cannotType) {
                $count++;
            }
        }
        return $count;
    }
}