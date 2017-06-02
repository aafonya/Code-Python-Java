package com.company.exercise;

import java.util.ArrayList;
import java.io.*;

public class Main {

    public static void main(String[] args) throws FileNotFoundException {
        readingFile();
        printData();
    }

    public static ArrayList<String> dataFromReading = new ArrayList<>();
    public static ArrayList<Person> persons = new ArrayList<>();
    public static ArrayList<Team> teams = new ArrayList<>();
    public static ArrayList<CodecoolClass> classes = new ArrayList<CodecoolClass>();

    public static void createObjects() {
        int i = 0;
        while (i < (dataFromReading.size()/3)) {
            for (int j = 0; j < 3; j++) {
                if (j == 0) {
                    String className = dataFromReading.get(i + j);
                    for (CodecoolClass cclass: classes) {
                        if (cclass.getName().equals(className)) {
                            break;
                        } else {

                        }
                    }
                } else if (j == 1) {
                    String teamName = dataFromReading.get(i + j);
                } else if (j == 2) {
                    String personName = dataFromReading.get(i + j);
                }
            }
            i += 3;
        }

    }

    public static void printData() {
        for (String stringy : dataFromReading) {
            System.out.println(stringy);
        }
    }

    private static void readingFile() throws FileNotFoundException {
        // Open the file
        FileInputStream fstream = null;

            fstream = new FileInputStream("names.txt");

        BufferedReader br = new BufferedReader(new InputStreamReader(fstream));

        String strLine;

        //Read File Line By Line
        try {
            while ((strLine = br.readLine()) != null)   {
                //System.out.println (strLine);
                for (String retval: strLine.split("/")) {
                   //System.out.println(retval);
                   dataFromReading.add(retval);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

//Close the input stream
        try {
            br.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void populateData() {

        Person A = new Person("A");
        persons.add(A);
        Person B = new Person("B");
        persons.add(B);
        Person C = new Person("C");
        persons.add(C);
        Person D = new Person("D");
        persons.add(D);
        Person E = new Person("A");
        persons.add(E);
        Person F = new Person("B");
        persons.add(F);
        Person G = new Person("C");
        persons.add(G);
        Person H = new Person("D");
        persons.add(H);
        Person I = new Person("A");
        persons.add(I);
        Person J = new Person("B");
        persons.add(J);
        Person K = new Person("C");
        persons.add(K);
        Person L = new Person("D");
        persons.add(L);
        Person M = new Person("A");
        persons.add(M);
        Person N = new Person("B");
        persons.add(N);
        Person O = new Person("C");
        persons.add(O);
        Person P = new Person("D");
        persons.add(P);
        Person Q = new Person("A");
        persons.add(Q);
        Person R = new Person("B");
        persons.add(R);
        Person S = new Person("C");
        persons.add(S);
        Person T = new Person("D");
        persons.add(T);
        Person V = new Person("A");
        persons.add(V);
        Person W = new Person("B");
        persons.add(W);
        Person X = new Person("C");
        persons.add(X);
        Person Y = new Person("D");
        persons.add(Y);
        Person Z = new Person("A");
        persons.add(Z);
        Person ZA = new Person("B");
        persons.add(ZA);

    }

}
