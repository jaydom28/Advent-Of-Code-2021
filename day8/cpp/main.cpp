#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

pair<vector<string>, vector<string>> parse_signals(string input) {
    // Parses signals from a line of input
    vector<string> mixed, output;
    string temp;
    string mixed_signals = input.substr(0, input.find("|")-1);
    string output_signals = input.substr(input.find("|")+2, input.size());

    for (char &c: mixed_signals) {
        if (c == ' ') {
            mixed.push_back(temp);
            temp.clear();
            continue;
        }
        temp.push_back(c);
    }
    mixed.push_back(temp);
    temp.clear();

    for (char &c: output_signals) {
        if (c == ' ') {
            output.push_back(temp);
            temp.clear();
            continue;
        }
        temp.push_back(c);
    }
    output.push_back(temp);
    return make_pair(mixed, output);

}

vector<string> read_file_lines(string file_path) {
    vector<string> output;
    fstream file;
    file.open(file_path);
    if (!file.is_open()) {
        cout << "ERROR: Unable to open " << file_path << endl;
        return output;
    }

    string line;
    while (getline(file, line)) {
        output.push_back(line);
    }
    return output;
}



int main(int argc, char* argv[]) {
    cout << "Hello world!\n";
    string input_file = "../test.txt";
    vector<string> lines = read_file_lines(input_file);
    for (string line: lines) {
        auto signals = parse_signals(line);
        cout << "outputting mixed signals:\n";
        for (auto sig: signals.first) {
            cout << sig << endl;
        }

        cout << "outputting output signals:\n";
        for (auto sig: signals.second) {
            cout << sig << endl;
        }
    }

    return 0;
}
