#include<stdio.h>
#include<conio.h>
#include<iostream>
#include<bits/stdc++.h>
using namespace std;
class Solution {
    public:
        double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
            // Creating The Result Array vector

            for(int i=0;i<nums2.size();i++){
                nums1.push_back(nums2[i]);
            }
            sort(nums1.begin(),nums1.end());

            // For Even Segment
            if(nums1.size()%2 == 0){
                if(nums1.size() == 0){
                    return 0.000f;
                }
                else{
                    int med = nums1.size()/2;
                    double ans = ((double)(nums1[med-1] + nums1[med]))/2;
                    return (ans);
                }
            }
            // For Odd Segment
            else{
                int med = nums1.size()/2;
                return(nums1[med]);
            }
        }
};
int main(){
    Solution s;
    vector <int> n1;
    vector <int> n2;

    n1.push_back(1);
    n1.push_back(2);

    n2.push_back(3);
    n2.push_back(4);
    cout<<s.findMedianSortedArrays(n1,n2);
    return 0;
}