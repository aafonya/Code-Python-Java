package com.company.exercise;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class Main {

    private static final Logger logger = LoggerFactory.getLogger(Main.class);
    public static void main(String[] args) {
        logger.info("I am informative!");

        Wombat w = new Wombat();
        w.setTemperature(10);
        w.setTemperature(29);
        w.setTemperature(31);
        w.setTemperature(51);
    }
}
