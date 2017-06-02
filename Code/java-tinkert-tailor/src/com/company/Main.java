package com.company;

public class Main {
    public static void main(String[] args) {

        //applying Vector
        TinkerTailorVector ttv = new TinkerTailorVector(5, 3);
        ttv.tinkerTailoring();
        ttv.getResults();
        System.out.println("Result with applying Vector");
        System.out.println(ttv.getResults());

    }
}
