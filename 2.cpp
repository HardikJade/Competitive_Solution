#include <iostream>
#include <bits/stdc++.h>
#define mod 1000000007
using namespace std;

int countDistinctWaysMemo(vector<int> stair, int nStairs)
{
    if (nStairs <= 1)
        return 1;
    else if (stair[nStairs] != -1)
        return stair[nStairs];
    else
        return stair[nStairs] = countDistinctWaysMemo(stair, nStairs - 1) + countDistinctWaysMemo(stair, nStairs - 2);
}

int countDistinctWaysTab(int number)
{
    vector<int> dp = {-1, -1, -1};
    dp[0] = 1;
    dp[1] = 1;
    for (int i = 2; i <= number; i++)
    {
        dp[2] = dp[0] + dp[1];
        dp[0] = dp[1];
        dp[1] = dp[2];
    }
    return dp[2];
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios::sync_with_stdio(false);
    cin.tie(0);
    int test;
    cin >> test;
    while (--test)
    {
        int number;
        cin >> number;
        cout << countDistinctWaysTab(number)<<endl;
    }
    return 0;
}