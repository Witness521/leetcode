package edu.tgu.interviewPre.service;

import java.util.LinkedList;

// 链地址法
public class MyHashSet {
    private final static int BASH = 769;
    private LinkedList[] List = new LinkedList[BASH];

    public MyHashSet() {
        // 初始化成为长度为零的LinkedList
        for (int i = 0; i < BASH; i++) {
            List[i] = new LinkedList<Integer>();
        }
    }

    public void add(int key) {
        int hash_val = hash(key);
        // 子链
        LinkedList<Integer> subchain = List[hash_val];
        for(int i = 0;i < subchain.size();i++){
            Integer element = subchain.get(i);
            if(element == key){
                return;
            }
        }
        subchain.add(key);
    }

    public void remove(int key) {
        int hash_val = hash(key);
        // 子链
        LinkedList<Integer> subchain = List[hash_val];
        for(int i = 0;i < subchain.size();i++){
            Integer element = subchain.get(i);
            if(element == key){
                subchain.remove(element);
            }
        }
    }

    public boolean contains(int key) {
        int hash_val = hash(key);
        // 子链
        LinkedList<Integer> subchain = List[hash_val];
        for(int i = 0;i < subchain.size();i++){
            Integer element = subchain.get(i);
            if(element == key){
                return true;
            }
        }
        return false;
    }

    //哈希方法
    public int hash(int key){
        return key % BASH;
    }

    public static void main(String[] args) {
        MyHashSet myHashSet = new MyHashSet();
        myHashSet.add(3);
        myHashSet.remove(2);
        System.out.println(myHashSet.contains(3));
        System.out.println(myHashSet.contains(2));
    }
}

