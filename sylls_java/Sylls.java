
/**
 * Creates a valid syllogism from a mood.  For example, AAA1 where a is A is the letter pertaining to
 * a statement such as All M are P and 1 is the figure. When creating an instance of Syll, use one of
 * the letters listed in the Syll.STATEMENT constant and a number between 1 and 4.
 * Example use:
 * syll = Syll("a","a","a",1)
 *
 
 *
 * @author Kelsey Williams
 * @version 10/4/2022
 */
import java.util.*;
public class Sylls
{
    // instance variables - replace the example below with your own
    private Hashtable<Character,Integer[]> dist_ref = new Hashtable<Character,Integer[]>();
    private static final Character[] STATEMENT = {'a','p','t','k','i','e','b','d','g','o'};
    private static final Integer[][] WEIGHTS = {{5,1},{4,1},{3,1},{2,1},{1,1},{5,5},{4,5},{3,5},{2,5},{1,5}};
    /**
     * Constructor for objects of class Sylls
     */
    public Sylls()
    {
        for(int i = 0; i < STATEMENT.length; i++){
            dist_ref.put(STATEMENT[i],WEIGHTS[i]);
        }
    }
}
