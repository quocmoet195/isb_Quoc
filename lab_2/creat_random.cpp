#include <iostream>
#include <cstdlib> 
using namespace std;

int main() {
    int arr[128];
    for (int i = 0; i < 128; ++i) {
        arr[i] = rand() % 2;
    }

    for (int i = 0; i < 128; ++i) {
        cout << arr[i];

    }

    return 0;
}