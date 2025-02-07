import java.util.Random;
import java.util.Scanner;

public class rockPaperScissors {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        String playerChoice;
        int randomNum;
        String gameResult = "";
        String compChoice;
        String[] choices = new String[3];
        choices[0] = "Rock";
        choices[1] = "Paper";
        choices[2] = "Scissors";

        randomNum = random.nextInt(choices.length);
        compChoice = choices[randomNum];


        System.out.println("Please enter Rock, Paper, or Scissors");
        playerChoice = scanner.nextLine();
        if (playerChoice.equals("Rock") || playerChoice.equals("Paper") || playerChoice.equals("Scissors") ) {
            if (playerChoice.equals(compChoice)) {
                gameResult = "Draw";
            } else if (playerChoice.equals("Paper") && compChoice.equals("Rock")) {
                gameResult = "Player Wins";
            } else if (playerChoice.equals("Scissors") && compChoice.equals("Paper")) {
                gameResult = "Player Wins";
            } else if (playerChoice.equals("Rock") && compChoice.equals("Scissors")) {
                gameResult = "Player Wins";
            } else {
                gameResult = "Computer Wins";
            }
        } else {
            gameResult = "error";
        }
        if (gameResult.equals("error")){
            System.out.println("Please restart and Type Rock, Paper, or Scissors");
        } else {
            System.out.printf("Player chose: %s while the Computer chose: %s\n%s", playerChoice, compChoice, gameResult);
        }
    }
}
