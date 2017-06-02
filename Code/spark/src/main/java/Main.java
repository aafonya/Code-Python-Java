import spark.ModelAndView;
import spark.template.thymeleaf.ThymeleafTemplateEngine;

import java.util.HashMap;
import java.util.Map;

import static spark.Spark.get;
import static spark.Spark.port;

public class Main {
    public static void main(String[] args) {
        port(5000);
        //staticFileLocation("/product");

        get("/hello", (req, res) -> "Hello World");

        get("/welcome", (req, res) -> {
            ToDoList todolist = new ToDoList("FirstTitle", 10);

            Map<String, Object> model = new HashMap<>();
            model.put("list", todolist);
            return new ThymeleafTemplateEngine().render(
                    new ModelAndView(model, "product/Welcome")
            );
        });

        get("/", ToDoListController::renderToDoList2, new ThymeleafTemplateEngine());
    }
}
