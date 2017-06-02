package com.company.exercise;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import spark.ModelAndView;
import spark.Request;
import spark.Response;

import java.util.HashMap;
import java.util.Map;
/**
 * Controlling the table that are shown
 * <p>
 * Responsible for generate as many buttons as many needed for show the table.
 *  </p>
 *
 */
public class GameController {

    private static final Logger logger = LoggerFactory.getLogger(GameController.class);

    /**
     * Renders the table.
     * <p>
     * Returns a Stark ModelAndView object, what contains information about the size of the table.
     * <p>
     *
     * @param  req Request object, provides information about the HTTP request
     * @param res Response object, provides information about the HTTP request
     * @return ModelAndView object to be rendered (it sets the name of the view and the model object to be rendered).
     */
    public static ModelAndView renderGame(Request req, Response res) {
        Table table = Main.table;
        Map params = new HashMap<>();
        params.put("height", table.getHeight());
        params.put("width", table.getWidth());
        params.put("table", table);
        logger.info("Table getting" + table.toString());
        return new ModelAndView(params, "game/game");
    }


}
