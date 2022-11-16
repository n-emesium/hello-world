public class round_me {
    public static void main(String[] args) {
        double a = 23723.232;
        double b = 23123.4373;
        double tolerance = 0.00000000001;
        boolean close_enough = Math.abs(a - b) < tolerance;
        System.out.println(close_enough);
    }
}