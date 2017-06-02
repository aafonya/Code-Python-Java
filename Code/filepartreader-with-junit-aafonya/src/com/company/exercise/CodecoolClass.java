package com.company.exercise;

import java.util.ArrayList;

/**
 * Created by judit on 14.05.17.
 */
public class CodecoolClass {
    private String name;
    private ArrayList<Team> teamList;

    public CodecoolClass(String name) {
        this.name = name;
    }

    public void addToteamList(Team team) {
        teamList.add(team);
    }

    public String getName() {
        return name;
    }

    public void setId(String name) {
        this.name = name;
    }

    public ArrayList<Team> getTeamList() {
        return teamList;
    }

    public void setTeamList(ArrayList<Team> teamList) {
        this.teamList = teamList;
    }
}
