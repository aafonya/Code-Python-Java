package com.company;
import java.util.List;
/**
 * Created by judit on 07.05.17.
 */
public abstract class TinkerTailorAbstract {

    protected int n;
    protected int k;

    protected List TinkerTailorList;
    protected List results;

    TinkerTailorAbstract(int n, int k) {
        this.n = n;
        this.k = k;
    }

    abstract List getTinkerTailorList();

    public void printOriginalList(){
        System.out.println("Original List" + "\n");
        System.out.println(getTinkerTailorList());
    }

    abstract void tinkerTailoring();

    abstract List getResults();

    abstract void printResults();

    //template method
    public final void showResults(){

        getTinkerTailorList();

        printOriginalList();

        tinkerTailoring();

        printResults();
    }
}
