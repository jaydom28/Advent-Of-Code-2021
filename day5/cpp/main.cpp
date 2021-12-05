#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>

using namespace std;

typedef pair<int, int> coordinate;
typedef pair<coordinate, coordinate> coordinatePair;

string coord_to_string(coordinate input) {
    return '(' + to_string(input.first) + ','
           + to_string(input.second) + ')';
}

coordinate string_to_coord(string input) {
    int fst = stoi(input.substr(0, input.find(",")));
    int snd = stoi(input.substr(input.find(",")+1, input.size()));
    return coordinate(fst, snd);
}

vector<coordinatePair> read_coords(string file_path) {
    fstream file;
    vector<coordinatePair> output;
    file.open(file_path, ios::in);

    if (!file.is_open()) {
        cout << "ERROR: Unable to open file!\n";
        return vector<coordinatePair>();
    }
    
    string line;
    while (getline(file, line)) {
        coordinate fst, snd;
        // cout << "Reading: " << line << endl;
        fst = string_to_coord(line.substr(0, line.find("->")));
        snd = string_to_coord(line.substr(line.find("->") + 3, line.size()));
        output.push_back(coordinatePair(fst, snd));
    }

    file.close();
    return output;
}

vector<coordinate> expand_pair(coordinate a, coordinate b, bool diagonal=false) {
    vector<coordinate> ret_vector;
    coordinate temp;

    if (!diagonal && a.first != b.first && a.second != b.second) {
        return ret_vector;
    }

    int x = a.first, y = a.second;
    int dx = (a.first == b.first) ? 0 : (a.first < b.first) ? 1 : -1;
    int dy = (a.second == b.second) ? 0 : (a.second < b.second) ? 1 : -1;

    while (x != b.first or y != b.second) {
        temp = coordinate(x, y);
        ret_vector.push_back(temp);
        x += dx; y += dy;
    }

    temp = coordinate(x, y);
    ret_vector.push_back(temp);

    return ret_vector;
}

int main(int argc, char* argv[]) {
    vector<coordinatePair> coords = read_coords("../test.txt");
    map<coordinate, int> grid;

    for (auto coord_pair: coords) {
        for (auto coord: expand_pair(coord_pair.first, coord_pair.second)) {
            grid[coord] += 1;
        }

    }

    int part1 = 0;
    for (auto kv: grid) {
        // cout << coord_to_string(kv.first) << " --> " << kv.second << endl;
        if (kv.second >= 2) {
            part1++;
        }
    }
    grid.clear();

    int part2 = 0;
    for (auto coords: coords) {
        cout << "Expanding: " << coord_to_string(coords.first) << " --> "
             << coord_to_string(coords.second) << endl;

        for (auto coord: expand_pair(coords.first, coords.second, true)) {
            cout << coord_to_string(coord) << ' ';;
            grid[coord] += 1;
        }
        cout << endl;
    }

    for (auto kv: grid) {
        if (kv.second >= 2) {
            part2++;
        }
    }

    cout << "Part 1: " << part1 << endl;
    cout << "Part 2: " << part2 << endl;
    return 0;
}
