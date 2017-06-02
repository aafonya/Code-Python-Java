package com.company.exercise;

import java.util.ArrayList;

/**
 * Created by judit on 14.05.17.
 */
public class Team {
    private String name;
    private ArrayList<Person> personList;

    public Team(String name, String code, int id, ArrayList<Person> personList) {
        this.name = name;
        this.personList = personList;
    }

    public void addTopersonList(Person person) {
        personList.add(person);
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ArrayList<Person> getPersonList() {
        return personList;
    }

    public void setPersonList(ArrayList<Person> personList) {
        this.personList = personList;
    }
}
