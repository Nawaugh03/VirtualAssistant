The Level Up System is a progression system that allows the user to visualize their progress. This Progression system universally can work with any task the user have completed and make the user gain XP after everything is completed.
There are a few contribution towards the growth of the user which is Urgency (1,2,3,4,5), and priority (1,2,3,4,5).

==**Formula**==
	There are a few types of formulas to calculate how a player earns XP:
	- Linear Progression ==(Base XP + (Level-1) * Increment)==
	- Exponential Progression ==(Base XP * Growth Factor<sup>(Level-1)</sup>)==
	- Quadratic Progression ==(Base XP + k x (Level)<sup>2</sup>)==
	The Exponential Progression Formula seems to be the best use and using 2 parameters can make a good difference in calculating the overall next level in XP
	The Formulas should be the following
	**Next Level XP = Base XP * (Scaling Factor)<sup>(CurrentLevel-1)</sup>** * **Difficulty**
	**Task Score = (Urgency * 0.6 ) * (Priority * 0.4)**
	**XP Gained = Base XP * Task Score**
	Difficulty is based on 5 questions scaled up to 1.2 
	Question 1 (Q1): How troublesome is your journey?
	Question 2 (Q2):  Do you have trouble focusing on your quests?
	Question 3 (Q3):  How Rewarding is your quests?
	Question 4 (Q4): How long are you willing to venture your quest?
	Question 5 (Q5): Are you willing to Complete the quests and 
	Question Weight goal: ==(0.25 \* Q1)+ (0.3 \* Q2)+( 0.28
	 \* Q3) +(0.1 \* Q4) +(0.17 \* Q5) = 1.2 ==
	