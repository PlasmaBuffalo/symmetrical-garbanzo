package SMP.src;

public class App {
    public static void main(String[] args){
        //main loop: starts up running loop and provides user options
        System.out.println("Welcome to course scheduler 0.0.1");
        System.out.println("What would you like to do?");
        //option: modify registry of credits earned
        //option: generate schedule based on available classes/known path
        //option: list course requisites in order?

        /* here's how things go in a basic sense (only working for SMCM):
        0. program starts main loop to either change major, earned credits, or to create a schedule
        1. student declares major and existing earned credits to program, gets saved to storage
        2. program web scrapes classes marked as relevant to major
        3. program cross-references earned credits with classes needed to complete major
        4. program creates a schedule for the next semester, year, etc. using prior year course info
         - we now have a list of courses completed, courses taking, and courses to take

        This tool is focused on helping students with long-term class planning, up to 4 years.
        CORE curriculum should be accounted for

        A priority system should be available to the student to adjust when classes are taken
         - For example, a student should be able to prioritize completion of their language credit
         

         */
    }
}
