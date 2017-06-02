package com.company;

import java.util.Vector;

/**
 * Created by judit on 06.05.17.
 */
public class TinkerTailorVector {

    private int n;
    private int k;

    private Vector<Integer> tinkerTailorVector = new Vector<>();
    private Vector<Integer> results = new Vector<>();

    TinkerTailorVector(int n, int k) {
        this.n = n;
        this.k = k;

        for (int i = 1; i < n + 1; i++) {
            tinkerTailorVector.add((Integer)i);
        }
    }

    public Vector<Integer> getResults() {
        return results;
    }

    public void tinkerTailoring() {
        int index = 0;

        for(int i = 0; i < n; i++) {
            index += k - 1;

            if (tinkerTailorVector.size() > 1) {
                while (index > (tinkerTailorVector.size() - 1)) {
                    index -= tinkerTailorVector.size();
                }
            } else {
                index = 0;
            }


            Integer removed = tinkerTailorVector.elementAt(index);
            tinkerTailorVector.removeElementAt(index);
            results.add(i, removed);
        }
    }
}

