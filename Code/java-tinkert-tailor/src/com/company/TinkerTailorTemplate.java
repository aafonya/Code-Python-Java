package com.company;

/**
 * Created by judit on 07.05.17.
 */
public class TinkerTailorTemplate {

    public static void main(String[] args) {

        TinkerTailorAbstract ttal = new TinkerTailorArrayList(5, 3);
        ttal.showResults();
        TinkerTailorAbstract ttll = new TinkerTailorLinkedList(5, 3);
        ttll.showResults();
    }
}
