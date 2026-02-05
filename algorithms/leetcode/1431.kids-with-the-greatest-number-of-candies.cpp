class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int maxCandies = 0;
        for (int candy : candies) {
            maxCandies = max(maxCandies, candy);
        }

        vector<bool> greatests;

        for (int candy : candies) {
            greatests.push_back(candy + extraCandies >= maxCandies);
        }
        return greatests;
    }
};