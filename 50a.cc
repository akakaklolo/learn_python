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

    for (int i = 0; i < t; i++) {
        std::string sound;
        std::cin >> sound;
        
        if (isMeow(sound))
            std::cout << "meow" << std::endl;
        else if (isPurr(sound))
            std::cout << "purr" << std::endl;
        else if (isRoar(sound))
            std::cout << "roar" << std::endl;
        else
            std::cout << "human noises" << std::endl;
    }
    
    return 0;
}
