#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>


using namespace std;

typedef int fish;

string output_vector(vector<fish> fishes) {
    string output;
    for (fish f: fishes) {
        output += to_string(f) + ',';
    }
    return output;
}

vector<fish> read_data(string file_path) {
    fstream file;
    vector<fish> output;
    string line, temp;

    file.open(file_path, ios::in);
    if (!file.is_open()) {
        cout << "ERROR: Unable to open file!\n";
        return output;
    }
    
    getline(file, line);
    file.close();

    cout << line << endl;
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

vector<long int> get_fish_counts(vector<fish> fishes) {
    vector<long int> counts;
    for (int i = 0; i < 9; i++) {
        counts.push_back(0);
    }

    for (fish &f: fishes) {
        counts[f] += 1;    
    }
    return counts;
}

void smart_update_fishes(vector<long int> &counts) {
    int num_new_fish = counts[0];
    for (int i = 0; i < 8; i++) {
        counts[i] = counts[i+1];
    }
    counts[6] += num_new_fish;
    counts[8] = num_new_fish;
}


void update_fishes(vector<fish> &fishes) {
    vector<fish> babies;
    for (fish &f: fishes) {
        if (f == 0) {
            f = 7;
            babies.push_back(8);
        }
        f--;
    }

    for (fish &f: babies) {
        fishes.push_back(f);
    }
    return;
}

unsigned int get_sum(vector<long int> &numbers) {
    unsigned int sum = 0;
    for (long int &num: numbers) {
        sum += num;
    }
    return sum;
}

int main(int argc, char* argv[]) {
    string file_path = "../test.txt";
    // Read in the fish
    // vector<fish> fishes = read_data("../test.txt");
    vector<long int> counts = get_fish_counts(read_data(file_path));
    // cout << "Initial state: " << output_vector(fishes) << endl;

    for (int i=0; i < 18; i++) {
        smart_update_fishes(counts);
        // cout << "After " << i+1 << "days:   "
        //      << output_vector(fishes) << endl;
        // if (i == 5) break;
    }

    cout << "After 18 days: " << get_sum(counts) << endl;

    counts = get_fish_counts(read_data(file_path));
    for (int i=0; i < 80; i++) {
        smart_update_fishes(counts);
        // cout << "After " << i+1 << "days:   "
        //      << output_vector(fishes) << endl;
        // if (i == 5) break;
    }

    cout << "Part 1: " << get_sum(counts) << endl;

    counts = get_fish_counts(read_data(file_path));
    for (int i=0; i < 256; i++) {
        smart_update_fishes(counts);
        // cout << "After " << i+1 << "days:   "
        //      << output_vector(fishes) << endl;
        // if (i == 5) break;
    }

    cout << "Part 2: " << get_sum(counts) << endl;
    return 0;
}
