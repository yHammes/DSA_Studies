class Solution {
public:
    bool valid(string str1, string str2, int i) {
        int len1 = str1.length(), len2 = str2.length();

        if (len1 % i > 0 || len2 % i > 0) {
            return false;
        }
        string base = str1.substr(0, i);

        return str1 == joinWords(base, len1 / i) && str2 == joinWords(base, len2 / i);
    }

    string joinWords(string str, int ratio) {
        string ans = "";
        for (int i = 0; i < ratio; ++i) {
            ans += str;
        }
        return ans;
    }

    string gcdOfStrings(string str1, string str2) {
        int len1 = str1.length(), len2 = str2.length();

        for (int i = min(len1, len2); i >= 1; --i) {
            if (valid(str1, str2, i)) {
                return str1.substr(0, i);
            }
        }
        return "";
    }
};