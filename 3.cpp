#include <iostream>
#include <bits/stdc++.h>
#define mod 1000000007
using namespace std;

int frogJumpMemo(int index, vector<int> &arr, vector<int> &dp)
{
    if (index == 0)
        return 0;
    else
    {
        if (dp[index] == -1)
        {
            int left = frogJumpMemo(index - 1, arr, dp) +
                       abs(arr[index] - arr[index - 1]);
            int right = INT_MAX;
            if (index - 2 >= 0)
                right = frogJumpMemo(index - 2, arr, dp) +
                        abs(arr[index] - arr[index - 2]);

            return dp[index] = min(left, right);
        }
        else
            return dp[index];
    }
}

int frogJumpTab(int index, vector<int> arr)
{
    vector<int> dp(index + 1, -1);
    dp[0] = 0;
    for (int i = 1; i <= index; i++)
    {
        int right = INT_MAX;
        int left = dp[i - 1] +
                   abs(arr[i] - arr[i - 1]);
        if (i - 2 >= 0)
            right = dp[i - 2] +
                    abs(arr[i] - arr[i - 2]);
        dp[i] = min(right, left);
    }
    return dp[index];
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
    while (test--)
    {
        int steps;
        cin >> steps;
        vector<int> arr;
        for (int i = 0; i < steps; i++)
        {
            int height;
            cin >> height;
            arr.push_back(height);
        }
        // vector<int> dp(steps + 1, -1);
        // cout << frogJumpMemo(steps - 1, arr, dp);
        cout << frogJumpTab(steps - 1, arr);
        cout << endl;
    }
    return 0;
}