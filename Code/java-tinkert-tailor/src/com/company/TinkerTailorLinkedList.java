package com.company;

import java.util.LinkedList;

/**
 * Created by judit on 06.05.17.
 */
public class TinkerTailorLinkedList extends TinkerTailorAbstract {

    private LinkedList<Integer> tinkerTailorList = new LinkedList<>();
    private LinkedList<Integer> results = new LinkedList<>();

    TinkerTailorLinkedList(int n, int k) {
        super(n, k);

        for (int i = 1; i < n + 1; i++) {
            tinkerTailorList.add((Integer)i);
        }
    }

    public LinkedList<Integer> getTinkerTailorList() { return tinkerTailorList; }

    public LinkedList<Integer> getResults() {
        return results;
    }

    public void printResults(){
        System.out.println("ResultList with LinkedList" + "\n");
        System.out.println(getResults());
    }

    public void tinkerTailoring() {
        int index = 0;

        for(int i = 0; i < n; i++) {
            index += k - 1;

            if (tinkerTailorList.size() > 1) {
                while (index > (tinkerTailorList.size() - 1)) {
                    index -= tinkerTailorList.size();
                }
            } else {
                index = 0;
            }


            results.add(tinkerTailorList.remove(index));
        }
    }
}
