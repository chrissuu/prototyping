#include <iostream>
using namespace std;

auto printHello = []() {
        printf("Hello World!");
};

auto add = [](int a, int b) {
        return a + b;
};

int main() {
        printHello();
        return 0;
}
