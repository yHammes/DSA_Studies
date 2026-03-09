#include <iostream>

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false;

        std::string x_std = std::to_string(x);

        int index = x_std.size();
        std::string x_inverted;

        for (int i = 0; i < x_std.size(); i++) {
            index -= 1;
            x_inverted += x_std[index];
        }
        return x == std::stod(x_inverted);
    }
};