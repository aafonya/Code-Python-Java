package com.company.exercise;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import spark.Request;
import spark.Response;
import spark.template.thymeleaf.ThymeleafTemplateEngine;

import static spark.Spark.*;

/**
 * <h1>Table</h1>
 * Main Class - contains only the main method
 * <p>
 * responsible for starting the web application
 * </p>
 *
 * @author  aafonya
 * @since   2017-05
 */
public class Main {

    private static final Logger logger = LoggerFactory.getLogger(Main.class);

    public static Table table = new Table();


    /**
     * main method - containing default server settings and routes
     * <p>
     * The main building block of our Spark application, the set of
     * our routes.
     */
    public static void main(String[] args) {

	// write your code here
        // default server settings
        exception(Exception.class, (e, req, res) -> e.printStackTrace());
        staticFileLocation("/public");
        port(8888);
        logger.info("Server settings are ready");

        get("/hello", (Request req, Response res) -> {
            logger.info("hello route requested");
            return "hello world";
        });

        get("/index", (Request req, Response res) -> {
            logger.info("index route requested");
            return new ThymeleafTemplateEngine().render(GameController.renderGame(req, res));
        });

        get("/index/:id", (Request req, Response res) -> {
            logger.info("index/:id route requested");
            String StringId = req.params(":id");
            int intId = Integer.parseInt(StringId);
            String result = table.findById(intId);
            return result;
        });
    }
}
