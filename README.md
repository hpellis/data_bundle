# Data Bundle

This is a command line program that provides customers with the opportunity to check the balance on their mobile phone and purchase additional credit. 

The program simulates three separate customer interactions, with each customer having a hardcoded password (1111, 2222 and 3333 respectively) and hardcoded balance. Users have three chances to enter the correct password to log in. If they select to top up their credit they must enter and re-enter their mobile number to verify themselves.

Users can then select an amount to top up their credit, provided it is an increment of £5 and lower than their available balance.

I developed this while learning about validation testing, try and except statements. The program also uses if, elif and else statements and while loops.

## Installation
Clone the repository.

```$ git clone https://github.com/hpellis/data_bundle```

Navigate to the directory.

```$ cd data_bundle```

Run the data_bundle_run.py file from the command line.

```$ python data_bundle_run.py```

Running this file runs three customer interactions, requiring user input to select options and verify information.
