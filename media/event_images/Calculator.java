package testcode;

import java.util.Scanner;






/**
 * Utility functions for different calculator operations
 */
public class Calculator {

	public Calculator(){}

    
    public void switchTest(int count){
        
        switch(count){
            case 1:
                break;
            
            case 2:
                break;
                
            default:
                break;
        }
        
        switch(count*10){
                
        }
    }
    
    
    
    int x;
    public void method1(String args[]){
        method1(args);
    }
    public void method1(String args[],int x, Test t){
        this.x = 1;
        method1(args);
    }
    
    
    
    
    
    public void testerMethod(int a, int b){
    
        while(a < b){
            System.out.println("a less than b");
        }
        if (a<b){
            // do nothing
        }else{
            System.out.println("a bigger than b");
        }
        while(b < a){
            // do nothing hahah
        }
        
        do{
            // a dooo loop
        }while(b < a);
        
        for (int i = a; i<b; i++){
            System.out.println("For looping a < b");
        }
        
        for (int i = b; i<a; i++){
           /// doooo nothing again
        }
        
        if (false){
            System.out.println("hey");
        }
    }

    /*
	public int add(int a, int b) {
		return a + b;
	}

	public int subtract(int a, int b) {
		return a - b;
	}

	public int multiply(int a, int b) {
		return a * b;
	}

	public int divide(int a, int b) {
		int value = -100000000;
		if (b == 0) {
			System.out.println("Error! Dividing by zero is not allowed.");
		} 
		else if(a==0) {
			//dd
		}
		else {
			value =  a / b;
		}

		return value;
	}



	public int modulo(int a,int b){
		int value = -100000000;
		if (b == 0) {
			System.out.println("Error! Dividing by zero is not allowed.");
		} else {
			value = a % b;
		}
		return value;
	}



	public static int multiply2(int num1, int num2) {
		if (num1 == 0 || num2 == 0) {
			return 0;
		}
		else if(num2 > 0){
			return num1 + multiply2(num1, num2 - 1);
		}
		else if(num1>0) {
		}
		else{
			return -num1 + multiply2(num1, num2 + 1);
		}
	}



	public static void switchCalculator() {

		Scanner reader = new Scanner(System.in);
		System.out.print("Enter two numbers: ");

		double first = reader.nextDouble();
		double second = reader.nextDouble();

		System.out.print("Enter an operator (+, -, *, /): ");
		char operator = reader.next().charAt(0);

		double result;

		switch(operator)
		{
		case '+':
			result = first + second;
			break;

		case '-':
			result = first - second;
			break;

		case '*':
			result = first * second;
			break;

		case '/':
			result = first / second;
			break;
		default:
			System.out.printf("Error! operator is not correct");
			return;
		}
		


		System.out.printf("%.1f %c %.1f = %.1f", first, operator, second, result);
	}

	public void method1(String args[]){
		int x =1;		
		method1(args,x);
	}

	public void method1(String args[],int x){

	}
	
	public static int sumNTimes(int factor, int n) {
        int sum = 0;
		for(int i = 0; i <=n; i++) {
            sum = sum + factor;
		}
		
		return sum;
	}*/
}