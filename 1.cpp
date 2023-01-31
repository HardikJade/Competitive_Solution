#include <iostream>
#include <bits/stdc++.h>
#define mod 1000000007
using namespace std;

int fibonacci(vector<int> dp, int number)
{
    if (number <= 1)
        return number;
    else
        return fibonacci(dp, number - 1) + fibonacci(dp, number - 2);
}
int fibonacciTabular(int number)
{
    vector<int> dp(number + 1, -1);
    dp[0] = 0;
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

    int num;
    cin >> num;
    // vector<int> dp(num, -1);
    // cout << fibonacci(dp, num);

    cout << fibonacciTabular(num);

    return 0;
}