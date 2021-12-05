#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

class Tile {
    public:
        Tile(int x, int y, int number) {
            m_x = x;
            m_y = y;
            m_number = number;
        }
        string toString() {
            return '(' + to_string(m_x) + ',' + to_string(m_y)
                       + ',' + to_string(m_number) + ')';
        }
    private:
        int m_x, m_y, m_number;
        bool m_marked;
};

vector<string> read_file(string file_path) {
    vector<string> ret_vector;
    return ret_vector;
}

void bloop() {
    cout << "bloop blaap\n";
}


int main(int argc, char* argv[]) {
    cout << "Hello world!\n";
    cout << read_file("test.txt").size() << endl;
    Tile my_tile = Tile(1, 3, 24);
    cout << my_tile.toString();

    return 0;
}
