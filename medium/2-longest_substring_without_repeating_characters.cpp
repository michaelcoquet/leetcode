#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        vector<int> map(128);

        int left = 0;
        int right = 0;

        int largest = 0;
        while (right < s.length())
        {
            char r = s[right];
            map[r]++;

            while (map[r] > 1)
            {
                char l = s[left];
                map[l]--;
                left++;
            }

            largest = max(largest, right - left + 1);

            right++;
        }

        return largest;
    }
};

int main()
{
    Solution s;
    std::cout << "lengOfLongestSubstring = " << s.lengthOfLongestSubstring("abcthabc") << "\n\n";
    return 0;
}