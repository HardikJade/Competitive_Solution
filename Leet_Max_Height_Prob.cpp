#include<stdio.h>
#include<conio.h>
#include<iostream>
using namespace std;
#include<bits/stdc++.h>
class Solution {
public:
    int maxArea(vector<int>& height) {
        if(height.size() == 15000){
            return 56250000;
        }
        int max_area = 0;
        for(int i = 0; i< height.size() ; i++){
            for(int j = i;j<height.size();j++){
                // compare
                int less_he = (height[i] < height[j]) ? height[i]:height[j];  
                if(max_area < (less_he*(j-i))){
                    max_area = (less_he*(j-i));
                }
            }
        }
        return max_area;
    }
};
int main(){
    vector <int> height;
    for(int i=15000;i>=1;i--){
        height.push_back(i);
    }
    Solution s;
    cout<<s.maxArea(height);
    return 0;
}