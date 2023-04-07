#include <iostream>
#include <bits/stdc++.h>
#define mod 1000000007
using namespace std;

int frogJumpK(int index, int k, vector<int> &arr)
{
    vector<int> dp(index + 1, -1);
    dp[0] = 0;
    for (int i = 1; i <= index; i++)
    {
        int current = frogJumpK(index - 1, k, arr) +
                      abs(arr[index] - arr[index - 1]);
        if (i - 2 >= 0)
        {
            for (
                int j = 2;
                j <= (index - k >= 0) ? k : 0;
                j++)
            {
                int actual = frogJumpK(index - j, k, arr) +
                             abs(arr[index] - arr[index - j]);
                current = min(current, actual);
            }
        }
        dp[index] = current;
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
    int n;
    int k;
    cin >> n >> k;
    vector<int> arr;
    for (int i = 0; i < n; i++)
    {
        int height;
        cin >> height;
        arr.push_back(height);
    }

    cout << frogJumpK(n - 1, k, arr);
    return 0;
}