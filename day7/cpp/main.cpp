#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <tuple>
#include <cmath>

using namespace std;

string output_vector(vector<int> input) {
    string output;
    for (int f: input) {
        output += to_string(f) + ',';
    }
    return output;
}

vector<int> read_crabs(string file_path) {
    vector<int> output;
    fstream file;
    string line, temp;

    file.open(file_path, ios::in);
    if (!file.is_open()) {
        cout << "ERROR: Unable to open file!\n";
        return output;
    }
    
    getline(file, line);
    file.close();

    for (char c: line) {
        if (c == ',') {
            output.push_back(stoi(temp));
            temp.clear();
            continue;
        }
        temp += c;
        // cout << "Temp so far: " << temp << endl;
    }

    output.push_back(stoi(temp));

    return output;
}

tuple<map<int, int>,int,int> get_crab_counts(vector<int> crabs) {
    map<int, int> counter;
    int min = crabs[0], max = crabs[0];
    for (int &crab: crabs) {
        counter[crab] += 1;
        if (crab > max) max = crab;
        if (crab < min) min = crab;
    }
    return make_tuple(counter, min, max);
}

int get_fuel_cost(map<int, int> crab_counts, int position) {
    int sum = 0;
    for (pair<int,int> kv: crab_counts) {
        sum += abs(kv.first - position) * kv.second;
    }
    return sum;
}

int check_possible_positions(map<int,int> crab_counts, int min, int max) {
    int lowest_fuel_cost;
    int temp;
    for (int i = min; i <= max; i++) {
        temp = get_fuel_cost(crab_counts, i);
        if (i == min) lowest_fuel_cost = temp;
        if (temp < lowest_fuel_cost) lowest_fuel_cost = temp;
    }
    return lowest_fuel_cost;
}

int get_fuel_cost2(map<int,int> crab_counts, int position) {
    int sum = 0;
    int temp;
    for (pair<int,int> kv: crab_counts) {
        for (int i=0; i <= abs(kv.first - position); i++) {
            sum += i * kv.second;
        }
    }
    return sum;
}

int check_possible_positions2(map<int,int> crab_counts, int min, int max) {
    int lowest_fuel_cost;
    int temp;
    for (int i = min; i <= max; i++) {
        temp = get_fuel_cost2(crab_counts, i);
        if (i == min) lowest_fuel_cost = temp;
        if (temp < lowest_fuel_cost) lowest_fuel_cost = temp;
    }
    return lowest_fuel_cost;
}


int main(int argc, char* argv[]) {
    string file_path = "../input.txt";
    vector<int> crabs = read_crabs(file_path);
    map<int, int> crab_counts;
    int min, max;
    tie(crab_counts, min, max) = get_crab_counts(crabs);
    cout << "Crabs: " << output_vector(crabs) << endl;
    cout << "Lowest fuel cost: " << check_possible_positions(crab_counts, min, max) << endl;

    cout << "Lowest fuel cost2: " << check_possible_positions2(crab_counts, min, max) << endl;
    return 0;
}
