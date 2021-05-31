#include<stdio.h>
#include<conio.h>
#include<iostream>
#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector <int>> result;
        vector<int> temp;
        for(int i = 0;i < nums.size();i++){
            for(int j = i+1;j<nums.size();j++){
                for(int k = j+1;k<nums.size();k++){
                    int a = nums[i];
                    int b = nums[j];
                    int c = nums[k];
                    if((a + b + c) == 0){
                        temp.push_back(a);
                        temp.push_back(b);
                        temp.push_back(c);
                        result.push_back(temp);
                        cout<<a<<endl<<b<<endl<<c<<endl;
                    }
                }
            }
        }
        if(result.size()>2){
            vector<int> k;
            for(int i = 0;i<result.size();i++){
                for(int j=(i+1);j<result.size();j++){
                    if(result[i][0] == result[j][0] ||result[i][0] == result[j][1] ||result[i][0] ==  result[j][2]){
                        if(result[i][1] == result[j][0] || result[i][1] == result[j][1] ||result[i][1] == result[j][2]){
                            if(result[i][2] == result[j][0] || result[i][2] == result[j][1] ||result[i][2] == result[j][2]){
                                
                                result.remove(result.begin,result.end,);
                            }
                            else{break;}
                        }
                        else{break;}
                    }
                    else{break;}
                }
            }
        }
        return result;
    }
};
int main(){
    vector<int> nums;
    nums.push_back(-1);
    nums.push_back(0);
    nums.push_back(1);
    nums.push_back(2);
    nums.push_back(-1);
    nums.push_back(4);
    Solution s;
    vector<vector<int>> rrr = s.threeSum(nums);

    // nums = rrr[0];
    // for(int i = 0;i<nums.size();i++){
    //     cout<<nums[i]<<endl;
    // }

    // for(int i = 0;i < rrr.size();i++){
    //     cout<<rrr[i]<<endl;
    // }
    return 0;
}