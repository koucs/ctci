// implement function void reverse(char* str) in c or c++ which reverses a null-terminated string

#include <iostream>

std::string reverse(char* str) {
    std::string rev_str = "";
    for (int i = (strlen(str) - 1); i >= 0; i--) {
        rev_str += str[i];
    }
    return rev_str;
}

int main(int argc, const char * argv[]) {
    std::cout << reverse("esrever") << std::endl;
    return 0;
}