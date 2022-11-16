public class trial {
    public static void main(String[] args) {
        System.out.println("Yo. ");
        String my_name = "Ege";
        System.out.println(my_name);
        String new_name = new String("Egeus Salmoneus Modeus Tamaus");
        System.out.println(new_name);
        boolean am_I_gay = false;
        System.out.println(am_I_gay);
        String entire_name = my_name + new_name; // The entire name is Ege Egeus Salmoneus Modeus Tamaus
        int swords = 8;
        String result = entire_name + swords;
        System.out.println(result);
        int brooms = 12;
        String new_result = entire_name + (swords + brooms); 
        System.out.println(new_result);
        System.out.println(my_name == new_name);
        System.out.println(my_name.equals(new_name));
        System.out.println(my_name.equals("Deez nuts lmao haha got'em"));
        System.out.println(!my_name.equals(new_name));
        System.out.println(!entire_name.equals(entire_name));
        System.out.println(my_name.compareTo(new_name));
        System.out.println(result.compareTo(new_name));  /* let's add some
        multiline comments for fun, cuz why not?  */
        System.out.println(5 + 9 + 13 / 46);
        int a_new_result = entire_name.length();
        System.out.println(a_new_result);
        int a_new_length = new_name.length();
        System.out.println(a_new_length);
        String empty_string_name = new String();
        System.out.println(empty_string_name.length());
        empty_string_name = "Ege"; //It's not an empty string anymore! 
        System.out.println(empty_string_name);
    }
}
