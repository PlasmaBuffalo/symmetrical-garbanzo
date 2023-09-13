package SMP.src;

import java.util.Scanner;
import java.io.BufferedReader;
import java.io.BufferedWriter;

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

        A priority system may be available to the student to adjust when classes are taken
         - For example, a student should be able to prioritize completion of their language credit

        consistency of timing for alternating classes, such as AF/AS classes
        web scraping should be done rarely, not every run
        use python to web scrape
        stage 1 is web scraping
         - need to figure out intermediate file format, will do based on web scraping
         - maybe some type of object containing course name/code, timing, requisites
        stage 2 is calendar/schedule formatting
         - major object:
           - set of required classes
           - set of higher level/electives
           - option of capstone/SMP
         - non-CS classes may be a difficulty
         - consider using multiple tags, such as required, optional, cosc, math, 100, 300, capstone, etc.
         - maybe JSON


         */
    }
}
