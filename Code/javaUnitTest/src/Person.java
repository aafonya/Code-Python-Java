/**
 * Created by judit on 10.05.17.
 */
public class Person {

    private String name;
    private Integer age;

    public Person(String name, Integer age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;

    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        if (age < 0) throw new IllegalArgumentException("Age cannot be lower zero");
        this.age = age;
    }
}
