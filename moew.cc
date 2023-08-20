#include <iostream>
#include <string>

bool isMeow(const std::string& sound) {
    if (sound.size() < 4)
        return false;

    return (sound[0] == 'm' && sound.find('e') != std::string::npos &&
            sound.find('o') != std::string::npos && sound.find('w') != std::string::npos);
}

bool isPurr(const std::string& sound) {
    if (sound.size() < 4)
        return false;

    return (sound.substr(0, 2) == "pu" && sound.find('r') != std::string::npos);
}

bool isRoar(const std::string& sound) {
    if (sound.size() < 4)
        return false;

    return (sound[0] == 'r' && sound.find('o') != std::string::npos &&
            sound.substr(sound.size() - 2) == "ar");
}

int main() {
    int t;
    std::cin >> t;

    while (t--) {
        std::string sound;
        std::cin >> sound;

        if (isMeow(sound))
            std::cout << "meow\n";
        else if (isPurr(sound))
            std::cout << "purr\n";
        else if (isRoar(sound))
            std::cout << "roar\n";
        else
            std::cout << "human noises\n";
    }

    return 0;
}
