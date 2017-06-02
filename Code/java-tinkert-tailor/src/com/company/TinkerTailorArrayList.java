package com.company;

import java.util.ArrayList;

/**
 * Created by judit on 06.05.17.
 */
public class TinkerTailorArrayList extends TinkerTailorAbstract {

    private ArrayList<Integer> tinkerTailorList = new ArrayList<>();
    private ArrayList<Integer> results = new ArrayList<>();

    TinkerTailorArrayList(int n, int k) {
        super(n, k);

        for (int i = 1; i < n + 1; i++) {
            tinkerTailorList.add((Integer)i);
        }
    }

    public ArrayList<Integer> getTinkerTailorList() { return tinkerTailorList; }

    public ArrayList<Integer> getResults() { return results; }

    public void printResults(){
        System.out.println("ResultList with ArrayList" + "\n");
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
