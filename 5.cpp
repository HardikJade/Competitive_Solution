#include <iostream>
#include <bits/stdc++.h>
#define mod 1000000007
using namespace std;

int maximumNonAdjacentSumMemo(int index, vector<int> &arr, vector<int> dp)
{
    if (index < 0)
        return 0;
    if (index == 0)
        return arr[0];
    else
    {
        if (dp[index] != -1)
            return dp[index];
        int pick = maximumNonAdjacentSumMemo(index - 2, arr, dp) + arr[index];
        int notPick = maximumNonAdjacentSumMemo(index - 1, arr, dp);
        return dp[index] = max(pick, notPick);
    }
}

int f(vector<int> &arr)
{
    vector<int> dp(arr.size() + 1, -1);
    dp[0] = arr[0];
    for (int i = 1; i < arr.size(); i++)
    {
        int pick = INT_MIN;
        int notPick = dp[i - 1] + 0;
        if (i - 2 == 0)
            pick = arr[i] + arr[0];
        else if (i - 2 < 0)
            pick = 0 + arr[i];
        else
            pick = dp[i - 2] + arr[i];
        dp[i] = max(pick, notPick);
    }
    return dp[arr.size() - 1];
}

int maximumNonAdjacentSum(vector<int> &arr)
{
    // int size = arr.size();
    // vector<int> dp(size + 1, -1);
    // return maximumNonAdjacentSumMemo(size - 1, arr, dp);
    return f(arr);
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
        int num;
        cin >> num;
        vector<int> arr;
        for (int i = 0; i < num; i++)
        {
            int temp;
            cin >> temp;
            arr.push_back(temp);
        }
        cout << maximumNonAdjacentSum(arr) << endl;
    }
    return 0;
}