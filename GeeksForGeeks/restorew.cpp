#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

int main() {
    int tests;
    std::cin >> tests;

    while (tests > 0) {
        tests--;

        int length, k;
        std::cin >> length >> k;

        std::vector<int> temp(length);
        std::vector<int> real(length);

        for (int i = 0; i < length; i++) {
            std::cin >> temp[i];
        }

        for (int i = 0; i < length; i++) {
            std::cin >> real[i];
        }

        std::vector<int> newtemp = temp;
        std::sort(newtemp.begin(), newtemp.end());
        std::sort(real.begin(), real.end());

        std::map<int, std::vector<int>> d;
        for (int i = 0; i < length; i++) {
            d[newtemp[i]].push_back(real[i]);
        }

        for (int i = 0; i < length; i++) {
            std::cout << d[temp[i]].front() << " ";
            d[temp[i]].erase(d[temp[i]].begin());
        }

        std::cout << std::endl;
    }

    return 0;
}
