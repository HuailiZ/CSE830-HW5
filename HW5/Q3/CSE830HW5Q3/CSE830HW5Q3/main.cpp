//
//  main.cpp
//  CSE830HW5Q3
//
//  Created by Huaili Zeng on 3/21/23.
//

#include <iostream>
#include <stdio.h>
#include <unordered_set>
#include <map>
#include <ctime>
#include <algorithm>
#include <numeric>
#include <fstream>
using namespace std;

// build the function to calculate the running time of insertion under different data structure
// hash table
double cal_running_time_um(int n) {
    std:: unordered_multiset<int> un_ml;
    // calculate the insertion time
    std::clock_t start_time = std::clock();
    for (int i = 0; i < n; i++){
        un_ml.insert(i);
    }
    std::clock_t end_time = std::clock() - start_time;
    double duration_time_um = ((double) end_time) / (double) CLOCKS_PER_SEC;
    
    return duration_time_um;
}

// binary tree
double cal_running_time_mm(int n) {
    std:: multimap<int, int> mm;
    // calculate the insertion time
    std::clock_t start_time = std::clock();
    for (int i = 0; i < n; i ++) {
        mm.insert(pair(i, i));
    }
    std::clock_t end_time = std::clock() - start_time;
    double duration_time_mm = ((double) end_time) / (double) CLOCKS_PER_SEC;
    
    return duration_time_mm;
}

int main(int argc, const char * argv[]) {

    // store the insertion time of each data structure
    ofstream ofile;
    ofile.open("results.txt", ios::out | ios::trunc);
    
    double duration_time_um = 0.0;
    double duration_time_mm = 0.0;
    
    int x[10];
    double dt_um[10]; // duration time of unordered multiset
    double dt_ms[10]; // duration time of multimap
    
    int n = 1;
    int counter = 0;
    
    while(duration_time_um < 3.0 && duration_time_mm < 3.0){
        n = n * 10;
        x[counter] = n;
        cout << "N: " << n << std::endl;
        
        // first calculate the running time of unordered multimap
        duration_time_um = cal_running_time_um(n);
        
        // if the running time of each insertion is too short
        // we might need to run multiple epochs
        if (duration_time_um < 0.001) {
            double duration_time_um_loops = 0;
            for (int j = 0; j < 10; j++){
                duration_time_um_loops += cal_running_time_um(n);
            }
            duration_time_um = duration_time_um_loops / 10.0;
        }
        dt_um[counter] = duration_time_um;
        std::cout << "Time of unordered multiset: "
            << duration_time_um
            << " seconds" << std::endl;
        
        // then calculate the running time of multiset
        duration_time_mm = cal_running_time_mm(n);
        
        // if the running time of each insertion is too short
        // we might need to run multiple epochs
        if (duration_time_mm < 0.001) {
            double duration_time_mm_loops = 0;
            for (int j = 0; j < 10; j++){
                duration_time_mm_loops += cal_running_time_mm(n);
            }
            duration_time_mm = duration_time_mm_loops / 10.0;
        }
        dt_ms[counter] = duration_time_mm;
        std::cout << "Time of multiset: "
            << duration_time_mm
            << " seconds" << std::endl;
        
        counter += 1;
    }
    
    if (ofile.is_open()) {
        for (int i = 0; i < 10; i++) {
            if (x[i] != 0) {
                ofile << x[i] << "," << dt_um[i] << "," << dt_ms[i] << endl;
            }
            else break;
        }
        ofile.close();
    }
    else std::cout << "Unable to open file";
    return 0;
}
