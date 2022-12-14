#include<iostream>
#include<list>
#include<map>
using namespace std;
class LRUCache {
    list<pair<int, int>> cache;
    map<int,list<pair<int, int>>::iterator> h;
    const int size;
public:
    LRUCache(int capacity):size(capacity){}
    int get(int key) {
        if(h.find(key) != h.end()){
            pair<int, int>p = *(h[key]);
            cache.erase(h[key]);
            h[key] = cache.begin();
            return p.second;
        }
        else return -1;
    }

    void put(int key, int value) {
        if(h.find(key) != h.end()){
            cache.erase(h[key]);
            cache.push_front({key, value});
            h[key] = cache.begin();
        }else{
            cache.push_front({key, value});
            h.insert({key, cache.begin()});
        }
    }
};