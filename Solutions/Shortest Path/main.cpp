#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'solution' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. 2D_CHARACTER_ARRAY N
 */

const int maxn = 15;

vector<vector<char>> grid;
bool vis[maxn][maxn];
int dy[4] = {0, 0, 1, -1};
int dx[4] = {1, -1, 0, 0};

string dfs(int y, int x, int n){
    
    cout << "vis " << y << " " << x << endl;
    
    vis[y][x] = true;
    
    if (grid[y][x] == '1') return "YES";
    
    bool solved = false;
    
    for (int i = 0; i < 4; i ++){
        int ny = y + dy[i];
        int nx = x + dx[i];
        
        if (ny >= 0 && ny < n && nx >= 0 && nx < n){
            
            if (!vis[ny][nx] && grid[ny][nx] != '#') {
              string res = dfs(ny, nx, n);
                
              if (res == "YES") solved = true;
            }
        }
    }
    if (solved) return "YES";
    return "NO";
    
}

string solution(int n, vector<vector<char>> N) {
    // Code your solution inside this function. Function MUST return a string.
    grid = N;
    
    int sy = -1;
    int sx = -1;
    
    for (int y = 0; y < n; y ++){
        for (int x = 0; x < n; x ++){
            if (grid[y][x] == '0'){
                sy = y;
                sx = x;
            }
        }
   }
    
    cout << sy << " " << sx << endl;
    
    return dfs(sy, sx, n);

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    vector<vector<char>> N(n);

    for (int i = 0; i < n; i++) {
        N[i].resize(n);

        string N_row_temp_temp;
        getline(cin, N_row_temp_temp);

        vector<string> N_row_temp = split(rtrim(N_row_temp_temp));

        for (int j = 0; j < n; j++) {
            char N_row_item = N_row_temp[j][0];

            N[i][j] = N_row_item;
        }
    }

    string result = solution(n, N);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
