package com.company.exercise;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * <h1>Table</h1>
 * Table Class - contains the attributes of the table
 * <p>
 * responsible for containing the data about the table for the game
 * </p>
 *
 * @author  aafonya
 * @since   2017-05
 */
public class Table {

    private static final Logger logger = LoggerFactory.getLogger(Table.class);

    private int size;

    private int level;

    /**
     * Getter of the variable numbers(which contains the elements of the table)
     *
     * @return the numbers in the table
     */
    public int[][] getNumbers() {
        return numbers;
    }

    /**
     * Contains the elements of the table
     */
    private int[][] numbers = {{0,1,0},{0,0,1},{1,0,0}};

    /**
     * Looking for an element of the table by the id shown on the button
     *
     * @param  id id of the button
     * @return value of the element in the table
     */
    public String findById(int id){
        int i = id / numbers.length;
        int j = id % numbers.length;
        int result = numbers[i][j];
        if (result == 1) {
            return "*";
        }
        return String.valueOf(numbers[i][j]);
    }

    /**
     * Getter of the height of the table
     *
     * @return int - value of height
     */
    public int getHeight() {
        logger.info("Height" + numbers.length);
        return numbers.length;
    }

    /**
     * Getter of the width of the table
     *
     * @return int - value of width
     */
    public int getWidth(){
        logger.info("Width" + numbers[0].length);
        return numbers[0].length;
    }

    public Table () {
    }

    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }

    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }
}
